import pandas
import footballframe
import nfldpw.players
import nfldpw.drafts
from .. import cleaning
import pickle
import nfldpw.ids
import tqdm
import os
import types


class IDKeeper:
    def __init__(self):
        pass

    def _path(self, cache_path: str) -> str:
        return cache_path + "idkeeper.csv"

    def load(self, cache_path: str):
        path = self._path(cache_path)
        self.df = pandas.DataFrame(
            {id_header[nfldpw.ids.MODULE_DEFAULT]: [] for id_header in nfldpw.ids.LIST}
        )
        if os.path.exists(path):
            self.df = pandas.concat([self.df, pandas.read_csv(path, index_col=0)])

    def exists(self, ids: dict[int, str]) -> bool:
        exists = False
        for id_key_index in ids:
            id_key = nfldpw.ids.LIST[id_key_index]
            id = ids[id_key_index]
            df_ids = self.df[id_key[nfldpw.ids.MODULE_DEFAULT]]
            if id in df_ids.values:
                exists = True
                break
        return exists

    def dump(self, cache_path: str):
        path = self._path(cache_path)
        self.df.to_csv(path, index=True)

    def append(self, pid: int, id_dict: dict[str, str]):
        self.df.loc[pid] = id_dict

    def __len__(self):
        return len(self.df)


def _pickle_path(pid: int, cache_path: str) -> str:
    return cache_path + "player-" + str(pid) + ".pickle"


def load(pid: int, cache_path: str) -> footballframe.Player:
    player = None
    with open(_pickle_path(pid, cache_path), "rb") as file:
        player = pickle.load(file)
    return player


def dump(player: footballframe.Player, pid: int, cache_path: str):
    with open(_pickle_path(pid, cache_path), "wb") as file:
        pickle.dump(player, file)


def new_from_player(player_series: pandas.Series) -> footballframe.Player:
    player = footballframe.Player()
    player.set_info(
        cleaning.str_or_none(player_series[nfldpw.players.cols.FirstName.header]),
        cleaning.str_or_none(player_series[nfldpw.players.cols.LastName.header]),
        cleaning.datetime_or_none(
            player_series[nfldpw.players.cols.BirthDate.header], "%Y-%m-%d"
        ),
        cleaning.int_or_none(player_series[nfldpw.players.cols.Height.header]),
        cleaning.int_or_none(player_series[nfldpw.players.cols.Weight.header]),
    )
    return player


def update_from_player(
    player_df: pandas.DataFrame,
    id_map: pandas.DataFrame,
    player_cache: str,
    nfl_cache: str,
):
    idkeep = IDKeeper()
    idkeep.load(player_cache)
    for index in player_df.index:
        ids = {
            nfldpw.ids.LIST.index(id_header): player_df.get(
                nfldpw.ids.id_col(id_header, nfldpw.players),
                pandas.Series({index: None}),
            )[index]
            for id_header in nfldpw.ids.LIST
        }
        if not idkeep.exists(ids):
            player_series = player_df.iloc[index]
            player = new_from_player(player_series)
            pid = len(idkeep)
            dump(player, pid, player_cache)
            id_series = nfldpw.ids.id_map_lookup(id_map, ids)
            print(id_series)
            id_dict = {
                nfldpw.ids.LIST[i][nfldpw.ids.MODULE_DEFAULT]: ids[i] for i in ids
            }
            idkeep.append(
                pid,
            )


def update_from_draft(draft_df: pandas.DataFrame, player_cache: str, nfl_cache: str):
    pass


# def update_from_player_info(player_df: pandas.DataFrame, player_cache: str):
#     idkeep = IDKeeper()
#     idkeep.load(player_cache)
#     for index in player_df.index:

#         pid = len(idkeep.df)
#         player_series = player_df.iloc[index]
#         player = new_from_player(player_series)
#         dump(player, pid, player_cache)
#         idkeep.append(
#             pid,
#             {
#                 id_header[ids.MODULE_DEFAULT]: player_series.get(
#                     ids.id_col(id_header, nfldpw.players), None
#                 )
#                 for id_header in ids.LIST
#             },
#         )
#         idkeep.dump(player_cache)


# def update_from_draft(draft_df: pandas.DataFrame, player_cache: str):
#     idkeep = ids.IDKeeper()
#     idkeep.load(player_cache)
#     draft_df = draft_df[
#         ~draft_df[ids.id_col(ids.CFBREF, nfldpw.drafts)].isin(
#             idkeep.df[ids.CFBREF[ids.MODULE_DEFAULT]]
#         )
#     ]
#     draft_df = draft_df.reset_index()
#     for index in draft_df.index:
#         pid = len(idkeep.df)
#         player_series = draft_df.iloc[index]
#         player = footballframe.Player()
#         dump(player, pid, player_cache)
#         idkeep.append(
#             pid,
#             {
#                 id_header[ids.MODULE_DEFAULT]: player_series.get(
#                     ids.id_col(id_header, nfldpw.drafts), None
#                 )
#                 for id_header in ids.LIST
#             },
#         )
#         idkeep.dump(player_cache)

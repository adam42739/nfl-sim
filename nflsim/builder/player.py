import pandas
import footballframe
import nfldpw.players.cols as cols
from . import cleaning
import pickle


def _pickle_path(pid: str, cache_path: str) -> str:
    return cache_path + "player-" + pid + ".pickle"


def load(pid: str, cache_path: str) -> footballframe.Player:
    player = None
    with open(_pickle_path(pid, cache_path), "rb") as file:
        player = pickle.load(file)
    return player


def dump(player: footballframe.Player, pid: str, cache_path: str):
    with open(_pickle_path(pid, cache_path), "wb") as file:
        pickle.dump(player, file)


def new(
    player_series: pandas.Series, pid: str, cache_path: str = None
) -> footballframe.Player:
    player = footballframe.Player()
    player.set_info(
        cleaning.str_or_none(player_series[cols.FirstName.header]),
        cleaning.str_or_none(player_series[cols.LastName.header]),
        cleaning.datetime_or_none(player_series[cols.BirthDate.header], "%Y-%m-%d"),
        cleaning.int_or_none(player_series[cols.Height.header]),
        cleaning.int_or_none(player_series[cols.Weight.header]),
    )
    if cache_path:
        dump(player, pid, cache_path)
    return player

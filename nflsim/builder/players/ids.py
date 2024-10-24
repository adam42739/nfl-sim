import pandas
import os
import nfldpw.drafts
import types
import nfl_data_py


MODULE_DEFAULT = "mdef"

YAHOO = {MODULE_DEFAULT: "yahoo_id"}
ESB = {MODULE_DEFAULT: "esb_id"}
SMART = {MODULE_DEFAULT: "smart_id"}
NFL = {MODULE_DEFAULT: "nfl_id"}
ESPN = {MODULE_DEFAULT: "espn_id"}
ROTOWORLD = {MODULE_DEFAULT: "rotoworld_id"}
GSIS = {MODULE_DEFAULT: "gsis_id"}
SLEEPER = {MODULE_DEFAULT: "sleeper_id"}
STATS = {MODULE_DEFAULT: "stats_id"}
SPORTRADAR = {MODULE_DEFAULT: "sportradar_id"}
CBS = {MODULE_DEFAULT: "cbs_id"}
STATS_GLOBAL = {MODULE_DEFAULT: "stats_global_id"}
CFBREF = {MODULE_DEFAULT: "cfbref_id", nfldpw.drafts: "cfb_player_id"}
FLEAFLICKER = {MODULE_DEFAULT: "fleaflicker_id"}
FANTASYPROS = {MODULE_DEFAULT: "fantasypros_id"}
FANTASY_DATA = {MODULE_DEFAULT: "fantasy_data_id"}
PFF = {MODULE_DEFAULT: "pff_id"}
MFL = {MODULE_DEFAULT: "mfl_id"}
PFR = {MODULE_DEFAULT: "pfr_id", nfldpw.drafts: "pfr_player_id"}
ROTOWIRE = {MODULE_DEFAULT: "rotowire_id"}
KTC = {MODULE_DEFAULT: "ktc_id"}
SWISH = {MODULE_DEFAULT: "swish_id"}


def id_col(id: dict[str | types.ModuleType, str], module: types.ModuleType) -> str:
    if module in id:
        return id[module]
    else:
        return id[MODULE_DEFAULT]


LIST = [
    YAHOO,
    ESB,
    SMART,
    NFL,
    ESPN,
    ROTOWORLD,
    GSIS,
    SLEEPER,
    STATS,
    SPORTRADAR,
    CBS,
    STATS_GLOBAL,
    CFBREF,
    FLEAFLICKER,
    FANTASYPROS,
    FANTASY_DATA,
    PFF,
    MFL,
    PFR,
    ROTOWIRE,
    KTC,
    SWISH,
]


class IDKeeper:
    def __init__(self):
        pass

    def _path(self, cache_path: str) -> str:
        return cache_path + "idkeeper.csv"

    def load(self, cache_path: str):
        path = self._path(cache_path)
        self.df = pandas.DataFrame(
            {id_header[MODULE_DEFAULT]: [] for id_header in LIST}
        )
        if os.path.exists(path):
            self.df = pandas.concat([self.df, pandas.read_csv(path, index_col=0)])

    def dump(self, cache_path: str):
        path = self._path(cache_path)
        self.df.to_csv(path, index=True)

    def append(self, pid: int, id_dict: dict[str, str]):
        self.df.loc[pid] = id_dict


def get_mapping(cache_path: str = None, refresh=False) -> pandas.DataFrame:
    if cache_path:
        path = cache_path + "player_ids.csv"
        if os.path.exists(path) and refresh == False:
            return pandas.read_csv(path)
        else:
            df = nfl_data_py.import_ids()
            df.to_csv(path)
            return df
    else:
        return nfl_data_py.import_ids()

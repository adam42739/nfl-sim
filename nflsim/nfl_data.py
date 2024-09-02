import nfl_data_py
import datetime
import pandas
import json
import os
from nflsim.nfl_data_cols import *

####################################
# define numpy.float_ to fix
# outdated use of it in nfl_data_py
####################################
import numpy

numpy.float_ = numpy.float64
####################################


def to_indexed_dict(pd_dict, obj_key):
    indexed_dict = {}
    for key in pd_dict:
        if key != obj_key:
            indexed_dict[key] = {}
            for id in pd_dict[key]:
                indexed_dict[key][pd_dict[key][id]] = None
        else:
            for id_key in indexed_dict:
                for id in pd_dict[obj_key]:
                    indexed_dict[id_key][pd_dict[id_key][id]] = pd_dict[obj_key][id]
    return indexed_dict


START_YEAR = 2002


def _this_year():
    today = datetime.datetime.today()
    if today.month < 6:
        return today.year - 1
    else:
        return today.year


THIS_YEAR = _this_year()

PBP_CACHE_PATH = "/pbp_cache/"


def _cache_pbp(year):
    nfl_data_py.cache_pbp([year], alt_path=os.path.dirname(__file__) + PBP_CACHE_PATH)


def _get_pbp_metadata():
    path = os.path.dirname(__file__) + PBP_CACHE_PATH + "metadata.json"
    metadata = {}
    with open(path, "r") as file:
        metadata = json.load(file)
    return metadata


def _write_pbp_metadata(metadata):
    path = os.path.dirname(__file__) + PBP_CACHE_PATH + "metadata.json"
    with open(path, "w") as file:
        json.dump(metadata, file)


def get_pbp(years):
    metadata = _get_pbp_metadata()
    dfs = []
    for year in years:
        if year == THIS_YEAR:
            dfs.append(nfl_data_py.import_pbp_data([year]))
        else:
            if str(year) not in metadata:
                _cache_pbp(year)
                metadata[year] = None
            dfs.append(
                nfl_data_py.import_pbp_data(
                    [year],
                    cache=True,
                    alt_path=os.path.dirname(__file__) + PBP_CACHE_PATH,
                )
            )
    df = pandas.concat(dfs, ignore_index=True, sort=False)
    _write_pbp_metadata(metadata)
    return df


def get_schedules(years):
    COLUMNS = [
        COLS.SCHEDULES.GSIS,
        COLS.SCHEDULES.SEASON,
        COLS.SCHEDULES.WEEK,
        COLS.SCHEDULES.GAME_TYPE,
        COLS.SCHEDULES.GAMEDAY,
        COLS.SCHEDULES.WEEKDAY,
        COLS.SCHEDULES.GAMETIME,
        COLS.SCHEDULES.HOME_TEAM,
        COLS.SCHEDULES.AWAY_TEAM,
        COLS.SCHEDULES.HOME_REST,
        COLS.SCHEDULES.AWAY_REST,
        COLS.SCHEDULES.LOCATION,
    ]
    df = nfl_data_py.import_schedules(years)
    df = df[COLUMNS]
    df[COLS.SCHEDULES.GAMEDAY] = pandas.to_datetime(df[COLS.SCHEDULES.GAMEDAY])
    return df


PLAYERS_COLUMNS_KEEP = [
    COLS.ROSTERS.PLAYER_ID,
    COLS.ROSTERS.PLAYER_NAME,
    COLS.ROSTERS.FIRST_NAME,
    COLS.ROSTERS.LAST_NAME,
    COLS.ROSTERS.POSITION,
    COLS.ROSTERS.HEIGHT,
    COLS.ROSTERS.WEIGHT,
    COLS.ROSTERS.BIRTH_DATE,
    COLS.ROSTERS.DRAFT_CLUB,
    COLS.ROSTERS.ENTRY_YEAR,
]


def get_players(rosters, drafts):
    df = rosters[PLAYERS_COLUMNS_KEEP]
    df.drop_duplicates()
    df = pandas.merge(
        df,
        drafts,
        how="left",
        left_on=[
            COLS.ROSTERS.PLAYER_NAME,
            COLS.ROSTERS.DRAFT_CLUB,
            COLS.ROSTERS.ENTRY_YEAR,
            COLS.ROSTERS.POSITION,
        ],
        right_on=[
            COLS.DRAFTS.PFR_PLAYER_NAME,
            COLS.DRAFTS.TEAM,
            COLS.DRAFTS.SEASON,
            COLS.DRAFTS.POSITION,
        ],
    )
    COLUMNS_DROP = [
        COLS.ROSTERS.DRAFT_CLUB,
        COLS.ROSTERS.ENTRY_YEAR,
        COLS.DRAFTS.PFR_PLAYER_NAME,
        COLS.DRAFTS.TEAM,
    ]
    df = df.drop(COLUMNS_DROP, axis=1)
    return df


ROSTER_CACHE_PATH = "/roster_cache/"


ROSTERS_COLUMNS_KEEP = [
    COLS.ROSTERS.TEAM,
    COLS.ROSTERS.SEASON,
    COLS.ROSTERS.WEEK,
    COLS.ROSTERS.PLAYER_ID,
]


def _load_rosters(year):
    df = nfl_data_py.import_weekly_rosters([year])
    COLUMNS_KEEP = ROSTERS_COLUMNS_KEEP + PLAYERS_COLUMNS_KEEP
    COLUMNS_KEEP = list(set(COLUMNS_KEEP))
    df = df[COLUMNS_KEEP]
    return df


def _cache_rosters(year):
    df = _load_rosters(year)
    path = os.path.dirname(__file__) + ROSTER_CACHE_PATH + str(year) + ".csv"
    df.to_csv(path)


def _get_rosters_metadata():
    path = os.path.dirname(__file__) + ROSTER_CACHE_PATH + "metadata.json"
    metadata = {}
    with open(path, "r") as file:
        metadata = json.load(file)
    return metadata


def _write_roster_metadata(metadata):
    path = os.path.dirname(__file__) + ROSTER_CACHE_PATH + "metadata.json"
    with open(path, "w") as file:
        json.dump(metadata, file)


def get_rosters(years):
    metadata = _get_rosters_metadata()
    dfs = []
    for year in years:
        if year == THIS_YEAR:
            df = _load_rosters(year)
            dfs.append(df)
        else:
            if str(year) not in metadata:
                _cache_rosters(year)
                metadata[year] = None
            path = os.path.dirname(__file__) + ROSTER_CACHE_PATH + str(year) + ".csv"
            dfs.append(pandas.read_csv(path))
    df = pandas.concat(dfs, ignore_index=True, sort=False)
    df[COLS.ROSTERS.BIRTH_DATE] = pandas.to_datetime(df[COLS.ROSTERS.BIRTH_DATE])
    _write_roster_metadata(metadata)
    return df


def get_teams():
    COLUMNS_KEEP = [
        COLS.TEAMS.ABBR,
        COLS.TEAMS.NAME,
        COLS.TEAMS.ID,
        COLS.TEAMS.CONF,
        COLS.TEAMS.DIVISION,
    ]
    df = nfl_data_py.import_team_desc()
    df = df[COLUMNS_KEEP]
    return df


def get_drafts(years):
    COLUMNS = [
        COLS.DRAFTS.SEASON,
        COLS.DRAFTS.ROUND,
        COLS.DRAFTS.PICK,
        COLS.DRAFTS.PFR_PLAYER_NAME,
        COLS.DRAFTS.POSITION,
        COLS.DRAFTS.TEAM,
    ]
    df = nfl_data_py.import_draft_picks(years)
    df = df[COLUMNS]
    return df


MISC_CACHE_PATH = "/misc_cache/"


def _check_cache_dir(dir_name):
    path = os.path.dirname(__file__) + dir_name
    if not os.path.exists(path):
        os.mkdir(path)


def _check_cache_dirs():
    _check_cache_dir(PBP_CACHE_PATH)
    _check_cache_dir(ROSTER_CACHE_PATH)
    _check_cache_dir(MISC_CACHE_PATH)


_check_cache_dirs()

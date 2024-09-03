import nfl_data_py
import datetime
import pandas
import json
import os
from nflsim import cols

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
        cols.schedules.GSIS,
        cols.schedules.SEASON,
        cols.schedules.WEEK,
        cols.schedules.GAME_TYPE,
        cols.schedules.GAMEDAY,
        cols.schedules.WEEKDAY,
        cols.schedules.GAMETIME,
        cols.schedules.HOME_TEAM,
        cols.schedules.AWAY_TEAM,
        cols.schedules.HOME_REST,
        cols.schedules.AWAY_REST,
        cols.schedules.LOCATION,
    ]
    df = nfl_data_py.import_schedules(years)
    df = df[COLUMNS]
    df[cols.schedules.GAMEDAY] = pandas.to_datetime(df[cols.schedules.GAMEDAY])
    return df


PLAYERS_COLUMNS_KEEP = [
    cols.rosters.PLAYER_ID,
    cols.rosters.PLAYER_NAME,
    cols.rosters.FIRST_NAME,
    cols.rosters.LAST_NAME,
    cols.rosters.POSITION,
    cols.rosters.HEIGHT,
    cols.rosters.WEIGHT,
    cols.rosters.BIRTH_DATE,
    cols.rosters.DRAFT_CLUB,
    cols.rosters.ENTRY_YEAR,
]


def get_players(rosters, drafts):
    df = rosters[PLAYERS_COLUMNS_KEEP]
    df.drop_duplicates()
    df = pandas.merge(
        df,
        drafts,
        how="left",
        left_on=[
            cols.rosters.PLAYER_NAME,
            cols.rosters.DRAFT_CLUB,
            cols.rosters.ENTRY_YEAR,
            cols.rosters.POSITION,
        ],
        right_on=[
            cols.drafts.PFR_PLAYER_NAME,
            cols.drafts.TEAM,
            cols.drafts.SEASON,
            cols.drafts.POSITION,
        ],
    )
    COLUMNS_DROP = [
        cols.rosters.DRAFT_CLUB,
        cols.rosters.ENTRY_YEAR,
        cols.drafts.PFR_PLAYER_NAME,
        cols.drafts.TEAM,
    ]
    df = df.drop(COLUMNS_DROP, axis=1)
    return df


ROSTER_CACHE_PATH = "/roster_cache/"


ROSTERS_COLUMNS_KEEP = [
    cols.rosters.TEAM,
    cols.rosters.SEASON,
    cols.rosters.WEEK,
    cols.rosters.PLAYER_ID,
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
    df[cols.rosters.BIRTH_DATE] = pandas.to_datetime(df[cols.rosters.BIRTH_DATE])
    _write_roster_metadata(metadata)
    return df


def get_teams():
    COLUMNS_KEEP = [
        cols.teams.ABBR,
        cols.teams.NAME,
        cols.teams.ID,
        cols.teams.CONF,
        cols.teams.DIVISION,
    ]
    df = nfl_data_py.import_team_desc()
    df = df[COLUMNS_KEEP]
    return df


def get_drafts(years):
    COLUMNS = [
        cols.drafts.SEASON,
        cols.drafts.ROUND,
        cols.drafts.PICK,
        cols.drafts.PFR_PLAYER_NAME,
        cols.drafts.POSITION,
        cols.drafts.TEAM,
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

import nfl_data_py
import datetime
import pandas
import json

####################################
# define numpy.float_ to fix
# outdated use of it in nfl_data_py
####################################
import numpy

numpy.float_ = numpy.float64
####################################

START_YEAR = 1999


def _this_year():
    today = datetime.datetime.today()
    if today.month < 6:
        return today.year - 1
    else:
        return today.year


THIS_YEAR = _this_year()

PBP_CACHE_PATH = "pbp_cache/"


def cache_pbp(year):
    nfl_data_py.cache_pbp([year], alt_path=PBP_CACHE_PATH)


def get_pbp_metadata():
    path = PBP_CACHE_PATH + "metadata.json"
    metadata = {}
    with open(path, "r") as file:
        metadata = json.load(file)
    return metadata


def write_pbp_metadata(metadata):
    path = PBP_CACHE_PATH + "metadata.json"
    with open(path, "w") as file:
        json.dump(metadata, file)


def get_pbp(years):
    metadata = get_pbp_metadata()
    dfs = []
    for year in years:
        if year == THIS_YEAR:
            dfs.append(nfl_data_py.import_pbp_data([year]))
        else:
            if str(year) not in metadata:
                cache_pbp(year)
                metadata[year] = None
            dfs.append(
                nfl_data_py.import_pbp_data([year], cache=True, alt_path=PBP_CACHE_PATH)
            )
    df = pandas.concat(dfs, ignore_index=True, sort=False)
    write_pbp_metadata(metadata)
    return df


def get_schedules(years):
    COLUMNS = [
        "gsis",
        "season",
        "week",
        "game_type",
        "gameday",
        "weekday",
        "gametime",
        "home_team",
        "away_team",
        "home_rest",
        "away_rest",
        "location",
    ]
    df = nfl_data_py.import_schedules(years)
    df = df[COLUMNS]
    df["gameday"] = pandas.to_datetime(df["gameday"])
    return df


def get_players():
    COLUMNS_KEEP = [
        "mfl_id",
        "sportradar_id",
        "fantasypros_id",
        "gsis_id",
        "pff_id",
        "sleeper_id",
        "nfl_id",
        "espn_id",
        "yahoo_id",
        "fleaflicker_id",
        "cbs_id",
        "pfr_id",
        "cfbref_id",
        "rotowire_id",
        "rotoworld_id",
        "ktc_id",
        "stats_id",
        "stats_global_id",
        "fantasy_data_id",
        "swish_id",
        "name",
        "position",
        "birthdate",
        "draft_year",
        "draft_round",
        "draft_pick",
        "height",
        "weight",
        "college",
    ]
    df = nfl_data_py.import_ids(COLUMNS_KEEP)
    df = df[COLUMNS_KEEP]
    df["birthdate"] = pandas.to_datetime(df["birthdate"])
    return df


ROSTER_CACHE_PATH = "roster_cache/"


def cache_rosters(year):
    COLUMNS_KEEP = ["team", "season", "week", "player_id"]
    df = nfl_data_py.import_weekly_rosters([year])
    df = df[COLUMNS_KEEP]
    path = ROSTER_CACHE_PATH + str(year) + ".csv"
    df.to_csv(path)


def get_rosters_metadata():
    path = ROSTER_CACHE_PATH + "metadata.json"
    metadata = {}
    with open(path, "r") as file:
        metadata = json.load(file)
    return metadata


def write_roster_metadata(metadata):
    path = ROSTER_CACHE_PATH + "metadata.json"
    with open(path, "w") as file:
        json.dump(metadata, file)


def get_rosters(years):
    metadata = get_rosters_metadata()
    dfs = []
    for year in years:
        if year == THIS_YEAR:
            dfs.append(nfl_data_py.import_weekly_rosters([year]))
        else:
            if str(year) not in metadata:
                cache_rosters(year)
                metadata[year] = None
            path = ROSTER_CACHE_PATH + str(year) + ".csv"
            dfs.append(pandas.read_csv(path))
    df = pandas.concat(dfs, ignore_index=True, sort=False)
    write_roster_metadata(metadata)
    return df

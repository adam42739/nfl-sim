import nfl_data_py
import datetime
import pandas

####################################
# define numpy.float_ to fix
# outdated use of it in nfl_data_py
####################################
import numpy

numpy.float_ = numpy.float64
####################################


def this_year():
    today = datetime.datetime.today()
    if today.month < 6:
        return today.year - 1
    else:
        return today.year


THIS_YEAR = this_year()

CACHE_PATH = "pbp_cache/"


def cache_pbp(years):
    nfl_data_py.cache_pbp(years, alt_path=CACHE_PATH)


def get_pbp(years):
    return nfl_data_py.import_pbp_data(years, cache=True, alt_path=CACHE_PATH)


#    self,
#         gsis,
#         season,
#         week,
#         type,
#         date,
#         weekday,
#         home,
#         away,
#         location,
#         home_rest,
#         away_rest,


def get_schedule(years):
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

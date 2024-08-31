import nfl_data_py

####################################
# define numpy.float_ to fix
# outdated use of it in nfl_data_py
####################################
import numpy

numpy.float_ = numpy.float64
####################################

import datetime


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

def get_schedule(years):
    return nfl_data_py.import_schedules(years)

import nfl_data_py
import datetime


def this_year():
    today = datetime.datetime.today()
    if today.month < 6:
        return today.year - 1
    else:
        return today.year


THIS_YEAR = this_year()

CACHE_PATH = "pbp_cache/"

def cache(years=[THIS_YEAR]):
    nfl_data_py.cache_pbp(years, downcast=True, alt_path=CACHE_PATH)


def get(years):
    return nfl_data_py.import_pbp_data(years, downcast=True, cache=True, alt_path=CACHE_PATH)

df = get([2023])
new = df[["time_to_throw", "sack", "was_pressure"]]
new = new[new["sack"]==1]
print(new.head(10))

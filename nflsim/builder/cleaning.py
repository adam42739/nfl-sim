import datetime
import math

def str_or_none(string) -> str:
    string = str(string)
    if (
        isinstance(string, str)
        and string != "None"
        and string != "NaN"
        and string != "nan"
        and string != None
        and string != math.nan
    ):
        return str(string)
    else:
        return None


def datetime_or_none(string, format: str) -> datetime.datetime:
    string = str(string)
    if (
        isinstance(string, str)
        and string != "None"
        and string != "NaN"
        and string != "nan"
        and string != None
        and string != math.nan
    ):
        return datetime.datetime.strptime(string, format)
    else:
        return


def int_or_none(string) -> int:
    string = str(string)
    if (
        isinstance(string, str)
        and string != "None"
        and string != "NaN"
        and string != "nan"
        and string != None
        and string != math.nan
    ):
        return int(float(string))
    else:
        return

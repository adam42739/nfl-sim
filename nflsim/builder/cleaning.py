import datetime


def str_or_none(string: str) -> str:
    if string == "None" or string == "NaN" or string == None:
        return None
    else:
        return str(string)


def datetime_or_none(string: str, format: str) -> datetime.datetime:
    if string == "None" or string == "NaN" or string == None:
        return None
    else:
        return datetime.datetime.strptime(string, format)


def int_or_none(string: str) -> int:
    if string == "None" or string == "NaN" or string == None:
        return None
    else:
        return int(string)

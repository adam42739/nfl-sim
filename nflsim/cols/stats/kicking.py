from nflsim.cols.stats import types


GP = "GP"
FG = "FG"
FGA = "FGA"
FGP = "FG%"
Y01_19 = "1-19"
Y20_29 = "20-29"
Y30_39 = "30-39"
Y40_49 = "40-49"
Y50P = "50+"
LNG = "LNG"
XPM = "XPM"
XPA = "XPA"
PTS = "PTS"

DICT = {
    GP: {types.TYPE: types.ACCUM, types.PARAM: None},
    FG: {types.TYPE: types.ACCUM, types.PARAM: None},
    FGA: {types.TYPE: types.ACCUM, types.PARAM: None},
    FGP: {types.TYPE: types.AVG, types.PARAM: {"X": [FG], "Y": [FGA]}},
    Y01_19: {types.TYPE: types.ACCUM, types.PARAM: None},
    Y20_29: {types.TYPE: types.ACCUM, types.PARAM: None},
    Y30_39: {types.TYPE: types.ACCUM, types.PARAM: None},
    Y40_49: {types.TYPE: types.ACCUM, types.PARAM: None},
    Y50P: {types.TYPE: types.ACCUM, types.PARAM: None},
    LNG: {types.TYPE: types.MAX, types.PARAM: None},
    XPM: {types.TYPE: types.ACCUM, types.PARAM: None},
    XPA: {types.TYPE: types.ACCUM, types.PARAM: None},
    PTS: {types.TYPE: types.ACCUM, types.PARAM: None},
}

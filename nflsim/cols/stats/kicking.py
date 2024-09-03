from nflsim.cols.stats import types


GP = "GP"
FG = "FG"
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
    GP: types.ACCUM,
    FG: types.ACCUM,
    FGP: types.AVG,
    Y01_19: types.ACCUM,
    Y20_29: types.ACCUM,
    Y30_39: types.ACCUM,
    Y40_49: types.ACCUM,
    Y50P: types.ACCUM,
    LNG: types.MAX,
    XPM: types.ACCUM,
    XPA: types.ACCUM,
    PTS: types.ACCUM,
}

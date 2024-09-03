from nflsim.cols.stats import types


GP = "GP"
REC = "REC"
TGTS = "TGTS"
YDS = "YDS"
AVG = "AVG"
TD = "TD"
LNG = "LNG"
FD = "FD"
FUM = "FUM"
LST = "LST"

DICT = {
    GP: types.ACCUM,
    REC: types.ACCUM,
    TGTS: types.ACCUM,
    YDS: types.ACCUM,
    AVG: types.AVG,
    TD: types.ACCUM,
    LNG: types.MAX,
    FD: types.ACCUM,
    FUM: types.ACCUM,
    LST: types.ACCUM,
}

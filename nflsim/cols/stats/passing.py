from nflsim.cols.stats import types


GP = "GP"
CMP = "CMP"
ATT = "ATT"
CMPP = "CMP%"
YDS = "YDS"
AVG = "AVG"
TD = "TD"
INT = "INT"
LNG = "LNG"
SACK = "SACK"

DICT = {
    GP: types.ACCUM,
    CMP: types.ACCUM,
    ATT: types.ACCUM,
    CMPP: types.AVG,
    YDS: types.ACCUM,
    AVG: types.AVG,
    TD: types.ACCUM,
    INT: types.ACCUM,
    LNG: types.MAX,
    SACK: types.ACCUM,
}

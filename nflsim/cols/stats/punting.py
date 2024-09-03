from nflsim.cols.stats import types


GP = "GP"
PUNTS = "PUNTS"
AVG = "AVG"
LNG = "LNG"
YDS = "YDS"
TB = "TB"
TBP = "TB%"
IN20 = "IN20"
IN20P = "IN20%"
ATT = "ATT"
RYDS = "RYDS"
RAVG = "RAVG"
NET = "NET"

DICT = {
    GP: types.ACCUM,
    PUNTS: types.ACCUM,
    AVG: types.AVG,
    LNG: types.MAX,
    YDS: types.ACCUM,
    TB: types.ACCUM,
    TBP: types.AVG,
    IN20: types.ACCUM,
    IN20P: types.AVG,
    ATT: types.ACCUM,
    RYDS: types.ACCUM,
    RAVG: types.AVG,
    NET: types.AVG,
}

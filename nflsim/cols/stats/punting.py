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

DICT = {
    GP: {types.TYPE:types.ACCUM,types.PARAM:None},
    PUNTS: {types.TYPE:types.ACCUM,types.PARAM:None},
    AVG: {types.TYPE:types.AVG, types.PARAM:{"X":[YDS],"Y":[PUNTS]}},
    LNG: {types.TYPE:types.MAX,types.PARAM:None},
    YDS: {types.TYPE:types.ACCUM,types.PARAM:None},
    TB: {types.TYPE:types.ACCUM,types.PARAM:None},
    TBP:{types.TYPE:types.AVG, types.PARAM:{"X":[TB],"Y":[PUNTS]}},
    IN20: {types.TYPE:types.ACCUM,types.PARAM:None},
    IN20P: {types.TYPE:types.AVG, types.PARAM:{"X":[IN20],"Y":[PUNTS]}},
    ATT: {types.TYPE:types.ACCUM,types.PARAM:None},
    RYDS: {types.TYPE:types.ACCUM,types.PARAM:None},
    RAVG: {types.TYPE:types.AVG, types.PARAM:{"X":[RYDS],"Y":[ATT]}},
}

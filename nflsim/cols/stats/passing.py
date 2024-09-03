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
    GP: {types.TYPE:types.ACCUM,types.PARAM:None},
    CMP: {types.TYPE:types.ACCUM,types.PARAM:None},
    ATT: {types.TYPE:types.ACCUM,types.PARAM:None},
    CMPP: {types.TYPE:types.AVG, types.PARAM:{"X":[CMP],"Y":[ATT]}},
    YDS: {types.TYPE:types.ACCUM,types.PARAM:None},
    AVG: {types.TYPE:types.AVG, types.PARAM:{"X":[YDS],"Y":[ATT]}},
    TD: {types.TYPE:types.ACCUM,types.PARAM:None},
    INT: {types.TYPE:types.ACCUM,types.PARAM:None},
    LNG: {types.TYPE:types.MAX,types.PARAM:None},
    SACK: {types.TYPE:types.ACCUM,types.PARAM:None},
}

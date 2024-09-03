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
    GP: {types.TYPE:types.ACCUM,types.PARAM:None},
    REC: {types.TYPE:types.ACCUM,types.PARAM:None},
    TGTS: {types.TYPE:types.ACCUM,types.PARAM:None},
    YDS: {types.TYPE:types.ACCUM,types.PARAM:None},
    AVG: {types.TYPE:types.AVG, types.PARAM:{"X":[YDS],"Y":[REC]}},
    TD: {types.TYPE:types.ACCUM,types.PARAM:None},
    LNG: {types.TYPE:types.MAX,types.PARAM:None},
    FD: {types.TYPE:types.ACCUM,types.PARAM:None},
    FUM: {types.TYPE:types.ACCUM,types.PARAM:None},
    LST: {types.TYPE:types.ACCUM,types.PARAM:None},
}

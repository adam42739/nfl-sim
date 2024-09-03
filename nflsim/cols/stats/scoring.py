from nflsim.cols.stats import types


GP = "GP"
PASS = "PASS"
RUSH = "RUSH"
REC = "REC"
RET = "RET"
TD = "TD"
TWOPT = "2PT"
PAT = "PAT"
FG = "FG"
PTS = "PTS"

DICT = {
    GP: {types.TYPE:types.ACCUM,types.PARAM:None},
    PASS: {types.TYPE:types.ACCUM,types.PARAM:None},
    RUSH: {types.TYPE:types.ACCUM,types.PARAM:None},
    REC: {types.TYPE:types.ACCUM,types.PARAM:None},
    RET: {types.TYPE:types.ACCUM,types.PARAM:None},
    TD: {types.TYPE:types.ACCUM,types.PARAM:None},
    TWOPT: {types.TYPE:types.ACCUM,types.PARAM:None},
    PAT: {types.TYPE:types.ACCUM,types.PARAM:None},
    FG: {types.TYPE:types.ACCUM,types.PARAM:None},
    PTS: {types.TYPE:types.ACCUM,types.PARAM:None},
}

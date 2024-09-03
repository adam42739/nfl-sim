from nflsim.cols.stats import types


GP = "GP"
TOT = "TOT"
SOLO = "SOLO"
AST = "AST"
SACK = "SACK"
FF = "FF"
FR = "FR"
FYDS = "FYDS"
INT = "INT"
IYDS = "IYDS"
TD = "TD"
LNG = "LNG"
PD = "PD"
STF = "STF"
STFYDS = "STFYDS"
KB = "KB"

DICT = {
    GP: {types.TYPE:types.ACCUM,types.PARAM:None},
    TOT: {types.TYPE:types.ACCUM,types.PARAM:None},
    SOLO: {types.TYPE:types.ACCUM,types.PARAM:None},
    AST: {types.TYPE:types.ACCUM,types.PARAM:None},
    SACK: {types.TYPE:types.ACCUM,types.PARAM:None},
    FF: {types.TYPE:types.ACCUM,types.PARAM:None},
    FR: {types.TYPE:types.ACCUM,types.PARAM:None},
    FYDS: {types.TYPE:types.ACCUM,types.PARAM:None},
    INT: {types.TYPE:types.ACCUM,types.PARAM:None},
    IYDS: {types.TYPE:types.ACCUM,types.PARAM:None},
    TD: {types.TYPE:types.ACCUM,types.PARAM:None},
    LNG: {types.TYPE:types.MAX,types.PARAM:None},
    PD: {types.TYPE:types.ACCUM,types.PARAM:None},
    STF: {types.TYPE:types.ACCUM,types.PARAM:None},
    STFYDS: {types.TYPE:types.ACCUM,types.PARAM:None},
    KB: {types.TYPE:types.ACCUM,types.PARAM:None},
}

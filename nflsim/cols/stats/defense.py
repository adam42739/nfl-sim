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
AVG = "AVG"
TD = "TD"
LNG = "LNG"
PD = "PD"
STF = "STF"
STFYDS = "STFYDS"
KB = "KB"

DICT = {
    GP: types.ACCUM,
    TOT: types.ACCUM,
    SOLO: types.ACCUM,
    AST: types.ACCUM,
    SACK: types.ACCUM,
    FF: types.ACCUM,
    FR: types.ACCUM,
    FYDS: types.ACCUM,
    INT: types.ACCUM,
    IYDS: types.ACCUM,
    AVG: types.AVG,
    TD: types.ACCUM,
    LNG: types.MAX,
    PD: types.ACCUM,
    STF: types.ACCUM,
    STFYDS: types.ACCUM,
    KB: types.ACCUM,
}

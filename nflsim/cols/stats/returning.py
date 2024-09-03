from nflsim.cols.stats import types


GP = "GP"
PATT = "PATT"
PYDS = "PYDS"
PTD = "PTD"
PFC = "PFC"
PLNG = "PLNG"
KATT = "KATT"
KYDS = "KYDS"
KTD = "KTD"
KRFC = "KRFC"
KLNG = "KLNG"

DICT = {
    GP: {types.TYPE:types.ACCUM,types.PARAM:None},
    PATT: {types.TYPE:types.ACCUM,types.PARAM:None},
    PYDS: {types.TYPE:types.ACCUM,types.PARAM:None},
    PTD: {types.TYPE:types.ACCUM,types.PARAM:None},
    PFC: {types.TYPE:types.ACCUM,types.PARAM:None},
    PLNG: {types.TYPE:types.MAX,types.PARAM:None},
    KATT: {types.TYPE:types.ACCUM,types.PARAM:None},
    KYDS: {types.TYPE:types.ACCUM,types.PARAM:None},
    KTD: {types.TYPE:types.ACCUM,types.PARAM:None},
    KRFC: {types.TYPE:types.ACCUM,types.PARAM:None},
    KLNG: {types.TYPE:types.MAX,types.PARAM:None},
}

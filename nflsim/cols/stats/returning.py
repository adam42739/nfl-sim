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
    GP: types.ACCUM,
    PATT: types.ACCUM,
    PYDS: types.ACCUM,
    PTD: types.ACCUM,
    PFC: types.ACCUM,
    PLNG: types.MAX,
    KATT: types.ACCUM,
    KYDS: types.ACCUM,
    KTD: types.ACCUM,
    KRFC: types.ACCUM,
    KLNG: types.MAX,
}

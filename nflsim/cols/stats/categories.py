from nflsim.cols.stats import defense
from nflsim.cols.stats import kicking
from nflsim.cols.stats import passing
from nflsim.cols.stats import punting
from nflsim.cols.stats import receiving
from nflsim.cols.stats import returning
from nflsim.cols.stats import rushing
from nflsim.cols.stats import scoring


PASSING = "Passing"
RUSHING = "Rushing"
RECEIVING = "Receiving"
DEFENSE = "Defense"
SCORING = "Scoring"
RETURNING = "Returning"
KICKING = "Kicking"
PUNTING = "Punting"

LIST = [
    PASSING,
    RUSHING,
    RECEIVING,
    DEFENSE,
    SCORING,
    RETURNING,
    KICKING,
    PUNTING,
]

STAT_DICTS = {
    PASSING: passing.DICT,
    RUSHING: rushing.DICT,
    RECEIVING: receiving.DICT,
    DEFENSE: defense.DICT,
    SCORING: scoring.DICT,
    RETURNING: returning.DICT,
    KICKING: kicking.DICT,
    PUNTING: punting.DICT,
}

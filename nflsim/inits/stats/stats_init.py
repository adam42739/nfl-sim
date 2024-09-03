from nflsim.inits.stats import stats
from nflsim.inits.stats import defense
from nflsim.inits.stats import kicking
from nflsim.inits.stats import passing
from nflsim.inits.stats import punting
from nflsim.inits.stats import receiving
from nflsim.inits.stats import returning
from nflsim.inits.stats import rushing
from nflsim.inits.stats import scoring
from nflsim import cols
import pandas

DICT = {
    cols.stats.categories.LIST[0]: passing.FRAME,
    cols.stats.categories.LIST[1]: rushing.FRAME,
    cols.stats.categories.LIST[2]: receiving.FRAME,
    cols.stats.categories.LIST[3]: defense.FRAME,
    cols.stats.categories.LIST[4]: scoring.FRAME,
    cols.stats.categories.LIST[5]: returning.FRAME,
    cols.stats.categories.LIST[6]: kicking.FRAME,
    cols.stats.categories.LIST[7]: punting.FRAME,
}


def init():
    frame = stats.FRAME.copy()
    for i in range(0, len(cols.stats.categories.LIST)):
        frame[cols.stats.categories.LIST[i]] = pandas.DataFrame(
            DICT[cols.stats.categories.LIST[i]]
        )
    return frame

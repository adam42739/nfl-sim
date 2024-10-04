from .field_goal import Model
from .field_goal import MADE, MISSED, BLOCKED, RECOVERED, YARDS_RETURNED
import random


class PRNG(Model):
    """
    PRNG
    ----

    Field goal model that determines outcomes randomly according to a set of given weights.
    """
    def __init__(self):
        pass

    def build(
        self,
        w_made: float,
        w_miss: float,
        w_block: float,
        w_recover: float,
        min_yrec: int,
        max_yrec: int,
    ):
        """
        Build the PRNG field goal model.

        Parameters
        ----------

        w_made : float
            Weight assigned to a field goal make.

        w_miss : float
            Weight assigned to a field goal miss.

        w_block : float
            Weight assigned to a field goal block.

        w_recover : float
            Weight assigned to a field goal recovery.

        min_yrec : int
            Minimum yards returned possible.

        max_yrec : int
            Maximum yards returned possible.

        Note
        ----

        `w_make`, `w_miss`, `w_block`, `w_recover` are all mutually exclusive (i.e.
        `w_any_missed_fg = w_miss + w_block + w_recover`)
        """
        total = w_made + w_miss + w_block + w_recover
        self.p_made = w_made / total
        self.p_miss = w_miss / total
        self.p_block = w_block / total
        self.p_recover = w_recover / total
        self.min_yrec = min_yrec
        self.max_yrec = max_yrec
        self.cump_made = self.p_made
        self.cump_miss = self.cump_made + self.p_miss
        self.cump_block = self.cump_miss + self.p_block
        self.cump_recover = self.cump_block + self.p_recover

    def sample(self) -> dict:
        rng = random.random()
        out = {
            MADE: False,
            MISSED: False,
            BLOCKED: False,
            RECOVERED: False,
            YARDS_RETURNED: 0,
        }
        if rng < self.cump_made:
            out[MADE] = True
        elif rng < self.cump_miss:
            out[MISSED] = True
        elif rng < self.cump_block:
            out[BLOCKED] = True
        elif rng < self.cump_recover:
            out[RECOVERED] = True
            out[YARDS_RETURNED] = random.randint(self.min_yrec, self.max_yrec)
        return out

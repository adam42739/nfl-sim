from nflsim import cols
from nflsim import inits

WEEK1_REST = 7

GAME_TYPE_REG = "REG"
GAME_TYPE_WC = "WC"
GAME_TYPE_DIV = "DIV"
GAME_TYPE_CON = "CON"
GAME_TYPE_SB = "SB"

LOCATION_HOME = "Home"
LOCATION_NEUTRAL = "Neutral"


GAME_QUARTER_SECONDS = 60 * 15

GAME_END_QUARTER = 0
GAME_END = 1


class GameSimTime:
    def __init__(self):
        self.Q = 1
        self.seconds = GAME_QUARTER_SECONDS

    def subtract(self, sec):
        self.seconds -= sec
        if self.seconds < 0:
            if self.Q == 4:
                return GAME_END
            else:
                return GAME_END_QUARTER


class GameSim:
    def __init__(self):
        return

    def from_row(self, row, league):
        self.gsis = row[cols.schedules.GSIS]
        self.season = row[cols.schedules.SEASON]
        self.week = row[cols.schedules.WEEK]
        self.home_team = league.teambase[cols.teams.ABBR][row[cols.schedules.HOME_TEAM]]
        self.away_team = league.teambase[cols.teams.ABBR][row[cols.schedules.AWAY_TEAM]]
        self.home_rest = row[cols.schedules.HOME_REST]
        self.away_rest = row[cols.schedules.AWAY_REST]
        if row[cols.schedules.WEEK] == 1:
            self.home_rest = WEEK1_REST
            self.away_rest = WEEK1_REST
        self.gametype = row[cols.schedules.GAME_TYPE]
        self.weekday = row[cols.schedules.WEEKDAY]
        self.gametime = row[cols.schedules.GAMETIME]
        self.location = row[cols.schedules.LOCATION]

    def sim(self):
        self.stats = inits.stats.stats_init.init()
        id = list(self.home_team.players.keys())[0]
        self.stats[cols.stats.categories.PASSING].loc[
            id
        ] = inits.stats.passing.ROW.copy()
        self.stats[cols.stats.categories.PASSING].at[id, cols.stats.passing.GP] = 5
        print(self.stats[cols.stats.categories.PASSING].head())
        self.time = GameSimTime()
        # sim game

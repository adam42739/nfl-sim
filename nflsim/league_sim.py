import nflsim.nfl_data as nfl_data
import nflsim.playerbase as playerbase
import nflsim.teambase as teambase


def update_teambase_rosters(teambase, rosters, season, week):
    return teambase


class LeagueSim:
    def __init__(self):
        years = [year for year in range(nfl_data.START_YEAR, nfl_data.THIS_YEAR + 1)]
        self.players = playerbase.load_playersbase()
        self.rosters = nfl_data.get_rosters(years)
        self.schedules = nfl_data.get_schedules(years)
        self.cur_season = nfl_data.START_YEAR
        self.cur_week = 1
        self.cur_sb_week = self._season_sb_week()
        self.fin_season = self._data_final_season()
        self.teambase = teambase.get_teambase()
        self.teambase = update_teambase_rosters(
            self.teambase, self.rosters, self.cur_season, self.cur_week
        )

    def _data_final_season(self):
        return self.schedules["season"].max()

    def _season_sb_week(self):
        return self.schedules[self.schedules["season"] == self.cur_season]["week"].max()

    def _load_schedules(self):
        years = [year for year in range(nfl_data.START_YEAR, nfl_data.THIS_YEAR + 1)]
        self.schedules = nfl_data.get_schedules(years)

    def sim_week(self):
        week_mask = (self.schedules["season"] == self.cur_season) & (
            self.schedules["week"] == self.cur_week
        )
        games = self.schedules[week_mask]
        games.apply(self._sim_game, axis=1)
        if self.cur_week == self.cur_sb_week:
            if self.cur_season == self.fin_season:
                return False
            else:
                self._advance_season()
        else:
            self._advance_week()
        return True

    def _advance_week(self):
        self.cur_week += 1

    def _sim_game(self, game):
        # sim game
        return

    def _advance_season(self):
        self.cur_season += 1
        self.cur_week = 1
        self.cur_sb_week = self.season_sb_week()

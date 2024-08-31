import data


class LeagueSim:
    def __init__(self):
        self._load_schedules()
        self.cur_season = data.START_YEAR
        self.cur_week = 1
        self.cur_sb_week = self._season_sb_week()
        self.fin_season = self._data_final_season()

    def _data_final_season(self):
        return self.schedules["season"].max()

    def _season_sb_week(self):
        return self.schedules[self.schedules["season"] == self.cur_season]["week"].max()

    def _load_schedules(self):
        years = [year for year in range(data.START_YEAR, data.THIS_YEAR + 1)]
        self.schedules = data.get_schedules(years)

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
            self.cur_week += 1
        return True

    def _sim_game(self, game):
        # sim game
        return

    def _advance_season(self):
        self.cur_season += 1
        self.cur_week = 1
        self.cur_sb_week = self.season_sb_week()

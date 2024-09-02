import nflsim.nfl_data as nfl_data
import nflsim.playerbase as playerbase
import nflsim.teambase as teambase
from nflsim.nfl_data_cols import *


def _player_add_team(row, team, playerbase):
    id = row[COLS.ROSTERS.PLAYER_ID]
    if not isinstance(id, float):
        team.players[id] = playerbase[id]


def update_teambase_rosters(teambase, rosters, playerbase, season, week):
    mask = (rosters[COLS.ROSTERS.SEASON] == season) & (
        rosters[COLS.ROSTERS.WEEK] == week
    )
    rosters_week = rosters[mask]
    for abbr in teambase[COLS.TEAMS.ABBR]:
        teambase[COLS.TEAMS.ABBR][abbr].players = {}
        mask = rosters_week[COLS.ROSTERS.TEAM] == abbr
        team_roster = rosters_week[mask]
        team_roster.apply(
            _player_add_team, axis=1, args=(teambase[COLS.TEAMS.ABBR][abbr], playerbase)
        )
    return teambase


class LeagueSim:
    def __init__(self):
        years = [year for year in range(nfl_data.START_YEAR, nfl_data.THIS_YEAR + 1)]
        self.rosters = nfl_data.get_rosters(years)
        self.drafts = nfl_data.get_drafts(years)
        self.players = playerbase.load_playersbase(self.rosters, self.drafts)
        self.schedules = nfl_data.get_schedules(years)
        self.cur_season = nfl_data.START_YEAR
        self.cur_week = 1
        self.cur_sb_week = self._season_sb_week()
        self.fin_season = self._data_final_season()
        self.teambase = teambase.get_teambase()
        self.teambase = update_teambase_rosters(
            self.teambase, self.rosters, self.players, self.cur_season, self.cur_week
        )

    def _data_final_season(self):
        return self.schedules[COLS.SCHEDULES.SEASON].max()

    def _season_sb_week(self):
        return self.schedules[self.schedules[COLS.SCHEDULES.SEASON] == self.cur_season][
            COLS.SCHEDULES.WEEK
        ].max()

    def _load_schedules(self):
        years = [year for year in range(nfl_data.START_YEAR, nfl_data.THIS_YEAR + 1)]
        self.schedules = nfl_data.get_schedules(years)

    def sim_week(self):
        week_mask = (self.schedules[COLS.SCHEDULES.SEASON] == self.cur_season) & (
            self.schedules[COLS.SCHEDULES.WEEK] == self.cur_week
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

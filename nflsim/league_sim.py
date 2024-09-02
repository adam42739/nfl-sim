import nflsim.nfl_data as nfl_data
import nflsim.playerbase as playerbase
import nflsim.teambase as teambase
from nflsim.nfl_data_cols import *
import os
import json


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


CONFS_PATH = "/confs.json"


def _get_confs():
    path = os.path.dirname(__file__) + CONFS_PATH
    confs_json = None
    with open(path, "r") as file:
        confs_json = json.load(file)
    return confs_json


class DivisionSim:
    def __init__(self):
        return

    def from_teambase(self, conf, div, teambase):
        self.conf = conf
        self.div = div
        self.teams = {COLS.TEAMS.ABBR: {}, COLS.TEAMS.ID: {}}
        for abbr in teambase[COLS.TEAMS.ABBR]:
            team = teambase[COLS.TEAMS.ABBR][abbr]
            if team.conf == conf and team.division == div:
                self.teams[COLS.TEAMS.ABBR][abbr] = team
        for id in teambase[COLS.TEAMS.ID]:
            team = teambase[COLS.TEAMS.ID][id]
            if team.conf == conf and team.division == div:
                self.teams[COLS.TEAMS.ID][id] = team


class ConfSim:
    def __init__(self):
        return

    def from_teambase(self, abbr, conf, teambase):
        self.abbr = abbr
        self.name = conf["name"]
        self.divs = {}
        for div in conf["divs"]:
            self.divs[div] = DivisionSim()
            self.divs[div].from_teambase(abbr, div, teambase)


class LeagueSim:
    def __init__(self, season, week):
        self.cur_season = season
        self.cur_week = week
        self._load_assets()
        self.cur_sb_week = self._season_sb_week()
        self.fin_season = self._data_final_season()
        self._load_confs()

    def _load_confs(self):
        confs_json = _get_confs()
        self.confs = {"AFC": ConfSim(), "NFL": ConfSim()}
        self.confs["AFC"].from_teambase("AFC", confs_json["AFC"], self.teambase)
        self.confs["NFC"].from_teambase("NFC", confs_json["NFC"], self.teambase)

    def _load_assets(self):
        years = [year for year in range(nfl_data.START_YEAR, nfl_data.THIS_YEAR + 1)]
        self.rosters = nfl_data.get_rosters(years)
        self.drafts = nfl_data.get_drafts(years)
        self.players = playerbase.load_playersbase(self.rosters, self.drafts)
        self.schedules = nfl_data.get_schedules(years)
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

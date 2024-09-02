import nflsim.nfl_data as nfl_data
import nflsim.playerbase as playerbase
import nflsim.teambase as teambase
from nflsim.nfl_data_cols import *
import os
import json
import nflsim.game_sim as game_sim
import pandas
from nflsim.league_sim_inits import *


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

    def from_teambase(self, conf, div, teambase, league):
        self.league = league
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

    def get_standings(self):
        mask = self.league.standings.index.isin(self.teams[COLS.TEAMS.ID].keys())
        return self.league.standings[mask]


class ConfSim:
    def __init__(self):
        return

    def from_teambase(self, abbr, conf, teambase, league):
        self.league = league
        self.abbr = abbr
        self.name = conf["name"]
        self.divs = {}
        for div in conf["divs"]:
            self.divs[div] = DivisionSim()
            self.divs[div].from_teambase(abbr, div, teambase, league)
        self._load_team_ids()

    def _load_team_ids(self):
        self.teams = []
        for div in self.divs:
            self.teams += self.divs[div].teams[COLS.TEAMS.ID].keys()

    def get_standings(self):
        mask = self.league.standings.index.isin(self.teams)
        return self.league.standings[mask]


class LeagueSim:
    def __init__(self, season, week):
        self.cur_season = season
        self.cur_week = week
        self._load_assets()
        self.cur_sb_week = self._season_sb_week()
        self.fin_season = self._data_final_season()
        self._load_confs()
        self._load_standings()
        self._load_stats()

    def _load_stats(self):
        self.stats = INITS.init_stats()

    def _load_standings(self):
        self._reset_standings()

    def _load_confs(self):
        confs_json = _get_confs()
        self.confs = {"AFC": ConfSim(), "NFC": ConfSim()}
        self.confs["AFC"].from_teambase("AFC", confs_json["AFC"], self.teambase, self)
        self.confs["NFC"].from_teambase("NFC", confs_json["NFC"], self.teambase, self)

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

    def _standings_compute_pct(self):
        total_games = (
            self.standings[COLS.STANDINGS.W]
            + self.standings[COLS.STANDINGS.L]
            + self.standings[COLS.STANDINGS.T]
        )
        total_games = total_games * (total_games != 0) + 1 * (total_games == 0)
        pct = self.standings[COLS.STANDINGS.W] / total_games
        self.standings[COLS.STANDINGS.PCT] = pct

    def _game_update_standings(self, game):
        self.standings.at[game.home_team.id, COLS.STANDINGS.PF] += game.home_score
        self.standings.at[game.home_team.id, COLS.STANDINGS.PA] += game.away_score
        self.standings.at[game.away_team.id, COLS.STANDINGS.PF] += game.away_score
        self.standings.at[game.away_team.id, COLS.STANDINGS.PA] += game.home_score
        conf = game.home_team.conf == game.away_team.conf
        div = game.home_team.division == game.away_team.division
        if game.home_score > game.away_score:
            self.standings.at[game.home_team.id, COLS.STANDINGS.W] += 1
            self.standings.at[game.away_team.id, COLS.STANDINGS.L] += 1
            self.standings.at[game.home_team.id, COLS.STANDINGS.HOMEW] += 1
            self.standings.at[game.away_team.id, COLS.STANDINGS.AWAYL] += 1
            if conf:
                self.standings.at[game.home_team.id, COLS.STANDINGS.CONFW] += 1
                self.standings.at[game.away_team.id, COLS.STANDINGS.CONFL] += 1
                if div:
                    self.standings.at[game.home_team.id, COLS.STANDINGS.DIVW] += 1
                    self.standings.at[game.away_team.id, COLS.STANDINGS.DIVL] += 1
            else:
                self.standings.at[game.home_team.id, COLS.STANDINGS.NON_CONFW] += 1
                self.standings.at[game.away_team.id, COLS.STANDINGS.NON_CONFL] += 1
        elif game.home_score < game.away_score:
            self.standings.at[game.home_team.id, COLS.STANDINGS.L] += 1
            self.standings.at[game.away_team.id, COLS.STANDINGS.W] += 1
            self.standings.at[game.home_team.id, COLS.STANDINGS.HOMEL] += 1
            self.standings.at[game.away_team.id, COLS.STANDINGS.AWAYW] += 1
            if conf:
                self.standings.at[game.home_team.id, COLS.STANDINGS.CONFL] += 1
                self.standings.at[game.away_team.id, COLS.STANDINGS.CONFW] += 1
                if div:
                    self.standings.at[game.home_team.id, COLS.STANDINGS.DIVL] += 1
                    self.standings.at[game.away_team.id, COLS.STANDINGS.DIVW] += 1
            else:
                self.standings.at[game.home_team.id, COLS.STANDINGS.NON_CONFL] += 1
                self.standings.at[game.away_team.id, COLS.STANDINGS.NON_CONFW] += 1
        else:
            self.standings.at[game.home_team.id, COLS.STANDINGS.T] += 1
            self.standings.at[game.away_team.id, COLS.STANDINGS.T] += 1
            self.standings.at[game.home_team.id, COLS.STANDINGS.HOMET] += 1
            self.standings.at[game.away_team.id, COLS.STANDINGS.AWAYT] += 1
            if conf:
                self.standings.at[game.home_team.id, COLS.STANDINGS.CONFT] += 1
                self.standings.at[game.away_team.id, COLS.STANDINGS.CONFT] += 1
                if div:
                    self.standings.at[game.home_team.id, COLS.STANDINGS.DIVT] += 1
                    self.standings.at[game.away_team.id, COLS.STANDINGS.DIVT] += 1
            else:
                self.standings.at[game.home_team.id, COLS.STANDINGS.NON_CONFT] += 1
                self.standings.at[game.away_team.id, COLS.STANDINGS.NON_CONFT] += 1
        self._standings_compute_pct()

    def _game_add_stats(self, game):
        # for i in range(0, len(COLS.STAT_CATEGORIES.LIST)):
        #     stats[COLS.STAT_CATEGORIES.LIST[i]] = pandas.DataFrame(
        #         INITS.STAT_TYPES.LIST[i]
        #     )
        # TODO
        return

    def _game_finish(self, game):
        self._game_add_stats(game)
        self._game_update_standings(game)

    def _sim_game(self, row):
        game = game_sim.GameSim()
        game.from_row(row, self)
        game.sim()
        self._game_finish(game)

    def _advance_season(self):
        self.cur_season += 1
        self.cur_week = 1
        self.cur_sb_week = self.season_sb_week()
        self._reset_standings()

    def _reset_standings(self):
        self.standings = pandas.DataFrame(INITS.STANDINGS)
        for id in self.teambase[COLS.TEAMS.ID]:
            team = self.teambase[COLS.TEAMS.ID][id]
            series = pandas.Series(INITS.STANDINGS_ROW)
            series["NFL Team"] = team.name_at_year(self.cur_season)
            self.standings.loc[id] = series

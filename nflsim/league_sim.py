from nflsim import nfl_data
from nflsim import playerbase
from nflsim import teambase
from nflsim import cols
import os
import json
from nflsim import game_sim
import pandas
from nflsim import inits
import numpy


def _player_add_team(row, team, playerbase):
    id = row[cols.rosters.PLAYER_ID]
    if not isinstance(id, float):
        team.players[id] = playerbase[id]


def update_teambase_rosters(teambase, rosters, playerbase, season, week):
    mask = (rosters[cols.rosters.SEASON] == season) & (
        rosters[cols.rosters.WEEK] == week
    )
    rosters_week = rosters[mask]
    for abbr in teambase[cols.teams.ABBR]:
        teambase[cols.teams.ABBR][abbr].players = {}
        mask = rosters_week[cols.rosters.TEAM] == abbr
        team_roster = rosters_week[mask]
        team_roster.apply(
            _player_add_team, axis=1, args=(teambase[cols.teams.ABBR][abbr], playerbase)
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
        self.teams = {cols.teams.ABBR: {}, cols.teams.ID: {}}
        for abbr in teambase[cols.teams.ABBR]:
            team = teambase[cols.teams.ABBR][abbr]
            if team.conf == conf and team.division == div:
                self.teams[cols.teams.ABBR][abbr] = team
        for id in teambase[cols.teams.ID]:
            team = teambase[cols.teams.ID][id]
            if team.conf == conf and team.division == div:
                self.teams[cols.teams.ID][id] = team

    def get_standings(self):
        mask = self.league.standings.index.isin(self.teams[cols.teams.ID].keys())
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
            self.teams += self.divs[div].teams[cols.teams.ID].keys()

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
        self.stats = inits.stats.stats_init.init()

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
        return self.schedules[cols.schedules.SEASON].max()

    def _season_sb_week(self):
        return self.schedules[self.schedules[cols.schedules.SEASON] == self.cur_season][
            cols.schedules.WEEK
        ].max()

    def _load_schedules(self):
        years = [year for year in range(nfl_data.START_YEAR, nfl_data.THIS_YEAR + 1)]
        self.schedules = nfl_data.get_schedules(years)

    def sim_week(self):
        week_mask = (self.schedules[cols.schedules.SEASON] == self.cur_season) & (
            self.schedules[cols.schedules.WEEK] == self.cur_week
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
            self.standings[cols.standings.W]
            + self.standings[cols.standings.L]
            + self.standings[cols.standings.T]
        )
        total_games = total_games * (total_games != 0) + 1 * (total_games == 0)
        pct = self.standings[cols.standings.W] / total_games
        self.standings[cols.standings.PCT] = pct

    def _game_update_standings(self, game):
        self.standings.at[game.home_team.id, cols.standings.PF] += game.home_score
        self.standings.at[game.home_team.id, cols.standings.PA] += game.away_score
        self.standings.at[game.away_team.id, cols.standings.PF] += game.away_score
        self.standings.at[game.away_team.id, cols.standings.PA] += game.home_score
        conf = game.home_team.conf == game.away_team.conf
        div = game.home_team.division == game.away_team.division
        if game.home_score > game.away_score:
            self.standings.at[game.home_team.id, cols.standings.W] += 1
            self.standings.at[game.away_team.id, cols.standings.L] += 1
            self.standings.at[game.home_team.id, cols.standings.HOMEW] += 1
            self.standings.at[game.away_team.id, cols.standings.AWAYL] += 1
            if conf:
                self.standings.at[game.home_team.id, cols.standings.CONFW] += 1
                self.standings.at[game.away_team.id, cols.standings.CONFL] += 1
                if div:
                    self.standings.at[game.home_team.id, cols.standings.DIVW] += 1
                    self.standings.at[game.away_team.id, cols.standings.DIVL] += 1
            else:
                self.standings.at[game.home_team.id, cols.standings.NON_CONFW] += 1
                self.standings.at[game.away_team.id, cols.standings.NON_CONFL] += 1
        elif game.home_score < game.away_score:
            self.standings.at[game.home_team.id, cols.standings.L] += 1
            self.standings.at[game.away_team.id, cols.standings.W] += 1
            self.standings.at[game.home_team.id, cols.standings.HOMEL] += 1
            self.standings.at[game.away_team.id, cols.standings.AWAYW] += 1
            if conf:
                self.standings.at[game.home_team.id, cols.standings.CONFL] += 1
                self.standings.at[game.away_team.id, cols.standings.CONFW] += 1
                if div:
                    self.standings.at[game.home_team.id, cols.standings.DIVL] += 1
                    self.standings.at[game.away_team.id, cols.standings.DIVW] += 1
            else:
                self.standings.at[game.home_team.id, cols.standings.NON_CONFL] += 1
                self.standings.at[game.away_team.id, cols.standings.NON_CONFW] += 1
        else:
            self.standings.at[game.home_team.id, cols.standings.T] += 1
            self.standings.at[game.away_team.id, cols.standings.T] += 1
            self.standings.at[game.home_team.id, cols.standings.HOMET] += 1
            self.standings.at[game.away_team.id, cols.standings.AWAYT] += 1
            if conf:
                self.standings.at[game.home_team.id, cols.standings.CONFT] += 1
                self.standings.at[game.away_team.id, cols.standings.CONFT] += 1
                if div:
                    self.standings.at[game.home_team.id, cols.standings.DIVT] += 1
                    self.standings.at[game.away_team.id, cols.standings.DIVT] += 1
            else:
                self.standings.at[game.home_team.id, cols.standings.NON_CONFT] += 1
                self.standings.at[game.away_team.id, cols.standings.NON_CONFT] += 1
        self._standings_compute_pct()

    def _game_stats_merged_df(self, game, cat):
        lstat = self.stats[cat]
        gstat = game.stats[cat]
        lstat_inds = lstat.index.values.tolist()
        gstat_inds = gstat.index.values.tolist()
        for g_ind in gstat_inds:
            if g_ind not in lstat_inds:
                lstat.loc[g_ind] = inits.stats.stats_init.ROW_DICT[cat]
        return lstat.merge(gstat, left_index=True, right_index=True)

    def _game_add_stats(self, game):
        for cat in cols.stats.categories.LIST:
            df = self._game_stats_merged_df(game, cat)
            stat_dict = cols.stats.categories.STAT_DICTS[cat]
            for stat in stat_dict:
                if stat_dict[stat][cols.stats.types.TYPE] == cols.stats.types.ACCUM:
                    df[stat + "_x"] += df[stat + "_y"]
                elif stat_dict[stat][cols.stats.types.TYPE] == cols.stats.types.MAX:
                    df[stat + "_x"] = numpy.maximum(df[stat + "_x"], df[stat + "_y"])
            for stat in stat_dict:
                if stat_dict[stat][cols.stats.types.TYPE] == cols.stats.types.AVG:
                    X_params_list = [
                        x + "_x" for x in stat_dict[stat][cols.stats.types.PARAM]["X"]
                    ]
                    X = df[X_params_list].sum(axis=1)
                    Y_params_list = [
                        x + "_x" for x in stat_dict[stat][cols.stats.types.PARAM]["Y"]
                    ]
                    Y = df[Y_params_list].sum(axis=1)
                    mask = Y == 0
                    df[stat_dict[stat][cols.stats.types.PARAM]["Y"][0] + "_x"][mask] = 1
                    Y = df[Y_params_list].sum(axis=1)
                    df[stat + "_x"] = X / Y
                    df[stat_dict[stat][cols.stats.types.PARAM]["Y"][0] + "_x"][mask] = 0
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
        self.standings = pandas.DataFrame(inits.standings.FRAME)
        for id in self.teambase[cols.teams.ID]:
            team = self.teambase[cols.teams.ID][id]
            series = pandas.Series(inits.standings.ROW)
            series["NFL Team"] = team.name_at_year(self.cur_season)
            self.standings.loc[id] = series

import nflsim.nfl_data as nfl_data
import os
import json
from nflsim.nfl_data_cols import *


def _get_abbrs():
    PATH = os.path.dirname(__file__) + "/abbrs.json"
    with open(PATH, "r") as file:
        abbrs = json.load(file)
    return abbrs


def get_teambase():
    COLUMNS_DEL = [COLS.TEAMS.NAME, COLS.TEAMS.CONF, COLS.TEAMS.DIVISION]
    teams = nfl_data.get_teams()
    abbr_match = (
        teams[[COLS.TEAMS.ABBR, COLS.TEAMS.ID]].set_index(COLS.TEAMS.ABBR).to_dict()
    )
    teams["team_obj"] = teams.apply(_load_team, axis=1)
    teams = teams.drop(COLUMNS_DEL, axis=1)
    teams_dict = teams.to_dict()
    teams_dict = nfl_data.to_indexed_dict(teams_dict, "team_obj")
    abbrs = _get_abbrs()
    for abbrs_key in abbrs:
        teams = []
        years = []
        for x in abbrs[abbrs_key]:
            if x in teams_dict[COLS.TEAMS.ABBR]:
                teams.append(teams_dict[COLS.TEAMS.ABBR][x])
                years.append(abbrs[abbrs_key][x])
        new_team = _agg_teams(teams, years)
        for abbr in abbrs[abbrs_key]:
            teams_dict[COLS.TEAMS.ABBR][abbr] = new_team
            if abbr in abbr_match[COLS.TEAMS.ID]:
                teams_dict[COLS.TEAMS.ID][abbr_match[COLS.TEAMS.ID][abbr]] = new_team
    return teams_dict


def _agg_teams(teams, years):
    team = Team()
    team.name = [x.name for x in teams]
    team.year = years
    team.conf = teams[0].conf
    team.division = teams[0].division
    team.players = {}
    return team


def _load_team(row):
    team = Team()
    team.from_row(row)
    return team


class Team:
    def __init__(self):
        return

    def from_row(self, row):
        self.name = row[COLS.TEAMS.NAME]
        self.year = [nfl_data.START_YEAR]
        self.conf = row[COLS.TEAMS.CONF]
        self.division = row[COLS.TEAMS.DIVISION]
        self.players = {}

    def name_at_year(self, year):
        for i in range(0, len(self.year)):
            if i == len(self.year) - 1:
                return self.name[i]
            elif year >= self.year[i] and year < self.year[i + 1]:
                return self.name[i]

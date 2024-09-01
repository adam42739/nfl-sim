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
        for x in abbrs[abbrs_key]:
            if x in teams_dict[COLS.TEAMS.ABBR]:
                teams.append(teams_dict[COLS.TEAMS.ABBR][x])
        new_team = _agg_teams(teams)
        for abbr in abbrs[abbrs_key]:
            teams_dict[COLS.TEAMS.ABBR][abbr] = new_team
            if abbr in abbr_match[COLS.TEAMS.ID]:
                teams_dict[COLS.TEAMS.ID][abbr_match[COLS.TEAMS.ID][abbr]] = new_team
    return teams_dict


def _agg_teams(teams):
    team = Team()
    team.team_name = [x.team_name for x in teams]
    team.team_conf = teams[0].team_conf
    team.team_division = teams[0].team_division
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
        self.team_name = row[COLS.TEAMS.NAME]
        self.team_conf = row[COLS.TEAMS.CONF]
        self.team_division = row[COLS.TEAMS.DIVISION]
        self.players = {}

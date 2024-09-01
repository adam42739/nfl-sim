import nflsim.nfl_data as nfl_data
import os
import json


def _get_abbrs():
    PATH = os.path.dirname(__file__) + "/abbrs.json"
    with open(PATH, "r") as file:
        abbrs = json.load(file)
    return abbrs


def get_teambase():
    COLUMNS_DEL = ["team_name", "team_conf", "team_division"]
    teams = nfl_data.get_teams()
    abbr_match = teams[["team_abbr", "team_id"]].set_index("team_abbr").to_dict()
    teams["team_obj"] = teams.apply(_load_team, axis=1)
    teams = teams.drop(COLUMNS_DEL, axis=1)
    teams_dict = teams.to_dict()
    teams_dict = nfl_data.to_indexed_dict(teams_dict, "team_obj")
    abbrs = _get_abbrs()
    for abbrs_key in abbrs:
        teams = [teams_dict["team_abbr"][x] for x in abbrs[abbrs_key]]
        new_team = _agg_teams(teams)
        for abbr in abbrs[abbrs_key]:
            teams_dict["team_abbr"][abbr] = new_team
            teams_dict["team_id"][abbr_match["team_id"][abbr]] = new_team
    return teams_dict


def _agg_teams(teams):
    team = Team()
    team.team_name = [x.team_name for x in teams]
    team.team_conf = teams[0].team_conf
    team.team_division = teams[0].team_division
    return team


def _load_team(row):
    team = Team()
    team.from_row(row)
    return team


class Team:
    def __init__(self):
        return

    def from_row(self, row):
        self.team_name = row["team_name"]
        self.team_conf = row["team_conf"]
        self.team_division = row["team_division"]

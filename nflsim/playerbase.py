import nflsim.nfl_data as nfl_data
from nflsim.nfl_data_cols import *


def load_playersbase(rosters, drafts):
    COLUMNS_DEL = [
        COLS.ROSTERS.PLAYER_NAME,
        COLS.ROSTERS.FIRST_NAME,
        COLS.ROSTERS.LAST_NAME,
        COLS.ROSTERS.POSITION,
        COLS.ROSTERS.BIRTH_DATE,
        COLS.DRAFTS.SEASON,
        COLS.DRAFTS.ROUND,
        COLS.DRAFTS.PICK,
        COLS.ROSTERS.HEIGHT,
        COLS.ROSTERS.WEIGHT,
    ]
    player_df = nfl_data.get_players(rosters, drafts)
    player_df["player_obj"] = player_df.apply(_player_from_row, axis=1)
    player_df = player_df.drop(COLUMNS_DEL, axis=1)
    player_dict = player_df.to_dict()
    player_dict = nfl_data.to_indexed_dict(player_dict, "player_obj")
    return player_dict


def _player_from_row(row):
    plyr = Player()
    plyr.from_row(row)
    return plyr


class Player:
    def __init__(self):
        return

    def from_row(self, row):
        self.name = row[COLS.ROSTERS.PLAYER_NAME]
        self.first_name = row[COLS.ROSTERS.FIRST_NAME]
        self.last_name = row[COLS.ROSTERS.LAST_NAME]
        self.position = row[COLS.ROSTERS.POSITION]
        self.birthdate = row[COLS.ROSTERS.BIRTH_DATE]
        self.draft_year = row[COLS.DRAFTS.SEASON]
        self.draft_round = row[COLS.DRAFTS.ROUND]
        self.draft_pick = row[COLS.DRAFTS.PICK]
        self.height = row[COLS.ROSTERS.HEIGHT]
        self.weight = row[COLS.ROSTERS.WEIGHT]

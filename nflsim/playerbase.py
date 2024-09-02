import nflsim.nfl_data as nfl_data
from nflsim.nfl_data_cols import *
import time
import os
import csv


MISC_CACHE_PLAYERBASE = "/misc_cache/playerbase.csv"


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
    ti = time.time()
    player_df = nfl_data.get_players(rosters, drafts)
    tf = time.time()
    print("nfl_data.get_players(): ", tf - ti)

    ti = time.time()
    player_df = player_df.drop_duplicates()
    tf = time.time()
    print("drop_dups(): ", tf - ti)

    ti = time.time()
    cache_path = os.path.dirname(__file__) + MISC_CACHE_PLAYERBASE
    COLUMNS_ORDER = [
        COLS.ROSTERS.PLAYER_ID,
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
    player_df = player_df.reindex(COLUMNS_ORDER, axis="columns")
    player_df.to_csv(cache_path)
    tf = time.time()
    print("to_dict(): ", tf - ti)

    player_dict = {}
    ti = time.time()
    with open(cache_path, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            player = Player()
            player.from_row(
                line[2],
                line[3],
                line[4],
                line[5],
                line[6],
                line[7],
                line[8],
                line[9],
                line[10],
                line[11],
            )
            player_dict[line[1]] = player
    tf = time.time()
    print("load_dict():", tf - ti)
    return player_dict


def _player_from_row(row):
    plyr = Player()
    plyr.from_row(row)
    return plyr


class Player:
    def __init__(self):
        return

    def from_row(
        self,
        name,
        first_name,
        last_name,
        position,
        birthdate,
        draft_year,
        draft_round,
        draft_pick,
        height,
        weight,
    ):
        self.name = name
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.birthdate = birthdate
        self.draft_year = draft_year
        self.draft_round = draft_round
        self.draft_pick = draft_pick
        self.height = height
        self.weight = weight

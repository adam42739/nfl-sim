import nflsim.nfl_data as nfl_data


def load_playersbase():
    COLUMNS_DEL = [
        "name",
        "position",
        "birthdate",
        "draft_year",
        "draft_round",
        "draft_pick",
        "height",
        "weight",
        "college",
    ]
    INDEXES = ["gsis_id", "player_obj"]
    player_df = nfl_data.get_players()
    player_df["player_obj"] = player_df.apply(_player_from_row, axis=1)
    player_df = player_df.drop(COLUMNS_DEL, axis=1)
    player_df = player_df[INDEXES]
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
        self.name = row["name"]
        self.position = row["position"]
        self.birthdate = row["birthdate"]
        self.draft_year = row["draft_year"]
        self.draft_round = row["draft_round"]
        self.draft_pick = row["draft_pick"]
        self.height = row["height"]
        self.weight = row["weight"]
        self.college = row["college"]

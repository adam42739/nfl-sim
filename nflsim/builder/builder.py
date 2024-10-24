from .players import players as build_players
import nfldpw.players as nfl_players
import nfldpw.players.cols as nfl_players_cols
import tqdm


def update_playerbase(nfl_cache_path: str, build_cache_path: str):
    nfl_df = nfl_players.get(cache_path=nfl_cache_path, refresh_cache=True)
    print(nfl_df.head())
    for index in tqdm.tqdm(nfl_df.index):
        mdata = build_players.load_metadata(build_cache_path)
        series = nfl_df.iloc[index]
        found = False
        for id_col in build_players.IDS:
            if str(series[id_col]) in mdata[id_col]:
                found = True
        if not found:
            build_players.new(series, len(mdata), build_cache_path)

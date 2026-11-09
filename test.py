import pandas as pd

url = "https://raw.githubusercontent.com/nflverse/nfldata/refs/heads/master/data/games.csv"
games = pd.read_csv(url)

cols = ["season", "week", "away_team", "home_team",
        "away_score", "home_score", "spread_line", "total_line", "total"]
games = games[cols].dropna(subset=["total"])   # drop unplayed games
games["over_hit"] = games["total"] > games["total_line"]

print(games)
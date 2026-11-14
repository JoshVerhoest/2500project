import pandas as pd
import numpy as np



main_df = pd.read_csv("full_league_hits.csv", usecols=[
    "launch_speed",
    "launch_angle",
    "bat_speed",
    "swing_length",
    "attack_angle",
    "attack_direction",
    "swing_path_tilt",
    "intercept_ball_minus_batter_pos_x_inches",
    "intercept_ball_minus_batter_pos_y_inches",
    "hc_x",
    "hc_y",
])

main_df["spray_angle"] = np.degrees(np.arctan((main_df["hc_x"] - 125.42) / (198.27 - main_df["hc_y"]))) * .75

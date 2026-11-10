#potential columns

'''
CONTACT QUALITY

launch_speed
launch_angle
bat_speed
swing_length
atack_angle
attack_direction
swing_path_tilt
intercept_ball_minus_batter_pos_x_inches / _y_inches -where bat meets ball

spray angle - from hc_x and hc_y
sprint_speed (more complex to get)
'''

'''
SOME OTHERS
release_speed, effective_speed, release_spin_rate, spin_axis
pfx_x, pfx_z (movement)
plate_x, plate_z (location)
sz_top, sz_bot (strike zone)
Game situation:

balls, strikes, outs_when_up, inning
on_1b / on_2b / on_3b: convert each to a 0/1 "runner present" flag
bat_score_diff
Categoricals that are worth encoding:

bb_type, if_fielding_alignment, of_fielding_alignment, stand, p_throws
home_team (ballpark effects)
pitch_type
'''
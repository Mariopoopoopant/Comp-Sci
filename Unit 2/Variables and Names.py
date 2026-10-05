team = "Toronto Blue Jays" #given variable values
current_date = "July 18, 2021"
player = "Vladimir Guerrero Jr."
home_runs_to_date = 31
games_played = 88
total_season_games = 162
home_run_record = 73

games_remaining = total_season_games - games_played #calculations to determine new values
home_runs_per_game = home_runs_to_date / games_played
projected_home_runs = home_runs_per_game * total_season_games
can_break_record = projected_home_runs > home_run_record

print(f"{player} of the {team}") #prints out all the text and values to the terminal
print(f"currently has {home_runs_to_date} home runs as of {current_date}")
print(f"currently, the MLB record for most amount of home runs in a season is {home_run_record}")
print(f"with {games_remaining} games remaining, and a average of {round(home_runs_per_game, 2)} home runs per game,")
print(f"it is {can_break_record} that he is on pace to break the record.")
print(f"{player} is projected to hit {round(projected_home_runs, 2)} home runs this season.")




import mlbstatsapi
from datetime import datetime

mlbAPI = mlbstatsapi.Mlb()

team_id = mlbAPI.get_team_id("Baltimore Orioles")
print(team_id)
# todays_date = datetime.today()
# print(todays_date)

# todays_game = mlbAPI.get_game_ids(str(todays_date))

# print(todays_game)


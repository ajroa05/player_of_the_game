import statsapi

ORIOLES_TEAM_ID = 110

recentGameID = statsapi.last_game(ORIOLES_TEAM_ID)

print(recentGameID)

box_data = statsapi.boxscore_data(recentGameID)


print(box_data.keys())

print(box_data.get("home").get("team"))
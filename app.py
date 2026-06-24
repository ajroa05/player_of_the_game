import statsapi

ORIOLES_TEAM_ID = 110

def check_if_home(game_data :dict, team_id: int) -> bool:
    home_team = game_data.get("home").get("team")

    if (home_team == team_id):
        return True
    else:
        return False


def main():
    recent_game_id = statsapi.last_game(ORIOLES_TEAM_ID)

    box_data = statsapi.boxscore_data(recent_game_id)

    isHome = check_if_home(box_data, ORIOLES_TEAM_ID)

    if (isHome):
        team_batters = box_data.get("homeBatters")
        print(team_batters.keys())
    else:
        team_batters = box_data.get("awayBatters")
        print(team_batters.keys())

    # print(recentGameID)


    # print(box_data.keys())

    # print(box_data.get("home").get("team"))

if __name__ == "__main__":
    main()


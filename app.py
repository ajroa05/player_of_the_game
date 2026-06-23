import statsapi

ORIOLES_TEAM_ID = 110

def CheckIfHome(gameData :dict, teamID: int) -> bool:
    box_data

    print(homeTeam)

    return false


def main():
    recentGameID = statsapi.last_game(ORIOLES_TEAM_ID)

    box_data = statsapi.boxscore_data(recentGameID)

    isHome = CheckIfHome(box_data, ORIOLES_TEAM_ID)

    # print(recentGameID)


    # print(box_data.keys())

    # print(box_data.get("home").get("team"))

if __name__ == "__main__":
    main()


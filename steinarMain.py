from LL.api_ll import APILL


def main():
    api = APILL()
    players = api.get_players_in_team("SegFault Spartans")
    for player in players:
        print(player.name, player.team)


main()

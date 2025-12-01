from LL.api_ll import APILL


class UserUI:
    def __init__(self, APILL: APILL) -> None:
        self.APILL = APILL

    def showTeams(self):
        teams = self.APILL.userLL.getAllTeams()
        print("Teams:")
        for id, team in teams.items():
            name = team[0]
            logo = team[2]
            teamCaptain = team[3]
            website = team[4]
            club = team[5]
            points = team[6]

            print("-----------------------------------------------------------")
            print(f"{id}:  {name} {logo} {teamCaptain} {website} {club} {points}")
        print("")
        print("b. back")
        print("q. quit")

    def showCurrentTournaments(self):
        tournaments = self.APILL.userLL.getAllTournaments()
        print("Tournaments:")
        for id, tourn in tournaments.items():
            print("-------------------------------------------------------")
            print(f"{tourn[0]} {tourn[1]}-{tourn[2]} {tourn[3]} {tourn[4]}")

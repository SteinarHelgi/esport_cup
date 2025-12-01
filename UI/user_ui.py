from LL.user_ll import UserLL


class UserUI:
    def __init__(self, APILL) -> None:
        self.APILL = APILL
        pass

    def showTeams(self):
        teams = self.APILL

        print(f"Teams: {teams}")

    def showTournaments(self):
        print("Tournaments: Blabla")
        userInput = input()
        if input == "1":
            self.showUpcomingTournaments()

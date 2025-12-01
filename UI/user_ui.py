from LL.user_ll import UserLL


class UserUI:
    def __init__(self) -> None:
        pass

    def showTeams(self):
        teams = UserLL.getAllTeams()

        print(f"Teams: {teams}")

    def showTournaments(self):
        print("Tournaments: Blabla")
        userInput = input()
        if input == "1":
            self.showUpcomingTournaments()

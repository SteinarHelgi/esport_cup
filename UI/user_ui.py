from LL.user_ll import UserLL
from LL.tournaments_ll import TournamentsLL

class UserUI:
    def __init__(self, APILL) -> None:
        self.APILL = APILL
        pass

    def showTeams(self):
        teams = self.APILL

        print(f"Teams: {teams}")

    def showTournaments(self):
        tournaments = getTournaments
        print("Tournaments: Blabla")
        userInput = input()
        if input == "1":
            self.showOngoingTournaments()
        elif input == '2':
            self.showUpcomingTournaments()
        elif input == '3':
            self.showPastTournaments
        
        
        

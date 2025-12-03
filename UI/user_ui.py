"""This is the page where everything related to the users UI is shown"""

from LL.api_ll import APILL
from Models.models import Team
from datetime import datetime
def print_back_and_quit():
    print("")
    print("b. Back")
    print("q. Quit")


class UserUI:
    def __init__(self, APILL: APILL, menu_manager) -> None:
        self.APILL = APILL
        self.menu_manager = menu_manager

    def show_teams(self):
        pass

    def show_tournaments(self):
        tournaments = self.APILL.get_all_tournaments()
        valid_options = ["1", "2", "3", "b", "q"]

        print("1. Ongoing tournaments \n2. Upcoming tournaments \n3. Past Tournaments")

        choice: str = self.menu_manager.prompt_choice(valid_options)
        print("choice:", choice)

        if choice == "1":
            return "ONGOING_TOURNAMENTS"
        elif choice == "2":
            return "UPCOMING_TOURNAMENTS"
        elif choice == "3":
            return  "PAST_TOURNAMENTS"
        elif choice == "b":
            return  "BACK"
        if choice == "q":
            return  "QUIT"

    def show_ongoing_tournaments(self): #Shows the tournaments that are going on at the time of checking
        today = datetime.today()
        tournaments = self.APILL.get_ongoing_tournaments(today)
        print("Ongoing Tournaments:")
        for tournament in tournaments:
            print(tournament.name, str(tournament.start_date).split(" ")[0])
        

    def show_upcoming_tournaments(self): #Shows the tournaments that are starting after the date of checking
        today = datetime.today()
        tournaments = self.APILL.get_upcoming_tournaments(today)
        print("Upcoming Tournaments")
        for tournament in tournaments:
            print(tournament.name, str(tournament.start_date).split(" ")[0])


    def show_past_tournaments(self):
        today = datetime.today()
        tournaments = self.APILL.get_past_tournaments(today)
        print("Past Tournaments")
        for tournament in tournaments:
            print(tournament.name, str(tournament.start_date).split(" ")[0])

    def show_players(self, team: Team):
        # Todo
        pass

    def show_statistics(self):
        # TODO
        pass

"""This is the page where everything related to the users UI is shown"""

from LL.api_ll import APILL
from LL.functions import format_team_list, format_tournament_table
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

    def show_teams(self) -> str:
        teams = self.APILL.get_all_teams()
        print(format_team_list(self, teams))
        return "QUIT"

        choice: str = self.menu_manager.prompt_choice(["1", "2", "3", "q"])

        if choice == "1":
            return "LOGIN_PAGE"
        else:
            return "QUIT"

    def show_tournaments(self) -> str:
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
            return "PAST_TOURNAMENTS"
        elif choice == "b":
            return "BACK"
        else:
            return "QUIT"

    def show_ongoing_tournaments(
        self,
    ):  # Shows the tournaments that are going on at the time of checking
        today = datetime.today()
        tournaments = self.APILL.get_ongoing_tournaments(today)
        print("Ongoing Tournaments:")
        print(format_tournament_table(self, tournaments))
        return "QUIT"
        

    def show_upcoming_tournaments(
        self,
    ):  # Shows the tournaments that are starting after the date of checking
        today = datetime.today()
        tournaments = self.APILL.get_upcoming_tournaments(today)
        print("Upcoming Tournaments")
        print(format_tournament_table(self, tournaments))
        return "QUIT"
        
        
    def show_past_tournaments(self):
        today = datetime.today()
        tournaments = self.APILL.get_past_tournaments(today)
        print("Past Tournaments")
        print(format_tournament_table(self, tournaments))
        return "QUIT"
        

    def show_players(self, team: Team):
        players = self.APILL.get_players_in_team(team.name)
        for player in players:
            print(player.name, player.handle)
        valid_options = ["q","b"]
        choice: str = self.menu_manager.prompt_choice(valid_options)
        if choice == "q":
            return "QUIT"
        if choice == "b":
            return "BACK"
        
        

    def show_statistics(self):
        # TODO
        pass

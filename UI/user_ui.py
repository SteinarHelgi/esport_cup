"""This is the page where everything related to the users UI is shown"""

from os import name
from LL.api_ll import APILL
from UI.functions import format_player_list, format_team_list, format_tournament_table
from Models.models import Team
from datetime import datetime


class UserUI:
    def __init__(self, APILL: APILL, menu_manager) -> None:
        self.APILL = APILL
        self.menu_manager = menu_manager

    def show_teams(self):
        teams = self.APILL.get_all_teams()
        print(format_team_list(teams))
        print("\nb.Back \nq.Quit")

        valid_choices = []
        for counter, team in enumerate(teams):
            valid_choices.append(str(counter))

        choice: str = self.menu_manager.prompt_choice(valid_choices + ["b", "q"])

        if choice in valid_choices:
            return self.show_players(teams[int(choice) - 1])

        if choice.lower() == "b":
            return "USER_MENU"

        return "QUIT"

    def show_tournaments(self):
        tournaments = self.APILL.get_all_tournaments()
        valid_options = ["1", "2", "3", "b", "q"]
        print(
            "1. Ongoing tournaments \n2. Upcoming tournaments \n3. Past Tournaments \nb. Back \nq. Quit"
        )
        choice: str = self.menu_manager.prompt_choice(valid_options)

        if choice == "1":
            return self.show_tournaments_blabla("PAST")
        elif choice == "2":
            return self.show_tournaments_blabla("UPCOMING")
        elif choice == "3":
            return self.show_tournaments_blabla("ONGOING")
        elif choice.lower() == "b":
            return "LOGIN_MENU"
        else:
            return "QUIT"

    def show_tournaments_blabla(
        self, time: str
    ):  # Shows the tournaments that are going on at the time of checking
        tournaments = []
        if time == "PAST":
            tournaments = self.APILL.get_past_tournaments()
            print("Past Tournaments:")
            print(format_tournament_table(tournaments))
            print("b.Back \nq.Quit")
        if time == "UPCOMING":
            tournaments = self.APILL.get_upcoming_tournaments()
            print("Upcoming Tournaments:")
            print(format_tournament_table(tournaments))
            print("b.Back \nq.Quit")
        if time == "ONGOING":
            tournaments = self.APILL.get_ongoing_tournaments()
            print("Ongoing Tournaments:")
            print(format_tournament_table(tournaments))
            print("b.Back \nq.Quit")
        # TODO Detailed tournaments look
        choice: str = self.menu_manager.prompt_choice(["b", "q"])

        if choice.lower() == "b":
            return "TOURNAMENTS"
        else:
            "QUIT"

    def show_players(self, team: Team):
        players = self.APILL.get_players_in_team(team.name)
        print(format_player_list(players))
        valid_options = ["q", "b"]
        choice: str = self.menu_manager.prompt_choice(valid_options)
        if choice.lower() == "q":
            return "QUIT"
        if choice.lower() == "b":
            return "TEAMS"

    def show_statistics(self):
        # TODO
        pass

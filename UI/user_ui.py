"""This is the page where everything related to the users UI is shown"""

from LL.api_ll import APILL
from Models.tournament import Tournament
from UI.functions import format_player_list, format_tournament_table
from Models.models import Team
from UI.ui_functions import refresh_logo


class UserUI:
    """Class for all of ui functions"""

    def __init__(self, APILL: APILL, menu_manager) -> None:
        self.APILL = APILL
        self.menu_manager = menu_manager

    def show_teams(self):
        """Shows teams that exist within the software"""
        teams = self.APILL.get_all_teams()
        teams[0]._print_header()
        for index, team in enumerate(teams):
            team.format_row(index + 1)
            team._print_divider_line()
        print("\nb.Back \nq.Quit")

        valid_choices = []
        for counter, team in enumerate(teams):
            valid_choices.append(str(counter + 1))

        choice: str = self.menu_manager.prompt_choice(valid_choices + ["b", "q"])

        if choice in valid_choices:
            return self.show_players(teams[int(choice) - 1])

        if choice.lower() == "b":
            if self.menu_manager.user == "USER":
                return "USER_MENU"
            if self.menu_manager.user == "TEAM_CAPTAIN":
                return "TEAM_CAPTAIN_MENU"
            if self.menu_manager.user == "ORGANISER":
                return "ORGANISER_MENU"

        return "QUIT"

    def show_tournaments(self):
        """Prints tournaments according to user choice and time of choosing"""
        tournaments = self.APILL.get_all_tournaments()
        valid_options = ["1", "2", "3", "b", "q"]
        print(
            "1. Ongoing tournaments \n2. Upcoming tournaments \n3. Past Tournaments \nb. Back \nq. Quit"
        )
        choice: str = self.menu_manager.prompt_choice(valid_options)

        if choice == "1":
            return self.show_tournaments_calling_function("ONGOING")
        elif choice == "2":
            return self.show_tournaments_calling_function("UPCOMING")
        elif choice == "3":
            return self.show_tournaments_calling_function("PAST")
        elif choice.lower() == "b":
            if self.menu_manager.user == "USER":
                return "USER_MENU"
            if self.menu_manager.user == "TEAM_CAPTAIN":
                return "TEAM_CAPTAIN_MENU"
            if self.menu_manager.user == "ORGANISER":
                return "ORGANISER_MENU"
        else:
            return "QUIT"

    def show_tournaments_calling_function(
        self, time: str
    ):  # Shows the tournaments that are going on at the time of checking
        refresh_logo()
        tournaments = []
        if time == "PAST":
            tournaments = self.APILL.get_past_tournaments()
            print("Past Tournaments:")
            print(format_tournament_table(tournaments))
            print("Select tournament by ID")
            print("b.Back \nq.Quit")
        if time == "UPCOMING":
            tournaments = self.APILL.get_upcoming_tournaments()
            if tournaments != []:
                print("Upcoming Tournaments:")
                print(format_tournament_table(tournaments))
                print("Select tournament by ID")
                print("b.Back \nq.Quit")
            else:
                print("There are no upcoming tournaments")
                print("b.Back \nq.Quit")
        if time == "ONGOING":
            tournaments = self.APILL.get_ongoing_tournaments()
            if tournaments != []:
                print("Ongoing Tournaments:")
                print(format_tournament_table(tournaments))
                print("Select tournament by ID")
                print("b.Back \nq.Quit")
            else:
                print("There are no ongoing tournaments")
                print("b.Back \nq.Quit")
        valid_choices = []
        for counter, tournament in enumerate(tournaments):
            valid_choices.append(str(counter + 1))

        choice: str = self.menu_manager.prompt_choice(valid_choices + ["b", "q"])
        if choice in valid_choices:
            return self.show_tournament_view(tournaments[int(choice) - 1], time)

        if choice.lower() == "b":
            return "TOURNAMENTS"
        else:
            "QUIT"

    def show_tournament_view(self, tournament: Tournament, time: str):
        """takes in a tournament name and shows the menu for the tournament"""

        refresh_logo()
        w_team = 26
        w_date = 12
        w_time = 12
        w_round = 8
        w_vs = 4
        w_completed = 10
        if tournament:
            print(
                f"{tournament.name.upper()}  |  {tournament.start_date} -- {tournament.end_date} "
            )
            print("--------------------")
            print(" ")
            print("Matches: ")
            header = (
                f"{'Team 1':<{w_team}}"
                f"{'vs':^{w_vs}}"
                f"{'Team 2':>{w_team}} "
                f"{'Date':^{w_date}}"
                f"{'Time':^{w_time}}"
                f"{'Round':>{w_round}}"
                f"{'Completed':>{w_completed}}"
                f"{'Winner':<{w_team}}"
            )
            print(header)
            print("-" * len(header))
            for match in tournament.matches:
                print(f"{match}")

            print("")
            
            print("b. Back")
            print("q. Quit")

        choice: str = self.menu_manager.prompt_choice(["b", "q"])
        if choice == "b":
            return self.show_tournaments_calling_function(time)

    def show_players(self, team: Team):
        """Shows a list of players when you select a team"""
        refresh_logo()
        print(team.my_team_header())
        players = self.APILL.get_players_in_team(team.name)
        for index, player in enumerate(players):
            player.format_row(index + 1)
        if self.menu_manager.user == "USER":
            valid_options = ["q", "b"]
        if self.menu_manager.user == "ORGANISER":
            valid_options
        print("\nb.Back\nq.Quit")
        choice: str = self.menu_manager.prompt_choice(valid_options)

        if choice.lower() == "q":
            return "QUIT"
        if choice.lower() == "b":
            return "TEAMS"

    def show_statistics(self):
        # TODO
        pass

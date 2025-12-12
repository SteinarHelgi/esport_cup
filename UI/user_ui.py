"""This is the page where everything related to the users UI is shown"""

from LL.api_ll import APILL
from UI.functions import format_tournament_table
from UI.ui_functions import refresh_logo
from Models.models import Player, Tournament


class UserUI:
    """Class for all of ui functions"""

    def __init__(self, APILL: APILL, menu_manager) -> None:
        self.APILL = APILL
        self.menu_manager = menu_manager

    def show_teams(self):
        """Shows teams that exist within the software"""
        teams = self.APILL.get_all_teams()
        teams[0]._print_header()
        teams[0]._print_divider_line()
        for index, team in enumerate(teams):
            team.format_row(index + 1)
            team._print_divider_line()
        print("Select a team by ID")
        print("")
        print("\nb.Back \nq.Quit")

        valid_choices = []
        for counter, team in enumerate(teams):
            valid_choices.append(str(counter + 1))

        choice: str = self.menu_manager.prompt_choice(valid_choices + ["b", "q"])

        if choice in valid_choices:
            self.menu_manager.team_to_view = teams[int(choice) - 1]
            return "PLAYERS"

        if choice.lower() == "b":
            if self.menu_manager.user == "USER":
                return "USER_MENU"
            if self.menu_manager.user == "TEAM_CAPTAIN":
                return "TEAM_CAPTAIN_MENU"
            if self.menu_manager.user == "ORGANISER":
                return "ORGANISER_MENU"

        return "QUIT"

    def show_player_view(self, player: Player):
        """takes in a player name and shows the menu for the player"""

        refresh_logo()
        if player:
            print(f"{player.name.upper()}  |  {player.handle} ")
            print("-" * len(f"    SOCIAL MEDIA: {player.social_media}"))

            print(f"    DATE OF BIRTH: {player.date_of_birth}")
            print(f"    ADDRESS: {player.address}")
            print(f"    PHONE: {player.phone_number}")
            print(f"    EMAIL: {player.email}")
            print(f"    HANDLE: {player.handle}")
            print(f"    SOCIAL MEDIA: {player.social_media}")
            print(f"    TEAM: {player.team_name}")
            print("-" * len(f"    SOCIAL MEDIA: {player.social_media}"))

            print("")
            valid_choices = []
            if self.menu_manager.user == "TEAM_CAPTAIN":
                print("1. Edit player data")
                valid_choices = ["1"]

            print("")
            print("b. Back")
            print("q. Quit")

            choice: str = self.menu_manager.prompt_choice(valid_choices + ["b", "q"])

            if choice == "1" and self.menu_manager.user == "TEAM_CAPTAIN":
                # Modify player menuið
                return self.menu_manager.team_captain_ui.show_modify_player_menu(player)
            if choice == "b":
                return "PLAYERS"

            if choice == "q":
                return "QUIT"

    def show_players(self):
        """Shows a list of players when you select a team"""
        refresh_logo()
        team = self.menu_manager.team_to_view
        print(team.my_team_header())
        players = self.APILL.get_players_in_team(team.name)
        valid_options = []
        for index, player in enumerate(players):
            if self.menu_manager.user == "USER":
                print(player)
            elif self.menu_manager.user == "TEAM_CAPTAIN":
                print(player)
            else:
                player.format_row(index + 1)
                if self.menu_manager.user == "ORGANISER":
                    valid_options.append(str(index + 1))

        print("")
        print("t. Tournaments for team \nb. Back \nq. Quit")
        choice: str = self.menu_manager.prompt_choice(valid_options + ["t", "b", "q"])
        for element in valid_options:
            if element == choice and self.menu_manager.user == "ORGANISER":
                player = self.show_player_view(players[int(element) - 1])
                return player
        if choice == "t":
            if team:
                tournaments = self.APILL.get_all_tournaments_for_team(team)
                print("All tournaments for this team.")
                print(format_tournament_table(tournaments))
                print("b. Back \nq. Quit")
                choice: str = self.menu_manager.prompt_choice(["b", "q"])
                if choice == "q":
                    return "QUIT"
                if choice == "b":
                    return "TEAMS"

        if choice.lower() == "q":
            return "QUIT"
        if choice.lower() == "b":
            return "TEAMS"

    def show_tournaments(self):
        """Prints tournaments according to user choice and time of choosing"""
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

    def show_clubs(self):
        """Shows all clubs and their teams"""

        clubs = self.APILL.get_all_club_data()
        print("Clubs: ")
        for club in clubs:
            print(club)
            print(club._divider_line())

        print("b. Back\nq. Quit")
        choice: str = self.menu_manager.prompt_choice(["b", "q"])
        if choice == "b":
            if self.menu_manager.user == "USER":
                return "USER_MENU"
            if self.menu_manager.user == "ORGANISER":
                return "ORGANISER_MENU"
            if self.menu_manager.user == "TEAM_CAPTAIN":
                return "TEAM_CAPTAIN_MENU"
        if choice == "q":
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
        for i in range(len(tournaments)):
            string_i = str(i + 1)
            valid_choices.append(string_i)

        choice: str = self.menu_manager.prompt_choice(valid_choices + ["b", "q"])
        for element in valid_choices:
            if element == choice:
                return self.show_tournament_view(tournaments[int(element) - 1], time)
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
                f"{'Winner':>{w_team}}"
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

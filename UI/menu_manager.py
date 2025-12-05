import os
from LL.api_ll import APILL
from UI.user_ui import UserUI
from UI.team_captain_ui import TeamCaptainUI
from UI.organiser_ui import OrganiserUI


class MenuManager:
    """Responsible for menus and prompts for the choice"""

    def __init__(self, api_ll: APILL) -> None:
        self.api_ll = api_ll
        self.user_ui = UserUI(self.api_ll, self)
        self.team_captain_ui = TeamCaptainUI(self.api_ll, self)
        self.organiser_Ui = OrganiserUI(self.api_ll, self)
        self.user = ""
        self.team_name = ""

        self.pages = {
            "LOGIN_MENU": self.print_login_menu,
            "LOGIN_CREDENTIALS": self.login_credentials_menu,
            "LOGIN_CREDENTIALS_ORG": self.login_credentials_menu_org,
            # USER MENUS
            "USER_MENU": self.print_user_menu,
            "TEAMS": self.user_ui.show_teams,
            "TOURNAMENTS": self.user_ui.show_tournaments,
            "ONGOING_TOURNAMENTS": self.user_ui.show_ongoing_tournaments,
            "UPCOMING_TOURNAMENTS": self.user_ui.show_upcoming_tournaments,
            "PAST_TOURNAMENTS": self.user_ui.show_past_tournaments,
            "PLAYERS": self.user_ui.show_players,
            "STATISTICS": self.user_ui.show_statistics,
            # TEAM CAPTAIN MENUS
            "TEAM_CAPTAIN_MENU": self.print_team_captain_menu,
            "CREATE_PLAYER": self.team_captain_ui.show_create_player,
            "MODIFY_PLAYER": self.team_captain_ui.show_modify_player,
            "MY_TEAM": self.team_captain_ui.show_my_team,
            "MY_TOURNAMENTS_CAP": self.team_captain_ui.show_my_tournaments,
            "REGISTER_TEAM_TO_TOURNAMENT": self.team_captain_ui.show_register_team_to_tournament,
            "UPDATE_TEAM_DATA": self.team_captain_ui.show_update_team_data,
            "ADD_TEAM_TO_CLUB": self.team_captain_ui.show_add_team_to_club,
            "CREATE_TEAM": self.team_captain_ui.show_create_team,
            "SHOW_MY_PLAYERS": self.team_captain_ui.show_my_players,
            # ORGANISER MENUS
            "ORGANISER_MENU": self.print_organiser_menu,
            "CREATE_TOURNAMENT_MENU": self.organiser_Ui.show_create_tournament,
            "MY_TOURNAMENTS_ORG": self.organiser_Ui.show_my_tournaments,
            "CREATE_MATCH": self.organiser_Ui.show_create_match,
            "REGISTER_RESULTS": self.organiser_Ui.show_register_results,
            "DELETE_TOURNAMENT": self.organiser_Ui.show_delete_tournament,
            "GIVE_POINTS": self.organiser_Ui.show_give_points,
        }

    def prompt_choice(self, valid_choices: list[str]) -> str:
        """Prompt user, only give back valid choice"""
        valid_lower = []
        for choice in valid_choices:
            valid_lower.append(choice.lower())

        while True:
            choice: str = input("\n> ").strip().lower()
            if choice in valid_lower:
                return choice
            print("Not a valid choice")
            print("valid choices are: ")
            for choice in valid_lower:
                print(choice, ".", sep="")

    def print_login_menu(self):  # Login menu
        print("___ LOGIN ___")
        print("1. continue as user \n2. Login as Team Captain \n3. Login as Organiser")
        choice: str = self.prompt_choice(["1", "2", "3", "q"])
        if choice == "1":
            self.user = "USER"
            return "USER_MENU"
        if choice == "2":
            self.user = "TEAM_CAPTAIN"
            # return "LOGIN_CREDENTIALS"
            return "TEAM_CAPTAIN_MENU"
        if choice == "3":
            self.user = "ORGANISER"
            # return "LOGIN_CREDENTIALS_ORG"
            return "ORGANISER_MENU"
        return "QUIT"

    def login_credentials_menu(self):  # logging in as organiser
        username = input("Your handle: ")
        print(f"Handle: {username}\nConfirm(Y/N)? ")
        choice: str = self.prompt_choice(["y", "n"])
        self.team_name = "NullPointer Ninjas"
        if choice.lower() == "y":
            return "TEAM_CAPTAIN_MENU"
        else:
            return "LOGIN_MENU"

    def login_credentials_menu_org(self):  # logging in as organiser
        username = input("Username: ")
        print(f"Username: {username}\nConfirm(Y/N)? ")
        choice: str = self.prompt_choice(["y", "n"])
        if choice.lower() == "y":
            return "ORGANISER_MENU"
        else:
            return "LOGIN_MENU"

    def print_user_menu(self):  # Option menu for user
        # TODO
        print("__USER__")
        print("1. Teams \n2. Tournaments \nb. Back \nq. Quit")

        choice: str = self.prompt_choice(["1", "2", "q"])
        if choice == "1":
            return "TEAMS"
        if choice == "2":
            return "TOURNAMENTS"
        if choice.lower() == "b":
            return "LOGIN_MENU"
        return "QUIT"

    def print_team_captain_menu(self):  # Option menu for team captain
        # TODO
        self.team_name = "NullPointer Ninjas"
        print("__TEAM_CAPTAIN_MENU__")
        print(
            "1. Teams \n2. Tournaments \n3. My Team \n4. My Tournaments \nb. back \nq. Quit"
        )

        choice: str = self.prompt_choice(["1", "2", "3", "4", "b", "q"])
        if choice == "1":
            return "TEAMS"
        if choice == "2":
            return "TOURNAMENTS"
        if choice == "3":
            return "MY_TEAM"
        if choice == "4":
            return "MY_TOURNAMENTS"
        if choice.lower() == "b":
            return "LOGIN_MENU"

        return "QUIT"

    def print_organiser_menu(self):  # option menu for organiser
        # TODO
        print("__ORGANISER_MENU__")
        print(
            "1. Teams \n2. Tournaments \n3. Create Tournaments \n4. My Tournaments \nb. Back \nq. Quit"
        )
        choice: str = self.prompt_choice(["1", "2", "3", "4", "b", "q"])
        if choice == "1":
            return "TEAMS"
        if choice == "2":
            return "TOURNAMENTS"
        if choice == "3":
            return "CREATE_TOURNAMENT_MENU"
        if choice == "4":
            return "MY_TOURNAMENTS_ORG"
        if choice.lower() == "b":
            return "LOGIN_MENU"

        return "QUIT"

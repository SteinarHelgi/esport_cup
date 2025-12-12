from LL.api_ll import APILL
from Models.models import Team
from UI.ui_functions import refresh_logo
from UI.user_ui import UserUI
from UI.team_captain_ui import TeamCaptainUI
from UI.organiser_ui import OrganiserUI
from UI.shrek import shrek


class MenuManager:
    """Responsible for menus and prompts for the choice"""

    def __init__(self, api_ll: APILL) -> None:
        self.api_ll = api_ll
        self.user_ui = UserUI(self.api_ll, self)
        self.team_captain_ui = TeamCaptainUI(self.api_ll, self)
        self.organiser_Ui = OrganiserUI(self.api_ll, self)
        self.shrek = shrek
        self.user = ""
        self.team_name = ""
        self.team_to_view: Team

        self.pages = {
            "LOGIN_MENU": self.print_login_menu,
            "LOGIN_CREDENTIALS": self.login_credentials_menu,
            "SHREK": shrek,
            # USER MENUS
            "USER_MENU": self.print_user_menu,
            "TEAMS": self.user_ui.show_teams,
            "TOURNAMENTS": self.user_ui.show_tournaments,
            "PLAYERS": self.user_ui.show_players,
            "CLUBS": self.user_ui.show_clubs,
            # TEAM CAPTAIN MENUS
            "TEAM_CAPTAIN_MENU": self.print_team_captain_menu,
            "CREATE_PLAYER": self.team_captain_ui.show_create_player,
            "PLAYER_ADDED_SCREEN": self.team_captain_ui.player_added_screen,
            "MY_TEAM": self.team_captain_ui.show_my_team,
            "MY_TOURNAMENTS_CAP": self.team_captain_ui.show_my_tournaments,
            "ADD_TEAM_TO_CLUB": self.team_captain_ui.show_add_team_to_club,
            "SHOW_MY_PLAYERS": self.team_captain_ui.show_my_players,
            # ORGANISER MENUS
            "ORGANISER_MENU": self.print_organiser_menu,
            "CREATE_TOURNAMENT_MENU": self.organiser_Ui.show_create_tournament,
            "MY_TOURNAMENTS_ORG": self.organiser_Ui.show_my_tournaments,
            "CREATE_MATCH": self.organiser_Ui.show_create_match,
            "REGISTER_RESULTS": self.organiser_Ui.show_register_results,
            "DELETE_TOURNAMENT": self.organiser_Ui.show_delete_tournament,
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
            formatted = (
                "Valid choices are | "
                + " | ".join(f"{c}." for c in valid_choices)
                + " |"
            )
            print(formatted)

    def print_login_menu(self):
        """Menu for logging in depending on who the user is at the time"""
        print("=== LOGIN ===")
        print("")
        print(
            "1. Continue as user \n2. Continue as Team Captain \n3. Continue as Organiser\n69. Shrek"
        )
        choice: str = self.prompt_choice(["1", "2", "3", "69", "q"])
        if choice == "1":
            self.user = "USER"
            return "USER_MENU"
        if choice == "2":
            self.user = "TEAM_CAPTAIN"
            return "LOGIN_CREDENTIALS"
        if choice == "3":
            self.user = "ORGANISER"
            return "ORGANISER_MENU"
        if choice == "69":
            return "SHREK"
        return "QUIT"

    def login_credentials_menu(self):
        """Username logging in as a team captain"""

        while True:  # Loop until a valid username is entered or the user quits
            username = input(
                "Continue with Team Captain handle:\n \nb. Back\nq. Quit\n\n> "
            )
            teams = self.api_ll.get_all_teams()
            if username == "b":
                return "LOGIN_MENU"
            if username == "q":
                return "QUIT"
            print(f"Handle: {username}")
            found_name = False

            for team in teams:
                if team.captain_handle == username:
                    print("Confirm (Y/N)?")
                    choice: str = self.prompt_choice(["y", "n"])
                    found_name = True
                    self.team_name = team.name
                    self.team_to_view = team
                    self.captain_handle = team.captain_handle
                    if choice.lower() == "y":
                        return "TEAM_CAPTAIN_MENU"
                    else:
                        return "LOGIN_MENU"

            # If the username is not found
            if not found_name:
                print(
                    "Invalid username, press enter to try again or b to back and q to quit: "
                )
                choice: str = self.prompt_choice(["", "b", "q"])
                if choice == "":
                    refresh_logo()
                    continue  # Loop again to prompt for the username
                if choice == "q":
                    return "QUIT"
                if choice == "b":
                    return "LOGIN_MENU"


    def print_user_menu(self):
        """Menu of options for an organiser"""
        print("=== USER ===")
        print("")
        print("1. Teams \n2. Tournaments\n3. Clubs \n\nb. Back \nq. Quit")

        choice: str = self.prompt_choice(["1", "2", "3", "b", "q"])
        if choice == "1":
            return "TEAMS"
        if choice == "2":
            return "TOURNAMENTS"
        if choice == "3":
            return "CLUBS"
        if choice.lower() == "b":
            return "LOGIN_MENU"
        return "QUIT"

    def print_team_captain_menu(self):
        """Menu of options for team captain"""
        print("=== TEAM_CAPTAIN ===")
        print("")
        print(
            "1. Teams \n2. Tournaments\n3. Clubs \n4. My Team \n5. My Tournaments\n\nb. Back \nq. Quit"
        )

        choice: str = self.prompt_choice(["1", "2", "3", "4", "5", "b", "q"])
        if choice == "1":
            return "TEAMS"
        if choice == "2":
            return "TOURNAMENTS"
        if choice == "3":
            return "CLUBS"
        if choice == "4":
            return "MY_TEAM"
        if choice == "5":
            return "MY_TOURNAMENTS_CAP"
        if choice.lower() == "b":
            return "LOGIN_MENU"

        return "QUIT"

    def print_organiser_menu(self):
        """Menu of options for an organiser"""
        print("=== ORGANISER_MENU ===")
        print("")
        print(
            "1. Teams \n2. Tournaments\n3. Clubs \n4. Create Tournament \n5. My Tournaments\n\nb. Back \nq. Quit"
        )
        choice: str = self.prompt_choice(["1", "2", "3", "4", "5", "b", "q"])
        if choice == "1":
            return "TEAMS"
        if choice == "2":
            return "TOURNAMENTS"
        if choice == "3":
            return "CLUBS"
        if choice == "4":
            return "CREATE_TOURNAMENT_MENU"
        if choice == "5":
            return "MY_TOURNAMENTS_ORG"
        if choice.lower() == "b":
            return "LOGIN_MENU"

        return "QUIT"

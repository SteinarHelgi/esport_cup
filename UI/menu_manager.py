from LL.api_ll import APILL


class MenuManager:
    """Responsible for all menus and prompts for the choice"""

    def __init__(self, api_ll: APILL) -> None:
        self.api_ll = api_ll

        self.pages = {
            "LOGIN_MENU": self.print_login_menu,
            "USER_MENU": self.print_user_menu,
            "TEAM_CAPTAIN_MENU": self.print_team_captain_menu,
            "ORGANISER_MENU": self.print_organiser_menu,
        }

    def prompt_choice(self, valid_choices: list[str]) -> str:
        """Prompt user, only give back valid choice"""
        valid_lower = []
        for choice in valid_choices:
            valid_lower.append(choice.lower())

        while True:
            choice: str = input("> ").strip().lower()
            if choice in valid_lower:
                return choice
            print("Not a valid choice")
            print("valid choices are: ")
            for choice in valid_lower:
                print(choice, ".", sep="")

    def print_login_menu(self):  # Login menu
        print("__________LOGIN_________")
        print("1. continue as user \n2. Login as Team Captain \n3. Login as Organiser")
        choice: str = self.prompt_choice(["1", "2", "3", "q"])
        if choice == "1":
            return "USER_MENU"
        if choice == "2":
            return "TEAM_CAPTAIN_MENU"
        if choice == "3":
            return "ORGANISER_MENU"
        return "QUIT"

    def print_user_menu(self):  # Option menu for user
        # TODO
        print("__SELECT AN OPTION__")
        print("1. Teams \n2. Tournaments \nq. Quit")

        choice: str = self.prompt_choice(["1", "2", "q"])
        if choice == "1":
            return "TEAMS"
        if choice == "2":
            return "TOURNAMENTS"
        return "QUIT"

    def print_team_captain_menu(self):  # Option menu for team captain
        # TODO
        print("__SELECT AN OPTION__")
        print("1. Teams \n2. Tournaments \n3. My Team \n4. My Tournaments \nq. Quit")

        choice: str = self.prompt_choice(["1", "2", "3", "4", "q"])
        if choice == "1":
            return "TEAMS"
        if choice == "2":
            return "TOURNAMENTS"
        if choice == "3":
            return "MY_TEAM"
        if choice == "4":
            return "MY_TOURNAMENTS"

        return "QUIT"

    def print_organiser_menu(self):  # option menu for organiser
        # TODO
        print("__SELECT AN OPTION__")
        print(
            "1. Teams \n2. Tournaments \n3. Create Tournaments \n4. My Tournaments \nq. Quit"
        )
        choice: str = self.prompt_choice(["1", "2", "3", "4", "q"])
        if choice == "1":
            return "TEAMS"
        if choice == "2":
            return "TOURNAMENTS"
        if choice == "3":
            return "CREATE_TOURNAMENT"
        if choice == "4":
            return "MY_TOURNAMENTS_ORGANISER"

        return "QUIT"

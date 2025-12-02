def print_login_menu():  # Login menu
    print("__________LOGIN_________")
    print("1. continue as user \n2. Login as Team Captain \n3. Login as Organiser")


def print_user_menu():  # Option menu for user
    print("__SELECT AN OPTION__")
    print("1. Teams \n2. Tournaments \nq. Quit")


def print_team_captain_menu():  # Option menu for team captain
    print("__SELECT AN OPTION__")
    print("1. Teams \n2. Tournaments \n3. My Team \n4. My Tournaments \nq. Quit")


def print_organiser_menu():  # option menu for organiser
    print("__SELECT AN OPTION__")
    print(
        "1. Teams \n2. Tournaments \n3. Create Tournaments \n4. My Tournaments \nq. Quit"
    )


def print_team_menu():  # Prints a list of teams with the corresponding information
    list_of_teams = 0
    return list_of_teams
    # TODO add options for this menu


def print_tournament_menu():  # Menu for looking at tournaments
    print(
        "1. Ongoing Tournaments \n2. Upcoming Tournaments \n3. Past Tournaments \nb. Back \nq.Quit"
    )


def print_my_team_menu():  # Options for my team
    club = 0
    team_name = 0
    link = 0
    logo = 0
    captain = 0
    print(f"{club} {team_name} {link} {logo} {captain}")
    print("1. Add team to club \n2. Roster \n3. Edit team info \nb. Back \nq. Quit")


def show_main_menu(self) -> str:
    """Print main menu and return 'LIST', 'CREATE' or 'QUIT'."""
    print("\n==== Aðalvalmynd ====")
    print("1. Skoða matseðla")
    print("2. Búa til nýjan matseðil")
    print("q. Hætta")

    choice: str = self._prompt_choice(["1", "2", "q"])
    if choice == "1":
        return "LIST"
    if choice == "2":
        return "CREATE"
    return "QUIT"


def tournaments_for_my_team():
    tournaments_registered = 0
    return tournaments_registered


def register_for_tournament():
    available_tournaments = 0
    print(f"{available_tournaments}")

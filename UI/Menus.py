# First menu and login menus


def login_credentials_menu():  # logging in as organiser
    username = "Chuck Norris"
    password = "Pepsi Max"
    print(f"Username: {username} \nPassword: {password} \nConfirm(Y/N)? ")


# Teams and Tournaments menu that all users can use
def print_team_menu():  # Prints a list of teams with the corresponding information
    list_of_teams = 0
    return list_of_teams  # with clubs
    # TODO add options for this menu


def print_tournaments_menu():  # Menu for looking at tournaments
    print(
        "1. Ongoing Tournaments \n2. Upcoming Tournaments \n3. Past Tournaments \nb. Back \nq.Quit"
    )


# Team captain menus
def print_my_team_menu():  # Options for my team
    club = 0
    team_name = 0
    link = 0
    logo = 0
    captain = 0
    print(f"{club} {team_name} {link} {logo} {captain}")
    print("1. Add team to club \n2. Roster \n3. Edit team info \nb. Back \nq. Quit")


def add_team_to_club():
    list_of_clubs = 0
    print(f"{list_of_clubs}")


def tournaments_for_my_team():  # Tournaments that team is registered to
    tournaments_registered = 0
    return tournaments_registered


def register_for_tournament():  # option to register for available tournaments
    available_tournaments = 0
    print(f"{available_tournaments}")
    # TODO options for list of tournaments


def edit_team_info():
    print(
        "1. Club \n2. Website/Social Media \n3. Logo \n4. Team Captain \nb. Back \nq. Quit"
    )


def roster_menu():
    print(
        "1. Add player to team \n2. Player Information \n3. Remove player from team \nb. Back \nq. Quit"
    )



def player_added():
    player_name = "Chuck Norris"
    player_handle = "You Know Who I am"
    player_social = "@chuckfucks"
    print(f"PLAYER ADDED!\n{player_name} \n{player_handle} \n{player_social} \nq. Quit")


# Organiser menus


def create_tournament_menu(self):
    print("Fill in the required info!")
    name_of_tournament = input("Name: ")
    start_date_of_tournament = input("Start date(Year-MOnth-Day): ")
    end_date_of_tournamnet = input("End date(Year-Month-Day): ")
    amount_of_servers = int(input("Number of servers: "))
    venue = input("Venue: ")
    double_elimination = input("Double elimination(Y/N): ")
    game_for_tournament = input("Game: ")
    choice: str = self.menu_manager.prompt_choice(["b","q"])
    print("b. Back \nq. Quit")
    

def create_contact_person_menu():
    print("Fill in contact person info!")
    new_contact_person_name = input("Name: ")
    new_contact_person_email = input("Email: ")
    new_contact_person_phone_nmbr = input("Phone number: ")
    confirmation = input("Confirm(Y/N): ")
    



def tournament_created_menu():
    tournament_name = "Chuck Norris Open"
    venue = "Everywhere"
    game = "Chuck Norris's Wrath"
    print(
        f"TOURNAMENT CREATED! \nOpen for registration \n{tournament_name} \n{venue} \n{game} \nq.Quit"
    )


def my_tournaments_menu():
    my_created_tournaments = [
        "Chuck Norris Open",
        "Paris Major",
        "Steinar's Cock Wrestling",
    ]
    print(
        f"TOURNAMENTS YOU HAVE CREATED! \n{my_created_tournaments} \nb.Back \nq. Quit"
    )  # TODO Delete tournament?


# Eftir að klára og skoða betur
def create_schedule():
    print("Choose timeslot: ")


def create_match():
    print("Select two available teams to face off! \nAvailable Teams:")


def register_results():
    print("Enter results of matches that have been finished: ")


def update_schedule():
    print("Update your tournaments schedule: ")

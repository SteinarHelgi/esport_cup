#First menu and login menus
def print_login_menu(): #Login menu
    print("__________LOGIN_________")
    print("1. continue as user \n2. Login as Team Captain \n3. Login as Organiser")
    
def login_credentials_menu(): #logging in as organiser
    username = "Chuck Norris"
    password = "Pepsi Max"
    print(f"Username: {username} \nPassword: {password} \nConfirm(Y/N)? ")

def print_user_main_menu(): #Option menu for user
    print("__SELECT AN OPTION__")
    print("1. Teams \n2. Tournaments \nq. Quit")


def print_team_captain_main_menu(): #Option menu for team captain
    print("__SELECT AN OPTION__")
    print("1. Teams \n2. Tournaments \n3. My Team \n4. My Tournaments \nq. Quit")


def print_organiser_main_menu():#option menu for organiser
    print("__SELECT AN OPTION__")
    print("1. Teams \n2. Tournaments \n3. Create Tournaments \n4. My Tournaments \nq. Quit")

#Teams and Tournaments menu that all users can use
def print_team_menu(): #Prints a list of teams with the corresponding information
    list_of_teams = 0
    return list_of_teams #with clubs
    #TODO add options for this menu

def print_tournaments_menu(): #Menu for looking at tournaments
    print("1. Ongoing Tournaments \n2. Upcoming Tournaments \n3. Past Tournaments \nb. Back \nq.Quit")
    
#Team captain menus
def print_my_team_menu(): #Options for my team
    club = 0
    team_name = 0
    link = 0
    logo = 0
    captain = 0
    print (f"{club} {team_name} {link} {logo} {captain}")
    print ("1. Add team to club \n2. Roster \n3. Edit team info \nb. Back \nq. Quit")

def add_team_to_club():
    list_of_clubs = 0
    print(f"{list_of_clubs}")

def tournaments_for_my_team(): #Tournaments that team is registered to
    tournaments_registered = 0
    return tournaments_registered


def register_for_tournament(): #option to register for available tournaments
    available_tournaments = 0
    print(f"{available_tournaments}")
    #TODO options for list of tournaments

def edit_team_info():
    print("1. Club \n2. Website/Social Media \n3. Logo \n4. Team Captain \nb. Back \nq. Quit")

def roster_menu():
    print("1. Add player to team \n2. Player Information \n3. Remove player from team \nb. Back \nq. Quit")




class SelectionMenus():
    def print_login_menu(self): #Login menu
        print("__________LOGIN_________")
        print("1. continue as user \n2. Login as Team Captain \n3. Login as Organiser")
        

    def print_user_menu(self): #Option menu for user
        print("__SELECT AN OPTION__")
        print("1. Teams \n2. Tournaments \nq. Quit")


    def print_team_captain_menu(self): #Option menu for team captain
        print("__SELECT AN OPTION__")
        print("1. Teams \n2. Tournaments \n3. My Team \n4. My Tournaments \nq. Quit")


    def print_organiser_menu(self):#option menu for organiser
        print("__SELECT AN OPTION__")
        print("1. Teams \n2. Tournaments \n3. Create Tournaments \n4. My Tournaments \nq. Quit")
    
    def print_team_menu(self): #Prints a list of teams with the corresponding information
        list_of_teams = 0
        return list_of_teams
        #TODO add options for this menu
    
    def print_tournament_menu(self): #Menu for looking at tournaments
        print("1. Ongoing Tournaments \n2. Upcoming Tournaments \n3. Past Tournaments \nb. Back \nq.Quit")
        valid_options = ["1", "2", "3", "b", "q"]
        option = "?"
        for option in valid_options:
            if option == "1":
                return #ongoing_tournaments
            if option == "2":
                return #upcoming_tournaments
            if option == "3":
                return #Past_tournaments
            if option == "b":
                return #back_button
            if option == "q":
                return #quit
        
        
    def print_my_team_menu(self): #Options for my team
        club = 0
        team_name = 0
        link = 0
        logo = 0
        captain = 0
        print (f"{club} {team_name} {link} {logo} {captain}")
        print ("1. Add team to club \n2. Roster \n3. Edit team info \nb. Back \nq. Quit")
        valid_options = ["1", "2", "3", "b", "q"]
        option = "?"
        for option in valid_options:
            if option == "1":
                return #add_team_to_club
            if option == "2":
                return #roster_menu
            if option == "3":
                return #edit_team_info_menu
            if option == "b":
                return #back_button
            if option == "q":
                return #quit
        
        
        
    def tournaments_for_my_team(self):
        tournaments_registered = 0
        return tournaments_registered
    
    def register_for_tournament(self):
        available_tournaments = 0
        print(f"{available_tournaments}")


            
    



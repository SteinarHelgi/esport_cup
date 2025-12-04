from LL.api_ll import APILL
from UI.Menus import tournament_created_menu


class OrganiserUI:
    def __init__(self, APILL: APILL, menu_manager) -> None:
        self.APILL = APILL
        self.menu_manager = menu_manager

    def show_create_tournament(self): #Creates tournaments with options to quit or back anywhere in the process
        print("Fill in the required info or b.Back or q.Quit")
        name_of_tournament = input("Name: ")
        if name_of_tournament == "b":
            return "ORGANISER_MENU"
        if name_of_tournament == "q":
            return "QUIT"
        start_date_of_tournament = input("Start date(Year-MOnth-Day): ")
        if start_date_of_tournament == "b":
            return "ORGANISER_MENU"
        if start_date_of_tournament == "q":
            return "QUIT"
        end_date_of_tournamnet = input("End date(Year-Month-Day): ")
        if end_date_of_tournamnet == "b":
            return "ORGANISER_MENU"
        if end_date_of_tournamnet == "q":
            return "QUIT"
        amount_of_servers = input("Number of servers: ")
        if amount_of_servers == "b":
            return "ORGANISER_MENU"
        if amount_of_servers == "q":
            return "QUIT"
        while not amount_of_servers.isdigit():
            print("Needs to be a number!")
            amount_of_servers = input("Number of servers: ")
        venue = input("Venue: ")
        if venue == "b":
            return "ORGANISER_MENU"
        if venue == "q":
            return "QUIT"
        double_elimination = input("Double elimination(Y/N): ").lower()
        if double_elimination == "b":
            return "ORGANISER_MENU"
        if double_elimination == "q":
            return "QUIT"
        if double_elimination != "Y" and double_elimination != "N":
            print("Invalid input, valid inputs are: Y, N, B, Q")
            double_elimination = input("Double elimination(Y/N): ")
        if double_elimination == "b":
            return "ORGANISER_MENU"
        if double_elimination == "q":
            return "QUIT"
        game_for_tournament = input("Game: ")
        if game_for_tournament == "b":
            return "ORGANISER_MENU"
        if game_for_tournament == "q":
            return "QUIT"
        new_contact_person = self.create_contact_person_menu() #Calls the create contact person function so that it adds that person to the created tournament
        print("b. Back \nq. Quit")
        #TODO setja inn tournament created menuið
        new_tournament = [name_of_tournament, start_date_of_tournament, end_date_of_tournamnet, int(amount_of_servers), venue, double_elimination, game_for_tournament]
        if self.APILL.create_tournament(new_tournament) == "valid":
            val = self.tournament_created(new_tournament)
            return "ORGANISER MENU"
        else:
            print("Tournament could not be created, contact developer")
            return "ORGANISER MENU"
        

    def create_contact_person_menu(self): #Creates the contact person with options to back or quit anywhere in the process
        print("Fill in contact person info or 'b' to Back and 'q' to Quit")
        new_contact_person_name = input("Name: ")
        if new_contact_person_name == "b":
            return "ORGANISER_MENU"
        if new_contact_person_name == "q":
            return "QUIT"
        new_contact_person_email = input("Email: ")
        if new_contact_person_email == "b":
            return "ORGANISER_MENU"
        if new_contact_person_email == "q":
            return "QUIT"
        new_contact_person_phone_nmbr = input("Phone number: ")
        if new_contact_person_phone_nmbr == "b":
            return "ORGANISER_MENU"
        if new_contact_person_phone_nmbr == "q":
            return "QUIT"
        confirmation = input("Confirm(Y/N): ")
        if confirmation == "Y":
            return [new_contact_person_name, new_contact_person_email, new_contact_person_phone_nmbr]
        if confirmation =="N":
            return "CREATE_TOURNAMENT_MENU"
    
    def tournament_created(self, tournament):
        tournament_name = tournament[0]
        venue = tournament[4]
        game = tournament[6]
        f"TOURNAMENT CREATED! \nOpen for registration \n{tournament_name} \n{venue} \n{game}"


    def show_my_tournament(self):
        # TODO
        pass

    def show_create_schedule(self):
        # TODO
        pass

    def show_update_schedule(self):
        # TODO
        pass

    def show_create_match(self):
        # TODO
        pass

    def show_register_results(self):
        # TODO
        pass

    def show_delete_tournament(self):
        # TODO
        pass

    def show_give_points(self):
        # TODO
        pass

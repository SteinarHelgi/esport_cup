from datetime import datetime
from LL.api_ll import APILL
from Models.match import Match
from Models.tournament import Tournament
from UI.Menus import tournament_created_menu
from UI.functions import format_tournament_table


class OrganiserUI:
    def __init__(self, APILL: APILL, menu_manager) -> None:
        self.APILL = APILL
        self.menu_manager = menu_manager

    def show_create_tournament(
        self,
    ):  # Creates tournaments with options to quit or back anywhere in the process
        print("Fill in the required info or b.Back or q.Quit")
        name_of_tournament = input("Name: ")
        if name_of_tournament.lower() == "b":
            return "ORGANISER_MENU"
        if name_of_tournament.lower() == "q":
            return "QUIT"
        start_date_of_tournament = input("Start date(Year-MOnth-Day): ")
        if start_date_of_tournament.lower() == "b":
            return "ORGANISER_MENU"
        if start_date_of_tournament.lower() == "q":
            return "QUIT"
        end_date_of_tournamnet = input("End date(Year-Month-Day): ")
        if end_date_of_tournamnet.lower() == "b":
            return "ORGANISER_MENU"
        if end_date_of_tournamnet.lower() == "q":
            return "QUIT"
        amount_of_servers = input("Number of servers: ")
        if amount_of_servers.lower() == "b":
            return "ORGANISER_MENU"
        if amount_of_servers.lower() == "q":
            return "QUIT"
        while not amount_of_servers.isdigit():
            print("Needs to be a number!")
            amount_of_servers = input("Number of servers: ")
        venue = input("Venue: ")
        if venue.lower() == "b":
            return "ORGANISER_MENU"
        if venue.lower() == "q":
            return "QUIT"
        double_elimination = input("Double elimination(Y/N): ")
        if double_elimination.lower() == "b":
            return "ORGANISER_MENU"
        if double_elimination.lower() == "q":
            return "QUIT"
        if double_elimination.lower() != "y" and double_elimination != "n":
            print("Invalid input, valid inputs are: Y, N, B, Q")
            double_elimination = input("Double elimination(Y/N): ")
        if double_elimination.lower() == "b":
            return "ORGANISER_MENU"
        if double_elimination.lower() == "q":
            return "QUIT"
        game_for_tournament = input("Game: ")
        if game_for_tournament.lower() == "b":
            return "ORGANISER_MENU"
        if game_for_tournament.lower() == "q":
            return "QUIT"
        new_contact_person = self.create_contact_person_menu()  # Calls the create contact person function so that it adds that person to the created tournament
        print("b. Back \nq. Quit")
        # TODO setja inn tournament created menuið
        if new_contact_person:
            new_tournament = Tournament(
                name_of_tournament,
                datetime.fromisoformat(start_date_of_tournament),
                datetime.fromisoformat(end_date_of_tournamnet),
                venue,
                game_for_tournament,
                amount_of_servers,
                new_contact_person[0],
            )
            

            if self.APILL.create_tournament(new_tournament):
                #val = self.tournament_created(new_tournament)
                print(tournament_created_menu((new_tournament)))
                enter_for_ok = input("Enter for ok or q to quit")
                if enter_for_ok == "q":
                    return "QUIT"
                else:
                    return "ORGANISER_MENU"

            else:
                print("Tournament could not be created, contact developer")
                enter_for_ok = input("Enter for ok or q to quit")
                if enter_for_ok == "q":
                    return "QUIT"
                return "ORGANISER_MENU"
                
        return "ORGANISER_MENU"

    def create_contact_person_menu(
        self,
    ):  # Creates the contact person with options to back or quit anywhere in the process
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
        confirmation = input("Confirm(Y): ")
        if confirmation.lower() == "y":
            returnlist = [
                new_contact_person_name,
                new_contact_person_email,
                new_contact_person_phone_nmbr,
            ]
            return returnlist

    def tournament_created(self, tournament: Tournament) -> str:
        tournament_name = tournament.name
        venue = tournament.venue
        game = tournament.game_id
        return f"TOURNAMENT CREATED! \nOpen for registration \n{tournament_name} \n{venue} \n{game}"

    def show_my_tournaments(self):
        # Shows all of the upcoming tournamnets for the organiser to look at
        """Finds all upcoming tournaments and prompts for choice"""
        tournaments = self.APILL.get_upcoming_tournaments()
        valid_choices = []
        for i in range(len(tournaments)):
            stringI = str(i + 1)
            valid_choices.append(stringI)
        print("MY_TOURNAMENTS_ORG")
        print(format_tournament_table(tournaments))

        print("Select a tournament with their respected id or: \nb. Back \nq. Quit")
        choice: str = self.menu_manager.prompt_choice(valid_choices + ["b", "q"])
        print()
        for element in valid_choices:
            if element == choice:
                return self.show_tournament_view(tournaments[int(element) - 1])

        if choice == "b":
            return "ORGANISER_MENU"
        if choice == "q":
            return "QUIT"

        return ""

    def show_tournament_view(self, tournament: Tournament):
        """takes in a tournament name and shows the menu for the tournament"""

        if tournament:
            print(
                f"{tournament.name.upper()}  |  {tournament.start_date} -- {tournament.end_date} "
            )
            print("--------------------")
            print(" ")
            for match in tournament.matches:
                print(f"    Matches: {match}")
            print("1. Add match")
            print("")
            print("b. Back")
            print("q. Quit")

        choice: str = self.menu_manager.prompt_choice(["1", "2", "b", "q"])
        if choice == "1":
            return self.show_create_match(tournament)

        if choice == "b":
            return "MY_TOURNAMENTS_ORG"
        if choice == "q":
            return "QUIT"

    def show_create_match(self, tournament: Tournament):
        prompts = [
            "Round: ",
            "Team 1: ",
            "Team 2: ",
            "Date YYYY-MM-DD: ",
            "Time HH-MM-SS: ",
        ]
        user_inputs = []
        for prompt in prompts:
            current_input = input(prompt)
            user_inputs.append(current_input)
        # match_id,*tournament_id,*round,match_number,*team_a_name,*team_b_name,*match_date,*match_time,server_id,score_a,score_b,winner_team_name,completed
        match = Match(
            tournament.id,
            user_inputs[0],
            user_inputs[1],
            user_inputs[2],
            user_inputs[3],
            user_inputs[4],
        )
        self.APILL.create_match(match)

        # Get information about matc
        print(*user_inputs)

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

from datetime import datetime
from os import name
from tracemalloc import start
from LL.api_ll import APILL
from Models import game
from Models.contact_person import ContactPerson
from Models.models import Match, Player, Team, Tournament
from UI.functions import format_player_list, format_team_list, format_tournament_table
from UI.ui_functions import refresh_logo
from LL.validators_ll import (Errors,
    validate_match_date,
    validate_match_time,
    validate_phone_number,
    validate_player_email,
    validate_player_name,
    validate_tournament_double_elimination,
    validate_tournament_end_date,
    validate_tournament_game,
    validate_tournament_name,
    validate_tournament_servers,
    validate_tournament_start_date,
    validate_tournament_venue)



class OrganiserUI:
    """UI functions for organiser"""

    def __init__(self, APILL: APILL, menu_manager) -> None:
        self.APILL = APILL
        self.menu_manager = menu_manager
        self.team_to_view: Team

    def show_create_tournament(self):
        """Creates tournaments with options to quit or back anywhere in the process and shows the confirmation of creation"""
        print("Fill in the required info or b.Back or q.Quit")

        name_of_tournament = input("Tournament name: ")
        if name_of_tournament.lower() == "b":
            return "ORGANISER_MENU"
        if name_of_tournament.lower() == "q":
            return "QUIT"
        while validate_tournament_name(name_of_tournament) != Errors.OK:
            error = validate_tournament_name(name_of_tournament)
            if error == Errors.TOURNAMENT_NAME_LENGTH:
                print("Tournament name needs to be atleast two letters")
            if error == Errors.TOURNAMENT_NAME_LENGTH_TOO_LONG:
                print("Tournament's name is too long")
            name_of_tournament = input("Tournament name: ").strip()

        start_date_of_tournament = input("Start date(Year-Month-Day): ").strip()
        if start_date_of_tournament.lower() == "b":
            return "ORGANISER_MENU"
        if start_date_of_tournament.lower() == "q":
            return "QUIT"
        while validate_tournament_start_date(start_date_of_tournament) != Errors.OK:
            error = validate_tournament_start_date(start_date_of_tournament)
            if error == Errors.DATE_FORMAT_NOT_VALID:
                print("Invalid format. Format is 0000-00-00.")
            if error == Errors.START_DATE_BEFORE_TODAY:
                print(
                    "The start date you entered has already passed, please input a different date."
                )
            start_date_of_tournament = input("Start date(Year-Month-Day): ").strip()

        end_date_of_tournamnet = input("End date(Year-Month-Day): ").strip()
        if end_date_of_tournamnet.lower() == "b":
            return "ORGANISER_MENU"
        if end_date_of_tournamnet.lower() == "q":
            return "QUIT"
        while (
            validate_tournament_end_date(
                start_date_of_tournament, end_date_of_tournamnet
            )
            != Errors.OK
        ):
            error = validate_tournament_end_date(
                start_date_of_tournament, end_date_of_tournamnet
            )
            if error == Errors.DATE_FORMAT_NOT_VALID:
                print("Invalid format. Format is 0000-00-00.")
            if error == Errors.END_DATE_BEFORE_START:
                print(
                    "The date you have input is before or on the start date you input. Please input a date that is after the start date."
                )
            end_date_of_tournamnet = input("End date(Year-Month-Day): ").strip()

        amount_of_servers = input("Number of servers: ").strip()
        if amount_of_servers.lower() == "b":
            return "ORGANISER_MENU"
        if amount_of_servers.lower() == "q":
            return "QUIT"
        while validate_tournament_servers(amount_of_servers) != Errors.OK:
            error = validate_tournament_servers(amount_of_servers)
            if error == Errors.SERVER_NOT_NUMBER:
                print("Server amount has to be a number.")
            if error == Errors.SERVER_LESS_THAN_0:
                print("Server amount cannot be less than 0.")
            amount_of_servers = input("Number of servers: ").strip()

        venue = input("Venue: ").strip()
        if venue.lower() == "b":
            return "ORGANISER_MENU"
        if venue.lower() == "q":
            return "QUIT"
        while validate_tournament_venue(venue) != Errors.OK:
            error = validate_tournament_venue(venue)
            if error == Errors.VENUE_INCLUDE_NUMBERS:
                print("Invalid input, cannot be all numnbers.")
            venue = input("Venue: ").strip()

        double_elimination = input("Double elimination(Y/N): ").strip()
        if double_elimination.lower() == "b":
            return "ORGANISER_MENU"
        if double_elimination.lower() == "q":
            return "QUIT"
        while validate_tournament_double_elimination(double_elimination) != Errors.OK:
            error = validate_tournament_double_elimination(double_elimination)
            if error == Errors.NOT_Y_OR_N:
                print("Invalid input, confirm with Y or N")
            double_elimination = input("Double elimination(Y/N): ").strip()

        games = self.APILL.get_all_games()
        print("Valid games are:", *[f"{game}," for game in games[:-1]], games[-1])
        game_for_tournament = input("Game: ").strip()
        if game_for_tournament.lower() == "b":
            return "ORGANISER_MENU"
        if game_for_tournament.lower() == "q":
            return "QUIT"
        while validate_tournament_game(game_for_tournament, games) != Errors.OK:
            error = validate_tournament_game(game_for_tournament, games)
            if error == Errors.GAME_NOT_VALID:
                print(
                    "You have input an invalid game, select a game from the list provided"
                )
                print("Valid games are:", *games)
                game_for_tournament = input("Game: ").strip()

        print("Fill in contact person info or 'b' to Back and 'q' to Quit")

        new_contact_person_name = input("Name: ").strip()
        if new_contact_person_name == "b":
            return "ORGANISER_MENU"
        if new_contact_person_name == "q":
            return "QUIT"
        while validate_player_name(new_contact_person_name) != Errors.OK:
            error = validate_player_name(new_contact_person_name)
            if error == Errors.EMPTY:
                print("Name cannot be empty")
            if error == Errors.NAME_INCLUDE_NUMBERS:
                print("Name cannot include numbers")
            new_contact_person_name = input("Name: ").strip()

        new_contact_person_email = input("Email: ").strip()
        if new_contact_person_email == "b":
            return "ORGANISER_MENU"
        if new_contact_person_email == "q":
            return "QUIT"
        while validate_player_email(new_contact_person_email) != Errors.OK:
            error = validate_player_email(new_contact_person_email)
            if error == Errors.EMPTY:
                print("Contact person email address cannot be empty.")
            if error == Errors.EMAIL_NOT_CONTAINING_AT:
                print("Email has to include an '@': example@example.com")
            new_contact_person_email = input("Email: ").strip()

        new_contact_person_phone_nmbr = input("Phone number: ").strip()
        if new_contact_person_phone_nmbr == "b":
            return "ORGANISER_MENU"
        if new_contact_person_phone_nmbr == "q":
            return "QUIT"
        while validate_phone_number(new_contact_person_phone_nmbr) != Errors.OK:
            error = validate_phone_number(new_contact_person_phone_nmbr)
            if error == Errors.EMPTY:
                print("Phone number cannot be empty.")
            if error == Errors.NUMBER_HAS_CHARACTERS:
                print("Phone number cannot have characters, only digits.")
            if error == Errors.NUMBER_NOT_CORRECT_LENGTH:
                print("Phone number has to be 7 digits long.")
            new_contact_person_phone_nmbr = input("Phone number: ").strip()
        # Try and except for contact person phone number validation
        confirmation = input("Confirm(Y): ").strip()
        if confirmation.lower() != "y":
            return "ORGANISER_MENU"

        print("b. Back \nq. Quit")

        new_tournament = Tournament(
            name_of_tournament,
            datetime.fromisoformat(start_date_of_tournament),
            datetime.fromisoformat(end_date_of_tournamnet),
            venue,
            game_for_tournament,
            amount_of_servers,
            new_contact_person_name,
        )
        tournament = self.APILL.create_tournament(new_tournament)

        if tournament:
            new_contact_person = ContactPerson(
                new_contact_person_name,
                new_contact_person_email,
                new_contact_person_phone_nmbr,
                tournament.id,
            )

            contact_person = self.APILL.create_contact_person(new_contact_person)

            print(self.tournament_created((new_tournament)))
            enter_for_ok = input("Press enter for OK or q to quit")
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

    def tournament_created(self, tournament: Tournament) -> str:
        """Menu that confirms that a tournament has been created"""
        tournament_name = tournament.name
        venue = tournament.venue
        game = tournament.game_id
        return f"TOURNAMENT CREATED! \nOpen for registration \n{tournament_name} \n{venue} \n{game}"

    def show_my_tournaments(self):
        """Finds all upcoming tournaments and prompts for choice"""
        tournaments = self.APILL.get_upcoming_tournaments()
        valid_choices = []

        for i, tournament in enumerate(tournaments):
            string_i = str(i + 1)
            valid_choices.append(string_i)

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

        refresh_logo()
        w_team = 26
        w_date = 12
        w_time = 12
        w_round = 8
        w_vs = 4
        w_completed = 10
        line_length = w_team + w_team + w_date + w_time + w_round + w_vs + w_completed
        updated_tournament = self.APILL.get_tournament_by_id(tournament.id)

        if updated_tournament:
            tournament = updated_tournament
            print(
                f"{tournament.name.upper()}  |  {tournament.start_date} -- {tournament.end_date} "
            )
            print("Matches: ")
            print(" ")
            header = (
                "   "
                f"{'Team 1':<{w_team}}"
                f"{'vs':^{w_vs}}"
                f"{'Team 2':>{w_team}} "
                f"{'Date':^{w_date}}"
                f"{'Time':^{w_time}}"
                f"{'Round':^{w_round}}"
                f"{'Completed':^{w_completed}}"
                f"{'Winner':>{w_team}}"
            )
            print("-" * len(header))
            print(header)
            print("-" * len(header))
            valid_choices = []

            for counter, match in enumerate(tournament.matches):
                valid_choices.append(str(counter + 1))
                print(f"{counter}. {match}")
            print(" ")
            print("c. Create new match \nd. Delete tournament \nb. Back \nq. Quit")
            choice: str = self.menu_manager.prompt_choice(
                valid_choices + ["c","d", "b", "q"]
            )
            if choice in valid_choices:
                return self.show_register_results(tournament.matches[int(choice) - 1])

            teams_in_tournament = self.APILL.get_teams_in_tournament(tournament)
            if choice == "c":
                if teams_in_tournament:
                    return self.show_create_match(tournament)
                else:
                    print("No teams have registered for this tournament")
                    print("")
                    print("b. Back\nq. Quit")
                    choice: str = self.menu_manager.prompt_choice(["b", "q"])
                    if choice == "b":
                        return "MY_TOURNAMENTS_ORG"
                    if choice == "q":
                        return "QUIT"
            if choice == "d":
                return self.show_delete_tournament(tournament)


            if choice == "b":
                return "MY_TOURNAMENTS_ORG"
            if choice == "q":
                return "QUIT"

    def show_create_match(self, tournament: Tournament):
        """Function for creating matches as an organiser"""

        if len(tournament.matches) < 8:
            round = "R16"
        elif len(tournament.matches) < 12:
            round = "QF"
        elif len(tournament.matches) < 14:
            round = "SF"
        else:
            round = "Final"
        teams_not_in_round = self.APILL.get_teams_not_in_round(tournament)
        print("Which teams are competing in this match?")
        print("")
        valid_choices = []
        teams_not_in_round[0]._print_header()
        teams_not_in_round[0]._print_divider_line()
        for counter, team in enumerate(teams_not_in_round):
            team.format_row(counter)
            valid_choices.append(str(counter))
            team._print_divider_line()
        print("")
        print("Round type ", round)
        print("Select team 1:", end="")

        choice: str = self.menu_manager.prompt_choice(valid_choices)
        team1 = teams_not_in_round[int(choice)]
        if choice in valid_choices:
            print(team1.name, "as Team 1")

        print("Select team 2:", end="")
        choice: str = self.menu_manager.prompt_choice(valid_choices)
        team2 = teams_not_in_round[int(choice)]
        if choice in valid_choices:
            print(team2.name, "as Team 2")

        date = input("Date (YYYY-MM-DD): ")
        while (
            validate_match_date(date, tournament.start_date, tournament.end_date)
            != Errors.OK
        ):
            print("Date not in tournament")
            date = input("Date (YYYY-MM-DD): ")

        time = input("Time (HH:MM): ")
        error = validate_match_time(time)
        timeslots = [
            "08:00",
            "10:00",
            "12:00",
            "14:00",
            "16:00",
            "18:00",
            "20:00",
        ]

        while error != Errors.OK:
            if error == Errors.TIME_NOT_IN_TIMESLOT:
                print("Choose a time in time slot:")
                print("Timeslots : ", *timeslots)
            time = input("Time (HH:MM): ")
            error = validate_match_time(time)

        match = Match(tournament.id, round, team1.name, team2.name, date, time)

        print("Confirm ? (Y/N)")
        choice: str = self.menu_manager.prompt_choice(["y", "n"])
        if choice == "y":
            match = self.APILL.create_match(match)
        if choice == "n":
            pass

        return self.show_tournament_view(tournament)

    def show_register_results(self, match: Match):
        """Registering results of a match, chooses a winner and marks match as completed"""
        print(f"Registering result for match: {match.team_a_name} vs {match.team_b_name}")
        print("Which team won the match?")
        print(f"1. {match.team_a_name}")
        print(f"2. {match.team_b_name}")
        
        winner = input("1 or 2, b to back and q to quit: ")

        if winner == "b":
            return "MY_TOURNAMENTS_ORG"
        if winner == "q":
            return "QUIT"
        
        # Determine winner name based on selection
        if winner == "1":
            winner_name = match.team_a_name
        elif winner == "2":
            winner_name = match.team_b_name
        else:
            print("Invalid input.")
            return

        # Update local object
        match.set_winner(winner_name, "TRUE")
        
        # Update Database via API (No scores involved)
        self.APILL.register_match_result(match.match_id, winner_name, "TRUE")
        
        print(f"{winner_name} has been set as the winner of this match.")

        # Navigation
        choice = self.menu_manager.prompt_choice(["b", "q"])
        if choice == "b":
            return "MY_TOURNAMENTS_ORG"
        if choice == "q":
            return "QUIT"


    def show_delete_tournament(self,tournament):
        print(f"Are you sure you wish to delete {tournament.name}")
        confirm = input("Confirm(Y/N): ")
        if confirm.lower() == "y":
            self.APILL.delete_tournament(tournament.id)
            print(f"{tournament.name} has been deleted")
            enter_to_leave = input("Enter to exit or q to Quit.")
            if enter_to_leave == "q":
                return "QUIT"
            else:
                return "MY_TOURNAMENTS_ORG"



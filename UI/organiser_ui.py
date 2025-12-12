from datetime import datetime
from LL.api_ll import APILL
from Models.models import Match, Team, Tournament, ContactPerson
from UI.functions import format_tournament_table
from UI.ui_functions import (
    refresh_logo,
    set_system_color_gold,
    set_system_color_red,
)
from LL.validators_ll import Errors


class OrganiserUI:
    """UI functions for organiser"""

    def __init__(self, APILL: APILL, menu_manager) -> None:
        self.APILL = APILL
        self.menu_manager = menu_manager
        self.team_to_view: Team

    def show_create_tournament(self):
        """Creates tournaments with options to quit or back anywhere in the process
        and shows the confirmation of creation"""
        print("Fill in the required info or b.Back or q.Quit")

        name_of_tournament = input("Tournament name: ")
        if name_of_tournament.lower() == "b":
            return "ORGANISER_MENU"
        if name_of_tournament.lower() == "q":
            return "QUIT"
        while self.APILL.validate_tournament_name(name_of_tournament) != Errors.OK:
            error = self.APILL.validate_tournament_name(name_of_tournament)
            if error == Errors.TOURNAMENT_NAME_LENGTH or error == Errors.EMPTY:
                print("Tournament name needs to be atleast two letters")
            if error == Errors.TOURNAMENT_NAME_LENGTH_TOO_LONG:
                print("Tournament's name is too long")
            if error == Errors.CONTAINS_UNWANTED_CHAR:
                print(
                    "Cannot contain: Comma, Quotation Marks or Semi Colon, nice try dummy."
                )
            name_of_tournament = input("Tournament name: ").strip()

        start_date_of_tournament = input("Start date(Year-Month-Day): ").strip()
        if start_date_of_tournament.lower() == "b":
            return "ORGANISER_MENU"
        if start_date_of_tournament.lower() == "q":
            return "QUIT"
        while (
            self.APILL.validate_tournament_start_date(start_date_of_tournament)
            != Errors.OK
        ):
            error = self.APILL.validate_tournament_start_date(start_date_of_tournament)
            if error == Errors.DATE_FORMAT_NOT_VALID:
                print("Invalid format. Format is YYYY-MM-DD.")
            if error == Errors.START_DATE_BEFORE_TODAY:
                print(
                    "The start date you entered has already passed, please input a different date."
                )
            if error == Errors.CONTAINS_UNWANTED_CHAR:
                print(
                    "Cannot contain: Comma, Quotation Marks or Semi Colon, nice try dummy."
                )
            start_date_of_tournament = input("Start date(Year-Month-Day): ").strip()

        end_date_of_tournamnet = input("End date(Year-Month-Day): ").strip()
        if end_date_of_tournamnet.lower() == "b":
            return "ORGANISER_MENU"
        if end_date_of_tournamnet.lower() == "q":
            return "QUIT"
        while (
            self.APILL.validate_tournament_end_date(
                start_date_of_tournament, end_date_of_tournamnet
            )
            != Errors.OK
        ):
            error = self.APILL.validate_tournament_end_date(
                start_date_of_tournament, end_date_of_tournamnet
            )
            if error == Errors.DATE_FORMAT_NOT_VALID:
                print("Invalid format. Format is YYYY-MM-DD.")
            if error == Errors.END_DATE_BEFORE_START:
                print(
                    "The date you have input is before or on the start date you input. Please input a date that is after the start date."
                )
            if error == Errors.CONTAINS_UNWANTED_CHAR:
                print(
                    "Cannot contain: Comma, Quotation Marks or Semi Colon, nice try dummy."
                )

            end_date_of_tournamnet = input("End date(Year-Month-Day): ").strip()

        amount_of_servers = input("Number of servers: ").strip()
        if amount_of_servers.lower() == "b":
            return "ORGANISER_MENU"
        if amount_of_servers.lower() == "q":
            return "QUIT"
        while self.APILL.validate_tournament_servers(amount_of_servers) != Errors.OK:
            error = self.APILL.validate_tournament_servers(amount_of_servers)
            if error == Errors.SERVER_NOT_NUMBER:
                print("Server amount has to be a number.")
            if error == Errors.SERVER_LESS_THAN_0:
                print("Server amount cannot be less than 0.")
            if error == Errors.CONTAINS_UNWANTED_CHAR:
                print(
                    "Cannot contain: Comma, Quotation Marks or Semi Colon, nice try dummy."
                )
            amount_of_servers = input("Number of servers: ").strip()

        venue = input("Venue: ").strip()
        if venue.lower() == "b":
            return "ORGANISER_MENU"
        if venue.lower() == "q":
            return "QUIT"
        while self.APILL.validate_tournament_venue(venue) != Errors.OK:
            error = self.APILL.validate_tournament_venue(venue)
            if error == Errors.VENUE_INCLUDE_NUMBERS:
                print("Invalid input, cannot be all numnbers.")
            if error == Errors.EMPTY:
                print("Venue cannot be empty")
            if error == Errors.CONTAINS_UNWANTED_CHAR:
                print(
                    "Cannot contain: Comma, Quotation Marks or Semi Colon, nice try dummy."
                )
            venue = input("Venue: ").strip()

        games = self.APILL.get_all_games()
        print("Valid games are:", *[f"{game}," for game in games[:-1]], games[-1])
        game_for_tournament = input("Game: ").strip()
        if game_for_tournament.lower() == "b":
            return "ORGANISER_MENU"
        if game_for_tournament.lower() == "q":
            return "QUIT"
        while (
            self.APILL.validate_tournament_game(game_for_tournament, games) != Errors.OK
        ):
            error = self.APILL.validate_tournament_game(game_for_tournament, games)
            if error == Errors.GAME_NOT_VALID:
                print(
                    "You have input an invalid game, input a game from the list provided"
                )
                print(
                    "Valid games are:", *[f"{game}," for game in games[:-1]], games[-1]
                )
            if error == Errors.EMPTY:
                print("Game cannot be empty.")
            if error == Errors.CONTAINS_UNWANTED_CHAR:
                print(
                    "Cannot contain: Comma, Quotation Marks or Semi Colon, nice try dummy."
                )
            game_for_tournament = input("Game: ").strip()

        print("Fill in contact person info or 'b' to Back and 'q' to Quit")

        new_contact_person_name = input("Name: ").strip()
        if new_contact_person_name == "b":
            return "ORGANISER_MENU"
        if new_contact_person_name == "q":
            return "QUIT"
        while self.APILL.validate_player_name(new_contact_person_name) != Errors.OK:
            error = self.APILL.validate_player_name(new_contact_person_name)
            if error == Errors.EMPTY:
                print("Name cannot be empty")
            if error == Errors.NAME_INCLUDE_NUMBERS:
                print("Name cannot include numbers")
            if error == Errors.NAME_INCLUDES_PERIOD:
                print("Name cannot contain periods.")
            if error == Errors.CONTAINS_UNWANTED_CHAR:
                print(
                    "Cannot contain: Comma, Quotation Marks or Semi Colon, nice try dummy."
                )
            new_contact_person_name = input("Name: ").strip()

        new_contact_person_email = input("Email: ").strip()
        if new_contact_person_email == "b":
            return "ORGANISER_MENU"
        if new_contact_person_email == "q":
            return "QUIT"
        while self.APILL.validate_player_email(new_contact_person_email) != Errors.OK:
            error = self.APILL.validate_player_email(new_contact_person_email)
            if error == Errors.EMPTY:
                print("Contact person email address cannot be empty.")
            if error == Errors.EMAIL_NOT_VALID:
                print("Invalid Email.")
            if error == Errors.HANDLE_CONTAINS_SPACE:
                print("Email cannot include spaces.")
            if error == Errors.NEEDS_PERIOD:
                print("Email has to include periods.")
            if error == Errors.CONSECUTIVE_PERIODS:
                print("Email cannot contain consecutive periods.")
            if error == Errors.STARTS_OR_ENDS_WITH_PERIOD:
                print("Email cannot contain consecutive periods.")
            if error == Errors.EMAIL_NOT_CONTAINING_AT:
                print("Email has to include an '@': example@example.com")
            if error == Errors.CONTAINS_UNWANTED_CHAR:
                print(
                    "Cannot contain: Comma, Quotation Marks or Semi Colon, nice try dummy."
                )
            new_contact_person_email = input("Email: ").strip()

        new_contact_person_phone_nmbr = input("Phone number: ").strip()
        if new_contact_person_phone_nmbr == "b":
            return "ORGANISER_MENU"
        if new_contact_person_phone_nmbr == "q":
            return "QUIT"
        while (
            self.APILL.validate_phone_number(new_contact_person_phone_nmbr) != Errors.OK
        ):
            error = self.APILL.validate_phone_number(new_contact_person_phone_nmbr)
            if error == Errors.EMPTY:
                print("Phone number cannot be empty.")
            if error == Errors.NUMBER_HAS_CHARACTERS:
                print("Phone number cannot have characters, only digits.")
            if error == Errors.NUMBER_NOT_CORRECT_LENGTH:
                print("Phone number has to be 7 digits long.")
            if error == Errors.CONTAINS_UNWANTED_CHAR:
                print(
                    "Cannot contain: Comma, Quotation Marks or Semi Colon, nice try dummy."
                )
            new_contact_person_phone_nmbr = input("Phone number: ").strip()

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

            self.APILL.create_contact_person(new_contact_person)

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
        tournaments = self.APILL.get_all_tournaments()
        valid_choices = []

        for i in range(len(tournaments)):
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
        updated_tournament = self.APILL.get_tournament_by_id(tournament.id)

        if updated_tournament:
            tournament = updated_tournament
            print(
                f"{tournament.name.upper()}  |  {tournament.start_date} -- {tournament.end_date} "
            )
            print("Matches: ")
            if tournament.matches:
                header = tournament.matches[0].header()
                print("-" * len(header))
                print(header)
                print("-" * len(header))
            else:
                print("     No matches created for this tournament")
            valid_choices = []

            for counter, match in enumerate(tournament.matches):
                valid_choices.append(str(counter + 1))
                match.format_row(counter + 1)
            if tournament.matches:
                print(" ")
                print("Select a match by ID to register results.")
            print(" ")
            print(
                "c. Create new match \nr. Remove match \nd. Delete tournament \nb. Back \nq. Quit"
            )
            choice: str = self.menu_manager.prompt_choice(
                valid_choices + ["c", "r", "d", "b", "q"]
            )
            if choice in valid_choices:
                match = tournament.matches[int(choice) - 1]
                if match.completed == "False":
                    return self.show_register_results(match)
                else:
                    # print("Cannot update results for  matches")
                    print("Match results already registered")
                    input("Enter to return")
                    return "MY_TOURNAMENTS_ORG"

            if choice == "c":
                return self.show_create_match(tournament)
            if choice == "d":
                return self.show_delete_tournament(tournament)
            if choice == "r":
                if tournament.matches != []:
                    select_match_number = input("Enter match id: ")
                    if select_match_number.lower() == "b":
                        return "MY_TOURNAMENTS_ORG"
                    if select_match_number.lower() == "q":
                        return "QUIT"
                    if select_match_number in valid_choices:
                        # change to index
                        index = int(select_match_number) - 1
                        match_to_delete = tournament.matches[index]
                        print(
                            f"Selected match: {match_to_delete.team_a_name} vs {match_to_delete.team_b_name}"
                        )
                        confirm = input("Are you sure (Y/N)? ")
                        if confirm.lower() == "y":
                            if match_to_delete.completed == "False":
                                self.APILL.delete_match(match_to_delete)
                                print("Match has been deleted.")
                                input("Press Enter to continue")
                            else:
                                print("")
                                print("You cannot delete completed matches")
                                input("Press Enter to continue")

                            return "MY_TOURNAMENTS_ORG"
                        else:
                            return "MY_TOURNAMENTS_ORG"
                else:
                    input("There are no matches to delete, enter to exit.")
                    return "MY_TOURNAMENTS_ORG"

            if choice == "b":
                return "MY_TOURNAMENTS_ORG"
            if choice == "q":
                return "QUIT"

    def show_create_match(self, tournament: Tournament):
        """Function for creating matches as an organiser"""
        refresh_logo()
        print(
            f"{tournament.name.upper()}  |  {tournament.start_date} -- {tournament.end_date} "
        )

        if len(tournament.teams) < 16 and self.APILL.check_tournament_started(
            tournament
        ):
            print("Tournament did not have enough teams registered to start")
            print("")
            print("d. Delete tournament")
            print("b. Back\nq. Quit")
            choice: str = self.menu_manager.prompt_choice(["b", "q", "d"])

            if choice == "b":
                return "MY_TOURNAMENTS_ORG"
            if choice == "d":
                return self.show_delete_tournament(tournament)
            return "QUIT"

        elif len(tournament.teams) < 16:
            print("Not enough teams have registered")
            print("")
            print("b. Back\nq. Quit")
            choice: str = self.menu_manager.prompt_choice(["b", "q"])
            if choice == "b":
                return "MY_TOURNAMENTS_ORG"
            if choice == "d":
                return self.show_delete_tournament(tournament)
            return "QUIT"

        while True:
            if len(tournament.matches) < 8:
                round = "R16"
            elif len(tournament.matches) < 12:
                round = "QF"
            elif len(tournament.matches) < 14:
                round = "SF"
            elif len(tournament.matches) < 15:
                round = "Final"
            else:
                round = "NONE"
                print("Tournament is over!")
                print(self.print_trophy())
                print("b. Back\nq. Quit")
                choice: str = self.menu_manager.prompt_choice(["b", "q"])
                if choice == "b":
                    return "MY_TOURNAMENTS_ORG"
                if choice == "q":
                    return "QUIT"

            valid_choices = []
            available_teams = self.APILL.get_available_teams_for_next_round(
                tournament, round
            )
            print("Which teams are competing in this match?")
            print("")
            if len(tournament.matches) > 1:
                available_teams[0]._print_header()
                for index, team in enumerate(available_teams):
                    correct_index = index + 1
                    team.format_row(correct_index)
                    team._print_divider_line()
                    valid_choices.append(str(correct_index))
            else:
                print("No teams have registered for this tournament")
                print("b. Back\nq. Quit")
                choice: str = self.menu_manager.prompt_choice(["b", "q"])
                if choice == "b":
                    return "MY_TOURNAMENTS_ORG"
                if choice == "q":
                    return "QUIT"

            print("")

            print("Round type ", round)
            print("b. Back\nq. Quit")
            print("Select team 1:", end="")

            choice = self.menu_manager.prompt_choice(valid_choices + ["b", "q"])
            if choice == "b":
                return "MY_TOURNAMENTS_ORG"
            if choice == "q":
                return "QUIT"
            team1 = available_teams[int(choice) - 1]
            print(team1.name, "as Team 1")

            print("Select team 2:", end="")
            choice = self.menu_manager.prompt_choice(valid_choices + ["b", "q"])

            if choice == "b":
                return "MY_TOURNAMENTS_ORG"
            if choice == "q":
                return "QUIT"

            team2 = available_teams[int(choice) - 1]
            print(team2.name, "as Team 2")

            date = input("Date (YYYY-MM-DD): ")
            while (
                self.APILL.validate_match_date(
                    date, tournament.start_date, tournament.end_date
                )
                != Errors.OK
            ):
                print("Date not in tournament")
                date = input("Date (YYYY-MM-DD): ")

            time = input("Time (HH:MM): ")
            error = self.APILL.validate_match_time(time)
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
                if error == Errors.CONTAINS_UNWANTED_CHAR:
                    print(
                        "Cannot contain: Comma, Quotation Marks or Semi Colon, nice try dummy."
                    )
                time = input("Time (HH:MM): ")
                error = self.APILL.validate_match_time(time)

            match = Match(tournament.id, round, team1.name, team2.name, date, time)

            print("Confirm ? (Y/N)")
            choice: str = self.menu_manager.prompt_choice(["y", "n"])
            if choice == "y":
                error = self.APILL.validate_match_creation(match, tournament)
                if error == Errors.OK:
                    match = self.APILL.create_match(match)
                    return self.show_tournament_view(tournament)
                if error == Errors.INVALID_SERVER_COUNT:
                    print("Server amount cannot be less than 1")
                if error == Errors.TEAM_A_ALREADY_IN_SLOT:
                    print(f"Team: {match.team_a_name} is already playing at this time")
                if error == Errors.TEAM_B_ALREADY_IN_SLOT:
                    print(f"Team: {match.team_b_name} is already playing at this time")
                if error == Errors.TEAM_A_ALREADY_IN_ROUND:
                    print(f"Team: {match.team_a_name}")
                if error == Errors.TEAM_B_ALREADY_IN_ROUND:
                    print(f"Team: {match.team_b_name}")
                if error == Errors.TIMESLOT_FULL:
                    print("Select another time, this time slot is full")
                if error == Errors.TEAM_A_LOST_LAST_ROUND:
                    print(
                        f"Team: {match.team_a_name} lost a round and is not in the tournament"
                    )
                if error == Errors.TEAM_B_LOST_LAST_ROUND:
                    print(
                        f"Team: {match.team_b_name} lost a round and is not in the tournament"
                    )
                if error == Errors.CONTAINS_UNWANTED_CHAR:
                    print(
                        "Cannot contain: Comma, Quotation Marks or Semi Colon, nice try dummy."
                    )

            if choice == "n":
                pass

    def check_game_over(self, match: Match) -> bool:
        """Checks if a game has finished or not"""
        date_str = match.match_date
        time_str = match.match_time

        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        time_obj = datetime.strptime(time_str, "%H:%M").time()

        match_datetime = datetime.combine(date_obj, time_obj)

        today = datetime.today()

        if match_datetime > today:
            return True
        return False

    def show_register_results(self, match: Match):
        """Registering results of a match, chooses a winner and marks match as completed"""

        refresh_logo()
        if not self.check_game_over(match):
            print(
                f"Registering result for match: {match.team_a_name} vs {match.team_b_name}\n\n"
            )
            print("Which team won the match?")
            print(f"1. {match.team_a_name}")
            print(f"2. {match.team_b_name}")
            print("")

            print("d. Delete match\nb. Back\nq. Quit: ")
            choice = self.menu_manager.prompt_choice(["1", "2", "b", "q"])

            if choice == "b":
                return "MY_TOURNAMENTS_ORG"
            if choice == "q":
                return "QUIT"

            # select winner
            if choice == "1":
                winner_name = match.team_a_name
            elif choice == "2":
                winner_name = match.team_b_name
            else:
                print("Invalid input.")
                return

            # set winner
            print("*WARNING* this change is permanent, confirm? (Y/N)")
            confirmation = self.menu_manager.prompt_choice(["y", "n"])
            if confirmation == "y":
                match.set_winner(winner_name, "TRUE")
            if confirmation == "n":
                print("Match winner not set")
                input("Enter to continue")

                return "MY_TOURNAMENTS_ORG"

            self.APILL.register_match_result(match.match_id, winner_name, "TRUE")
            self.APILL.give_team_points(winner_name, +2)
            if match.round == "Final":
                print(f"{winner_name} have won the tournament!")
                self.print_trophy()
                print("b. Back\nq. Quit")
            else:
                print(f"{winner_name} has been set as the winner of this match.")
        else:
            print("Match not over")
            print("b. Back\nq. Quit")
        choice = self.menu_manager.prompt_choice(["b", "q"])
        if choice == "b":
            return "MY_TOURNAMENTS_ORG"
        if choice == "q":
            return "QUIT"

    def show_delete_tournament(self, tournament):
        """Deletes the tournament chosen"""
        print(f"Are you sure you wish to delete {tournament.name}")
        confirm = input("Confirm(Y/N): ")
        if confirm.lower() == "y":
            self.APILL.delete_tournament(tournament)
            print(f"{tournament.name} has been deleted")
            enter_to_leave = input("Enter to exit or q to Quit.")
            if enter_to_leave.lower() == "q":
                return "QUIT"
            else:
                return "MY_TOURNAMENTS_ORG"
        if confirm.lower == "n":
            return "MY_TOURNAMENTS_ORG"

    def print_trophy(self):
        """Prints a magnificent championship trophy"""
        set_system_color_gold()
        print(r"""              
              .-=========-.
              \'-=======-'/
              _|   .=.   |_
             ((|  {{1}}  |))
              \|   /|\   |/
               \__ '`' __/
                 _`) (`_
               _/_______\_
              /___________\ """)
        set_system_color_red()

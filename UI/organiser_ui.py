from datetime import datetime
from tracemalloc import start
from LL.api_ll import APILL
from Models.contact_person import ContactPerson
from Models.models import Match, Player, Team, Tournament
from UI.functions import format_player_list, format_team_list, format_tournament_table
from UI.ui_functions import refresh_logo
from LL.validators_ll import (
    ValidationError,
    validate_tournament_double_elimination,
    validate_tournament_end_date,
    validate_tournament_name,
    validate_tournament_game,
    validate_tournament_start_date,
    validate_tournament_venue,
    validate_tournament_servers,
)


class OrganiserUI:
    """UI functions for organiser"""

    def __init__(self, APILL: APILL, menu_manager) -> None:
        self.APILL = APILL
        self.menu_manager = menu_manager
        self.team_to_view: Team

    def show_create_tournament(self):
        """Creates tournaments with options to quit or back anywhere in the process and shows the confirmation of creation"""
        print("Fill in the required info or b.Back or q.Quit")

        while True:
            name_of_tournament = input("Name: ")
            if name_of_tournament.lower() == "b":
                return "ORGANISER_MENU"
            if name_of_tournament.lower() == "q":
                return "QUIT"
            try:
                name_of_tournament = validate_tournament_name(name_of_tournament)
                break
            except ValidationError as e:
                print(str(e))

        while True:
            start_date_of_tournament = input("Start date(Year-Month-Day): ")
            if start_date_of_tournament.lower() == "b":
                return "ORGANISER_MENU"
            if start_date_of_tournament.lower() == "q":
                return "QUIT"
            try:
                start_date_of_tournament = validate_tournament_start_date(
                    start_date_of_tournament
                )
                break
            except ValidationError as e:
                print(str(e))
        while True:
            end_date_of_tournamnet = input("End date(Year-Month-Day): ")
            if end_date_of_tournamnet.lower() == "b":
                return "ORGANISER_MENU"
            if end_date_of_tournamnet.lower() == "q":
                return "QUIT"
            try:
                end_date_of_tournamnet = validate_tournament_end_date(
                    start_date_of_tournament, end_date_of_tournamnet
                )
                break
            except ValidationError as e:
                print(str(e))
        while True:
            amount_of_servers = input("Number of servers: ")
            if amount_of_servers.lower() == "b":
                return "ORGANISER_MENU"
            if amount_of_servers.lower() == "q":
                return "QUIT"
            try:
                amount_of_servers = validate_tournament_servers(amount_of_servers)
                break
            except ValidationError as e:
                print(str(e))
        while True:
            venue = input("Venue: ")
            if venue.lower() == "b":
                return "ORGANISER_MENU"
            if venue.lower() == "q":
                return "QUIT"
            try:
                venue = validate_tournament_venue(venue)
                break
            except ValidationError as e:
                print(str(e))
        while True:
            double_elimination = input("Double elimination(Y/N): ")
            if double_elimination.lower() == "b":
                return "ORGANISER_MENU"
            if double_elimination.lower() == "q":
                return "QUIT"
            try:
                double_elimination = validate_tournament_double_elimination(
                    double_elimination
                )
                break
            except ValidationError as e:
                print(str(e))

        while True:
            games = self.APILL.get_all_games()
            print("Valid games are:", *games)
            game_for_tournament = input("Game: ")
            if game_for_tournament.lower() == "b":
                return "ORGANISER_MENU"
            if game_for_tournament.lower() == "q":
                return "QUIT"
            try:
                game_for_tournament = validate_tournament_game(
                    game_for_tournament, games
                )
                break
            except ValidationError as e:
                print(str(e))

        print("Fill in contact person info or 'b' to Back and 'q' to Quit")
        while True:
            new_contact_person_name = input("Name: ")
            if new_contact_person_name == "b":
                return "ORGANISER_MENU"
            if new_contact_person_name == "q":
                return "QUIT"
            break
        # Try and except fyrir contact person name validation
        while True:
            new_contact_person_email = input("Email: ")
            if new_contact_person_email == "b":
                return "ORGANISER_MENU"
            if new_contact_person_email == "q":
                return "QUIT"
            break
        # Try and except for contact person email validation
        while True:
            new_contact_person_phone_nmbr = input("Phone number: ")
            if new_contact_person_phone_nmbr == "b":
                return "ORGANISER_MENU"
            if new_contact_person_phone_nmbr == "q":
                return "QUIT"
            break
        # Try and except for contact person phone number validation
        confirmation = input("Confirm(Y): ")
        if confirmation.lower() != "y":
            return "ORGANISER_MENU"

        print("b. Back \nq. Quit")
        # TODO setja inn tournament created menuið

        new_tournament = Tournament(
            name_of_tournament,
            datetime.fromisoformat(start_date_of_tournament),
            datetime.fromisoformat(end_date_of_tournamnet),
            venue,
            game_for_tournament.name,
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
            print("tournaments: ", tournament.matches)

        print("MY_TOURNAMENTS_ORG")
        print("")
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
        if tournament:
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
            print("c. Create new match\nb. Back\nq. Quit")
            choice: str = self.menu_manager.prompt_choice(
                valid_choices + ["c", "b", "q"]
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

            if choice == "b":
                return "MY_TOURNAMENTS_ORG"
            if choice == "q":
                return "QUIT"

    def show_create_match(self, tournament: Tournament):
        """Function for creating matches as an organiser"""
        teams_in_tournament = self.APILL.get_teams_in_tournament(tournament)
        print("Teams in tournament: ")
        for team in teams_in_tournament:
            print(team.name, end=" | ")
        print("")
        print("Round types:")
        print("  R16 QF SF Final")

        prompts = [
            "Round: ",
            "Team 1: ",
            "Team 2: ",
            "Date YYYY-MM-DD: ",
            "Time HH-MM-SS: ",
        ]
        user_inputs = {}

        for prompt in prompts:
            while True:  # prompt until back, quit or valid input
                current_input = input(prompt)
                if current_input.lower() == "b":
                    return "MY_TOURNAMENTS_ORG"
                elif current_input.lower() == "q":
                    return "QUIT"
                else:
                    user_inputs[prompt] = current_input
                    break  # exit the loop
        match = Match(
            tournament.id,
            user_inputs["Round: "],
            user_inputs["Team 1: "],
            user_inputs["Team 2: "],
            user_inputs["Date YYYY-MM-DD: "],
            user_inputs["Time HH-MM-SS: "],
        )

        try:
            match = self.APILL.create_match(match)
        except ValueError:
            print("Invalid values")

        # Get information about matc
        if match:
            print("Match created with id: ", match.match_id)
        else:
            print("Match not created")

        pass

    def show_register_results(self, match: Match):
        """Registering results of a match, chooses a winner and turns match completed to True"""
        print("Which team won the match? ")
        print(f"1. {match.team_a_name}")
        print(f"2. {match.team_b_name}")
        winner = input("1 or 2, b to back and q to quit")
        if winner == "1":
            match.set_winner(match.team_a_name, True)
            print(f"{match.winner_team_name} has been set as the winner of this match")
            choice: str = self.menu_manager.prompt_choice(["b", "q"])
            print("b to back or q to quit")
            if choice == "b":
                return "MY_TOURNAMENTS_ORG"
            if choice == "q":
                return "QUIT"

        if winner == "2":
            match.set_winner(match.team_b_name, True)
            print(f"{match.winner_team_name} has been set as the winner of this match")
            print("b to back or q to quit")
            choice: str = self.menu_manager.prompt_choice(["b", "q"])
            if choice == "b":
                return "MY_TOURNAMENTS_ORG"
            if choice == "q":
                return "QUIT"
        if winner == "b":
            return "MY_TOURNAMENTS_ORG"
        if winner == "q":
            return "QUIT"

    def show_delete_tournament(self):
        # TODO
        pass

    def show_give_points(self):
        # TODO
        pass

    def show_teams_org(self):
        """Showing teams for organiser"""
        teams = self.APILL.get_all_teams()
        print(format_team_list(teams))
        print("Select which team you would like to look at: \nb.Back \nq.Quit")

        valid_choices = []
        for counter, team in enumerate(teams):
            valid_choices.append(str(counter))

        choice: str = self.menu_manager.prompt_choice(valid_choices + ["b", "q"])

        if choice in valid_choices:
            self.team_to_view = teams[int(choice) - 1]
            return self.show_players_in_team_org()

        if choice.lower() == "b":
            return "ORGANISER_MENU"

        return "QUIT"

    def show_players_in_team_org(self):
        """Shows players in the selected team"""
        refresh_logo()
        team = self.team_to_view
        if team != "":
            players = self.APILL.get_players_in_team(team.name)
            valid_choices = []
            print(format_player_list(players))
            print("b. Back \nq.Quit")
            for i in range(len(players)):
                stringI = str(i + 1)
                valid_choices.append(stringI)
            choice: str = self.menu_manager.prompt_choice(valid_choices + ["b", "q"])

            for element in valid_choices:
                if element == choice:
                    player = self.show_players_with_personal_info_org(
                        players[int(element) - 1]
                    )
                    return player

            if choice.lower() == "q":
                return "QUIT"
            if choice.lower() == "b":
                return "TEAMS_ORG"

    def show_players_with_personal_info_org(self, player: Player):
        """The actual view of players information"""
        if player:
            team = self.APILL.get_team_by_name(player.team_name)
            print(f"{player.name.upper()}  |  {player.handle} ")
            print("-" * len(f"    SOCIAL MEDIA: {player.social_media}"))

            print(f"    DATE OF BIRTH: {player.date_of_birth}")
            print(f"    ADDRESS: {player.address}")
            print(f"    PHONE: {player.phone_number}")
            print(f"    EMAIL: {player.email}")
            print(f"    HANDLE: {player.handle}")
            print(f"    SOCIAL MEDIA: {player.social_media}")
            print(f"    TEAM: {player.team_name}")
            print("-" * len(f"    SOCIAL MEDIA: {player.social_media}"))
            input("Enter to return")
            if team:
                return "SHOW_PLAYERS_IN_TEAM_ORG"

from LL.api_ll import APILL
import UI.functions as f
from UI.ui_functions import refresh_logo
from Models.models import (
    Team,
    Tournament, 
    Player, 
    TeamCaptain
)
from LL.validators_ll import (
    validate_address,
    validate_date_of_birth,
    validate_phone_number,
    validate_player_email,
    validate_player_handle,
    validate_player_name,
    Errors,
    validate_players_in_teams,
    validate_social_media,
    validate_team_logo,
    validate_team_name,
)

class TeamCaptainUI:
    def __init__(self, APILL: APILL, menu_manager) -> None:
        self.APILL = APILL
        self.menu_manager = menu_manager

    def show_create_player(self):
        """Creating a player with the required information"""
        name = input("Player's name: ").strip()
        if name == "q":
            return "QUIT"
        if name == "b":
            return "MY_TEAM"
        error = self.APILL.validate_player_name(name)
        while error != Errors.OK:
            if error == Errors.EMPTY:
                print("Name cannot be empty")
            if error == Errors.NAME_INCLUDE_NUMBERS:
                print("Name cannot include a number")
            if error == Errors.CONTAINS_UNWANTED_CHAR:
                print(
                    "Cannot contain: Comma, Quotation Marks or Semi Colon, nice try dummy."
                )
            if name.lower() == "b":
                return "SHOW_MY_PLAYERS"
            if name.lower() == "q":
                return "QUIT"
            name = input("Player's name: ").strip()
            error = self.APILL.validate_player_name(name)

        date_of_birth = input("Player's birthday (YYYY-MM-DD): ").strip()
        if date_of_birth == "q":
            return "QUIT"
        if date_of_birth == "b":
            return "MY_TEAM"
        error = self.APILL.validate_date_of_birth(date_of_birth)
        while error != Errors.OK:
            if error == Errors.DATE_NOT_VALID:
                print("Use format YYYY-MM-DD")
            if error == Errors.DATE_TOO_OLD:
                print("Invalid date, choose a date after 1900")
            if error == Errors.CONTAINS_UNWANTED_CHAR:
                print(
                    "Cannot contain: Comma, Quotation Marks or Semi Colon, nice try dummy."
                )
            if date_of_birth.lower() == "b":
                return "MY_TEAM"
            if date_of_birth.lower() == "q":
                return "QUIT"
            error = self.APILL.validate_date_of_birth(date_of_birth)
            date_of_birth = input("Player's birthday (YYYY-MM-DD): ").strip()

        address = input("Enter address: ").strip()
        if address == "q":
            return "QUIT"
        if address == "b":
            return "MY_TEAM"
        error = self.APILL.validate_address(address)
        while error != Errors.OK:
            if error == Errors.EMPTY:
                print("Address cannot be empty.")
            if error == Errors.ADDRESS_ONLY_NUMBERS:
                print("Address cannot only be digits.")
            if error == Errors.CONTAINS_UNWANTED_CHAR:
                print(
                    "Cannot contain: Comma, Quotation Marks or Semi Colon, nice try dummy."
                )
            if address.lower() == "b":
                return "MY_TEAM"
            if address.lower() == "q":
                return "QUIT"
            address = input("Enter address: ").strip()
            error = self.APILL.validate_address(address)

        phone_number = input("Enter phone number: ").strip()
        if phone_number == "q":
            return "QUIT"
        if phone_number == "b":
            return "MY_TEAM"
        error = self.APILL.validate_phone_number(phone_number)
        while error != Errors.OK:
            if error == Errors.EMPTY:
                print("Phone number cannot be empty.")
            if error == Errors.NUMBER_HAS_CHARACTERS:
                print("Phone number cannot include characters.")
            if error == Errors.NUMBER_NOT_CORRECT_LENGTH:
                print("Phone number has to be exactly 7 digits.")
            if error == Errors.CONTAINS_UNWANTED_CHAR:
                print(
                    "Cannot contain: Comma, Quotation Marks or Semi Colon, nice try dummy."
                )
            if phone_number.lower() == "b":
                return "MY_TEAM"
            if phone_number.lower() == "q":
                return "QUIT"
            phone_number = input("Enter phone number: ").strip()
            error = self.APILL.validate_phone_number(phone_number)

        email = input("Enter email: ").strip()
        if email == "q":
            return "QUIT"
        if email == "b":
            return "MY_TEAM"
        error = self.APILL.validate_player_email(email)
        while error != Errors.OK:
            if error == Errors.EMPTY:
                print("Email address cannot be empty.")
            if error == Errors.EMAIL_NOT_CONTAINING_AT:
                print("Email has to include '@', example@example.com.")
            if error == Errors.CONTAINS_UNWANTED_CHAR:
                print(
                    "Cannot contain: Comma, Quotation Marks or Semi Colon, nice try dummy."
                )
            if email.lower() == "b":
                return "MY_TEAM"
            if email.lower() == "q":
                return "QUIT"
            email = input("Enter email: ").strip()
            error = self.APILL.validate_player_email(email)

        social_media = input("Enter social media handle: ").strip()
        if social_media == "q":
            return "QUIT"
        if social_media == "b":
            return "MY_TEAM"
        error = self.APILL.validate_social_media(social_media)
        while error != Errors.OK:
            if error == Errors.EMPTY:
                print("Social media handle cannot be empty.")
            if error == Errors.HANDLE_CONTAINS_SPACE:
                print("Social media handle cannot contain empty spaces.")
            if error == Errors.CONTAINS_UNWANTED_CHAR:
                print(
                    "Cannot contain: Comma, Quotation Marks or Semi Colon, nice try dummy."
                )
            if social_media.lower() == "b":
                return "MY_TEAM"
            if social_media.lower() == "q":
                return "QUIT"
            social_media = input("Enter social media handle: ").strip()
            error = self.APILL.validate_social_media(social_media)

        handle = input("Enter player handle: ").strip()
        if handle == "q":
            return "QUIT"
        if handle == "b":
            return "MY_TEAM"
        error = self.APILL.validate_player_handle(handle)
        while error != Errors.OK:
            if error == Errors.EMPTY:
                print("Player handle cannot be empty.")
            if error == Errors.HANDLE_CONTAINS_SPACE:
                print("Handle cannot contain empty spaces.")
            if error == Errors.CONTAINS_UNWANTED_CHAR:
                print("Cannot contain: Comma, Quotation Marks or Semi Colon, nice try dummy.")
            if error == Errors.SAME_HANDLE:
                print("Cannot have the same handle as another player.")
            if handle.lower() == "b":
                return "MY_TEAM"
            if handle.lower() == "q":
                return "QUIT"
            handle = input("Enter player handle: ").strip()
            error = self.APILL.validate_player_handle(handle)

        team = self.menu_manager.team_name
        new_player = Player(
            name,
            date_of_birth,
            address,
            phone_number,
            email,
            social_media,
            handle,
            team,
        )

        self.APILL.create_player(new_player)
        return self.player_added_screen(name, handle, social_media)

    def player_added_screen(self, name, handle, social_media):
        """Screen that is shown after creating/adding a player"""
        player_name = name
        player_handle = handle
        player_social = social_media
        print(f"PLAYER ADDED!\n{player_name} \n{player_handle} \n{player_social}")

        print("")
        print("b. Back \nq. Quit")
        choice: str = self.menu_manager.prompt_choice(["b", "q"])
        if choice == "b":
            return "MY_TEAM"
        if choice == "q":
            return "QUIT"

    def show_my_tournaments(self):
        """Tournaments the team captain has registered to"""
        team = self.APILL.get_team_by_name(self.menu_manager.team_name)
        players = self.APILL.get_players_in_team(self.menu_manager.team_name)
        captain = TeamCaptain(
            self.menu_manager.team_name, self.menu_manager.captain_handle
        )
        if team:
            tournaments = self.APILL.get_my_tournaments(team)
            print(f.format_tournament_table(tournaments))
            valid_choices_of_tournaments = []
            for index in range(len(tournaments)):
                valid_choices_of_tournaments.append(str(index + 1))
            print("r. Register for new tournament\nb. Back\nq. Quit")
            choice: str = self.menu_manager.prompt_choice(
                valid_choices_of_tournaments + ["r", "b", "q"]
            )
            if choice in valid_choices_of_tournaments:
                return self.show_tournament_view_cap(tournaments[int(choice) - 1])
            if choice == "r":
                while self.APILL.validate_players_in_teams(players) != Errors.OK:
                    error = self.APILL.validate_players_in_teams(players)
                    if error == Errors.PLAYERS_NOT_ENOUGH:
                        print("Not enough players on team to register.")
                    if error == Errors.PLAYERS_TOO_MANY:
                        print(
                            "Too many players on this team to register for a tournament."
                        )
                    input("Enter to exit")
                    return "MY_TOURNAMENTS_CAP"

                valid_choices: list[str] = []
                tournaments = self.APILL.get_all_open_tournaments_for_captain(captain)

                print(f.format_tournament_table(tournaments))
                print(
                    "Choose tournament to register for or 'b' to Back and 'q' to Quit"
                )
                for i in range(len(tournaments)):
                    stringI = str(i + 1)
                    valid_choices.append(stringI)
                choice: str = self.menu_manager.prompt_choice(
                    valid_choices + ["b", "q"]
                )
                if choice in valid_choices:
                    self.APILL.register_team_to_tournament(
                        team, tournaments[int(choice) - 1]
                    )
                    print(
                        f"{team} has been registered for {tournaments[int(choice) - 1].name}"
                    )
                    while True:
                        back_or_quit = (
                            input("b to go back to tournament menu or q to quit: ")
                            .strip()
                            .lower()
                        )

                        if back_or_quit == "b":
                            return "MY_TOURNAMENTS_CAP"  # Go back to tournament menu
                        elif back_or_quit == "q":
                            return "QUIT"  # Quit command
                        else:
                            print("Invalid choice, valid choices are B and Q.")
                if choice == "b":
                    return "MY_TOURNAMENTS_CAP"
                if choice == "q":
                    return "QUIT"

            if choice == "b":
                return "TEAM_CAPTAIN_MENU"
            if choice == "q":
                return "QUIT"

    def show_tournament_view_cap(self, tournament: Tournament):
        """takes in a tournament name and shows the menu for the tournament"""

        refresh_logo()
        w_team = 26
        w_date = 12
        w_time = 12
        w_round = 8
        w_vs = 4
        w_completed = 10
        if tournament:
            print(
                f"{tournament.name.upper()}  |  {tournament.start_date} -- {tournament.end_date} "
            )
            print("--------------------")
            print(" ")
            print("Matches: ")
            header = (
                f"{'Team 1':<{w_team}}"
                f"{'vs':^{w_vs}}"
                f"{'Team 2':>{w_team}} "
                f"{'Date':^{w_date}}"
                f"{'Time':^{w_time}}"
                f"{'Round':>{w_round}}"
                f"{'Completed':>{w_completed}}"
                f"{'Winner':<{w_team}}"
            )
            print(header)
            print("-" * len(header))
            for match in tournament.matches:
                print(f"{match}")

            print("")

            print("b. Back")
            print("q. Quit")

        choice: str = self.menu_manager.prompt_choice(["b", "q"])
        if choice == "b":
            return "MY_TOURNAMENTS_CAP"

    def show_modify_player_menu(self, player: Player):
        """displays a menu of player attributes to change"""
        refresh_logo()
        while True:
            print(f"\n      Editing Player: {player.name}      ")
            #sýnir current og svo changed, confirm og cancel
            print(f"1. Change Name      (Current: {player.name})")
            print(f"2. Change Email     (Current: {player.email})")
            print(f"3. Change Address   (Current: {player.address})")
            print(f"4. Change Number    (Current: {player.phone_number})")
            print(f"5. Change Socials   (Current: {player.social_media})")
            print(f"6. Change Handle    [Current: {player.handle}]")
            print("s. Finish and Save")
            print("c. Cancel")

            selection = input("Select the data you want to change (1-6): ")
            if selection == "1":
                new_name = input("Enter new name: ").strip()
                error = self.APILL.validate_player_name(new_name)
                while error != Errors.OK:
                    if error == Errors.EMPTY:
                        print("Name cannot be empty")
                    if error == Errors.NAME_INCLUDE_NUMBERS:
                        print("Name cannot include numbers")
                    if error == Errors.CONTAINS_UNWANTED_CHAR:
                        print(
                            "Cannot contain: Comma, Quotation Marks or Semi Colon, nice try dummy."
                        )
                    new_name = input("Enter new name: ").strip()
                    error = self.APILL.validate_player_name(new_name)
                print("Name updated locally.")

            elif selection == "2":
                new_email = input("Enter new email: ").strip()
                error = self.APILL.validate_player_email(new_email)
                while error != Errors.OK:
                    if error == Errors.EMPTY:
                        print("Email cannot be empty")
                    if error == Errors.EMAIL_NOT_CONTAINING_AT:
                        print("Email must contain @, example@example.com")
                    if error == Errors.CONTAINS_UNWANTED_CHAR:
                        print(
                            "Cannot contain: Comma, Quotation Marks or Semi Colon, nice try dummy."
                        )
                    new_email = input("Enter new email: ").strip()
                    error = self.APILL.validate_player_email(new_email)
                player.email = new_email
                print("Email updated locally.")

            elif selection == "3":
                new_address = input("Enter new address: ").strip()
                error = self.APILL.validate_address(new_address)
                while error != Errors.OK:
                    if error == Errors.EMPTY:
                        print("Address cannot be empty")
                    if error == Errors.ADDRESS_ONLY_NUMBERS:
                        print("Address cannot be only numbers")
                    if error == Errors.CONTAINS_UNWANTED_CHAR:
                        print(
                            "Cannot contain: Comma, Quotation Marks or Semi Colon, nice try dummy."
                        )
                    new_address = input("Enter new address: ").strip()
                    error = self.APILL.validate_address(new_address)
                player.address = new_address
                print("Address updated locally.")

            elif selection == "4":
                new_number = input("Enter new phone number: ").strip()
                error = self.APILL.validate_phone_number(new_number)
                while error != Errors.OK:
                    if error == Errors.NUMBER_NOT_CORRECT_LENGTH:
                        print("Phone number must be 7 digits")
                    if error == Errors.NUMBER_HAS_CHARACTERS:
                        print("Phone number cannot contain characters")
                    if error == Errors.CONTAINS_UNWANTED_CHAR:
                        print(
                            "Cannot contain: Comma, Quotation Marks or Semi Colon, nice try dummy."
                        )
                    new_number = input("Enter new phone number: ").strip()
                    error = self.APILL.validate_phone_number(new_number)
                player.phone_number = new_number
                print("Address updated locally.")

            elif selection == "5":
                new_socials = input("Enter new social media handle: ").strip()
                error = self.APILL.validate_social_media(new_socials)

                while error != Errors.OK:
                    if error == Errors.EMPTY:
                        print("Social Media cannot be empty")
                    if error == Errors.HANDLE_CONTAINS_SPACE:
                        print("Social Media cannot contain spaces")
                    if error == Errors.CONTAINS_UNWANTED_CHAR:
                        print(
                            "Cannot contain: Comma, Quotation Marks or Semi Colon, nice try dummy."
                        )
                    new_socials = input("Enter new social media handle: ").strip()
                    error = self.APILL.validate_social_media(new_socials)

                player.social_media = new_socials
                print("Socials updated locally.")

            elif selection == "6":
                new_handle = input("Enter new game handle: ").strip()
                error = self.APILL.validate_player_handle(new_handle)

                while error != Errors.OK:
                    if error == Errors.EMPTY:
                        print("Handle cannot be empty")
                    if error == Errors.HANDLE_CONTAINS_SPACE:
                        print("Handle cannot contain spaces")
                    if error == Errors.CONTAINS_UNWANTED_CHAR:
                        print(
                            "Cannot contain: Comma, Quotation Marks or Semi Colon, nice try dummy."
                        )
                    new_handle = input("Enter new game handle: ").strip()
                    error = self.APILL.validate_player_handle(new_handle)
                team: Team = self.menu_manager.team_to_view
                if player.handle == team.captain_handle:
                    self.menu_manager.team_to_view.captain_handle = new_handle
                    self.APILL.modify_team_data(team)
                player.handle = new_handle

                print("Game handle updated locally.")

            elif selection.lower() == "s":
                #saves info
                try:
                    self.APILL.modify_player(player)
                    print("Success, player data saved to database.")
                    return "SHOW_MY_PLAYERS"
                except Exception as e:
                    print(f"Error saving data: {e}")

            elif selection.lower() == "c":
                print("Change cancelled.")
                return "SHOW_MY_PLAYERS"

            else:
                print("Invalid selection. Please try again.")

    def show_my_team(self) -> str | None:
        """Shows the team captains team info"""
        team_name = self.menu_manager.team_name
        team = self.APILL.get_team_by_name(team_name)

        if team:
            print(team.my_team_header())
            print(
                "1. Add team to club \n2. Roster \n3. Edit team info \nb. Back \nq. Quit"
            )

            choice: str = self.menu_manager.prompt_choice(["1", "2", "3", "b", "q"])

            if choice == "1":
                return "ADD_TEAM_TO_CLUB"
            if choice == "2":
                return "SHOW_MY_PLAYERS"
            if choice == "3":
                return self.show_modify_team_menu()

            if choice.lower() == "b":
                return "TEAM_CAPTAIN_MENU"
            if choice.lower() == "q":
                return "QUIT"

    def show_my_players(self):
        """shows players that are on the team captains team"""
        # TODO laga útlit
        team = self.APILL.get_team_by_name(self.menu_manager.team_name)
        players = self.APILL.get_players_in_team(self.menu_manager.team_name)
        valid_choices = []

        if team:
            print(team.my_team_header())

        for i, player in enumerate(players):
            player.format_row(i + 1)
            stringI = str(i + 1)
            valid_choices.append(stringI)
        print("")
        print("6. Add player: \nb. Back \nq.Quit")
        choice: str = self.menu_manager.prompt_choice(
            valid_choices + ["6", "7", "b", "q"]
        )

        for element in valid_choices:
            if element == choice:
                player = self.show_player_view(players[int(element) - 1])
                return player
        if choice == "6":
            return "CREATE_PLAYER"

        if choice.lower() == "q":
            return "QUIT"
        if choice.lower() == "b":
            return "MY_TEAM"

    def show_player_view(self, player: Player):
        """takes in a player name and shows the menu for the player"""

        refresh_logo()
        if player:
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

            print("")
            valid_choices = []
            if self.menu_manager.user == "TEAM_CAPTAIN":
                print("1. Edit player data")
                print("2. Remove player from team")
                valid_choices = ["1", "2"]

            print("")
            print("b. Back")
            print("q. Quit")

            choice: str = self.menu_manager.prompt_choice(valid_choices + ["b", "q"])

            if choice == "1":
                # Modify player menuið
                return self.show_modify_player_menu(player)
            if choice == "2":
                return self.remove_selected_player(player)
            if choice == "b" and self.menu_manager.user == "TEAM_CAPTAIN":
                return "SHOW_MY_PLAYERS"
            if choice == "b" and self.menu_manager.user == "ORGANISER":
                return "SHOW_"

            if choice == "q":
                return "QUIT"

    def show_register_team_to_tournament(self, team, tournament):
        """Registration for tournament"""
        self.team = team
        self.tournament = tournament
        self.APILL.register_team_to_tournament(team, tournament)

    def show_update_team_data(self):
        """Updates the data of a team, social media or logo"""
        # TODO b krafa
        # STEINAR
        print("1. Edit social media\n2. Edit Logo")
        print("")
        print("b. Back\nq. Quit")
        choice: str = self.menu_manager.prompt_choice(["1", "2", "b", "q"])
        if choice == "1":
            return "EDIT_SOCIAL_MEDIA"
        if choice == "2":
            return "EDIT_LOGO"
        if choice == "b":
            return "MY_TEAM"
        if choice == "q":
            return "QUIT"

    def show_modify_team_menu(self):
        """same as for modifying player but for team"""
        refresh_logo()
        team = self.APILL.get_team_by_name(self.menu_manager.team_name)
        if not team:
            print("Error: team not found.")
            input("Press enter to return")
            return "MY_TOURNAMENTS_ORG"

        while True:
            print(f"\n      {team.name}   ")
            print(f"1. Change Logo          (Current: {team.logo})")
            print(f"2. Change Social Media  (Current: {team.social_media})")
            print("s. Finish and Save")
            print("c. Cancel")
            #pick what to change
            selection = input("Select the data you want to change: ")
            #logo editing
            if selection == "1":
                new_logo = input("Enter new Logo: ").strip()
                error = validate_team_logo(new_logo) 
                while error != Errors.OK:
                    if error == Errors.EMPTY:
                        print("Logo cannot be empty")
                    if error == Errors.CONTAINS_UNWANTED_CHAR:
                        print("Cannot contain: Comma, Quotation Marks or Semi Colon, nice try dummy.")
                    new_logo = input("Enter new Logo: ").strip()
                    error = validate_team_logo(new_logo)
                #update without saving
                team.logo = new_logo
                print("Logo updated locally.")

            #edit socials
            elif selection == "2":
                new_social_media = input("Enter new Social Media: ").strip()
                error = self.APILL.validate_social_media(new_social_media)
                while error != Errors.OK:
                    if error == Errors.EMPTY:
                        print("Social Media cannot be empty")
                    if error == Errors.HANDLE_CONTAINS_SPACE:
                        print("Social Media cannot contain spaces")
                    if error == Errors.CONTAINS_UNWANTED_CHAR:
                        print("Cannot contain: Comma, Quotation Marks or Semi Colon, nice try dummy.")
                    new_social_media = input("Enter new Social Media: ").strip()
                    error = self.APILL.validate_social_media(new_social_media)
                
                team.social_media = new_social_media
                print("Social Media updated locally.")

            #Save the info
            elif selection.lower() == "s":
                try:
                    updated_team = self.APILL.modify_team_data(team)
                    if updated_team:
                        print("Success, team data changed")
                        print("-" * 30)
                        print(f"New Logo: {updated_team.logo}")
                        print(f"New Socials: {updated_team.social_media}")
                        print("-" * 30)
                        input("Enter to go return")
                        return "MY_TEAM" #back to team
                    else:
                        print("Data update failed.")      
                except Exception as e:
                    print(f"Error saving data: {e}")
            #canceling
            elif selection.lower() == "c":
                print("Changes cancelled")
                return "MY_TEAM" #return without saving
            else:
                print("Invalid selection. Please try again.")
    

    def show_add_team_to_club(self):
        clubs = self.APILL.get_all_club_data()
        valid_choices = []
        team = self.menu_manager.team_to_view

        for index, club in enumerate(clubs):
            correct_index = index + 1
            print(correct_index, ". ", club, sep="")
            valid_choices.append(str(correct_index))

        print("b. Back\nq. Quit")
        choice: str = self.menu_manager.prompt_choice(valid_choices + ["b", "q"])
        if choice in valid_choices:
            if team.club == "No club":
                self.APILL.add_team_to_club(team, clubs[int(choice) - 1])
                print(
                    team.name,
                    "Added to club",
                    clubs[int(choice) - 1],
                )
                team.set_club(clubs[int(choice) - 1].name)
            else:
                print("Team already belongs to a club")
            print("b. Back\nq. Quit")
            choice = self.menu_manager.prompt_choice(["b", "q"])

            if choice == "b":
                return "MY_TEAM"
            if choice == "q":
                return "QUIT"

        if choice == "b":
            return "MY_TEAM"
        if choice == "q":
            return "QUIT"

    def show_create_team(self):  # TODO Klára þetta
        """If you are a new team captain you get this option to create a team"""
        print(
            "Input the required information about the team or 'b' to Back and 'q' to Quuit"
        )
        team_name = input("Team name: ")
        if team_name.lower == "b":
            return "TEAM_CAPTAIN_MENU"
        if team_name.lower == "q":
            return "QUIT"
        while self.APILL.validate_team_name(team_name) != Errors.OK:
            error = self.APILL.validate_team_name(team_name)
            if error == Errors.EMPTY:
                print("Team name cannot be empty.")
            if error == Errors.TEAM_NAME_TOO_LONG:
                print("Team name is too many characters.")
            if error == Errors.CONTAINS_UNWANTED_CHAR:
                print(
                    "Cannot contain: Comma, Quotation Marks or Semi Colon, nice try dummy."
                )
            team_name = input("Team name: ")
        # New team captain
        social_media = input("Social media: ")
        if social_media.lower() == "b":
            return "TEAM_CAPTAIN_MENU"
        if social_media.lower() == "q":
            return "QUIT"
        while self.APILL.validate_social_media(social_media) != Errors.OK:
            error = self.APILL.validate_social_media(social_media)
            if error == Errors.EMPTY:
                print("Social media handle cannot be empty.")
            if error == Errors.EMPTY:
                print("Social media handle cannot contain empty spaces.")
            if error == Errors.CONTAINS_UNWANTED_CHAR:
                print(
                    "Cannot contain: Comma, Quotation Marks or Semi Colon, nice try dummy."
                )
            social_media = input("Social media: ")
        team_logo = input("Input team logo in ASCII lettering: ")
        if team_logo.lower() == "q":
            return "QUIT"
        if team_logo.lower() == "b":
            return "TEAM_CAPTAIN_MENU"
        while self.APILL.validate_team_logo(team_logo) != Errors.OK:
            error = self.APILL.validate_team_logo(team_logo)
            if error == Errors.LOGO_EMPTY:
                print("Logo cannot be empty.")
            if error == Errors.CONTAINS_UNWANTED_CHAR:
                print(
                    "Cannot contain: Comma, Quotation Marks or Semi Colon, nice try dummy."
                )
            team_logo = input("Input team logo in ASCII lettering: ")

    def remove_selected_player(self, player: Player):
        """Removes the selected player from the team"""
        print(f"Are you sure you want to remove {player.name}?")
        confirmation = input("Confirm(Y/N)")
        if confirmation.lower() == "y":
            self.APILL.delete_player(player.id)
            print("DELETED PLAYER")
            enter_to_leave = input("Enter to exit or q to Quit.")
            if enter_to_leave.lower() == "q":
                return "QUIT"
            else:
                return "MY_TEAM"
        else:
            return "MY_TEAM"

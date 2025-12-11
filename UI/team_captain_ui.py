from datetime import date
from pickle import EMPTY_TUPLE
from wsgiref import validate
from LL.api_ll import APILL
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
from Models.player import Player
from Models.team import Team
from Models.team_captain import TeamCaptain
import UI.functions as f
from UI.ui_functions import refresh_logo


class TeamCaptainUI:
    def __init__(self, APILL: APILL, menu_manager) -> None:
        self.APILL = APILL
        self.menu_manager = menu_manager

    def show_create_player(self):
        """Creating a player with the required information"""
        name = input("Player's name: ").strip()
        if name.lower() == "b":
            return "SHOW_MY_PLAYERS"
        if name.lower() == "q":
            return "QUIT"
        while validate_player_name(name) != Errors.OK:
            error = validate_player_name(name)
            if error == Errors.EMPTY:
                print("Name cannot be empty")
            if error == Errors.NAME_INCLUDE_NUMBERS:
                print("Name cannot include a number")
            name = input("Player's name: ").strip()

        date_of_birth = input("Player's birthday (YYYY-MM-DD): ").strip()
        if date_of_birth.lower() == "b":
            return "MY_TEAM"
        if date_of_birth.lower() == "q":
            return "QUIT"
        while validate_date_of_birth(date_of_birth) != Errors.OK:
            error = validate_date_of_birth(date_of_birth)
            if error == Errors.DATE_NOT_VALID:
                print("Use format YYYY-MM-DD")
            if error == Errors.DATE_TOO_OLD:
                print("Invalid date, choose a date after 1900")
            date_of_birth = input("Player's birthday (YYYY-MM-DD): ").strip()

        address = input("Enter address: ").strip()
        if address.lower() == "b":
            return "MY_TEAM"
        if address.lower() == "q":
            return "QUIT"
        while validate_address(address) != Errors.OK:
            error = validate_address(address)
            if error == Errors.EMPTY:
                print("Address cannot be empty.")
            if error == Errors.ADDRESS_ONLY_NUMBERS:
                print("Address cannot only be digits.")
                address = input("Enter address: ").strip()

        phone_number = input("Enter phone number: ").strip()
        if phone_number.lower() == "b":
            return "MY_TEAM"
        if phone_number.lower() == "q":
            return "QUIT"
        while validate_phone_number(phone_number) != Errors.OK:
            error = validate_phone_number(phone_number)
            if error == Errors.EMPTY:
                print("Phone number cannot be empty.")
            if error == Errors.NUMBER_HAS_CHARACTERS:
                print("Phone number cannot include characters.")
            if error == Errors.NUMBER_NOT_CORRECT_LENGTH:
                print("Phone number has to be exactly 7 digits.")
            phone_number = input("Enter phone number: ").strip()
        email = input("Enter email: ").strip()
        if email.lower() == "b":
            return "MY_TEAM"
        if email.lower() == "q":
            return "QUIT"
        while validate_player_email(email) != Errors.OK:
            error = validate_player_email(email)
            if error == Errors.EMPTY:
                print("Email address cannot be empty.")
            if error == Errors.EMAIL_NOT_CONTAINING_AT:
                print("Email has to include '@', example@example.com.")
            email = input("Enter email: ").strip()

        social_media = input("Enter social media handle: ").strip()
        if social_media.lower() == "b":
            return "MY_TEAM"
        if social_media.lower() == "q":
            return "QUIT"
        while validate_social_media(social_media) != Errors.OK:
            error = validate_social_media(social_media)
            if error == Errors.EMPTY:
                print("Social media handle cannot be empty.")
            if error == Errors.HANDLE_CONTAINS_SPACE:
                print("Social media handle cannot contain empty spaces.")
                social_media = input("Enter social media handle: ").strip()
        handle = input("Enter player handle: ").strip()
        if handle.lower() == "b":
            return "MY_TEAM"
        if handle.lower() == "q":
            return "QUIT"
        while validate_player_handle(handle, self.APILL.APIDATA) != Errors.OK:
            error = validate_player_handle(handle, self.APILL.APIDATA)
            if error == Errors.EMPTY:
                print("Player handle cannot be empty.")
            if error == Errors.HANDLE_CONTAINS_SPACE:
                print("Handle cannot contain empty spaces.")
            handle = input("Enter player handle: ").strip()
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
            print("r. Register for new tournament\nb. Back\nq. Quit")
            choice: str = self.menu_manager.prompt_choice(["r", "b", "q"])
            if choice == "r":
                while validate_players_in_teams(players) != Errors.OK:
                    error = validate_players_in_teams(players)
                    if error == Errors.PLAYERS_NOT_ENOUGH:
                        print("Not enough players on team to register.")
                    if error == Errors.PLAYERS_TOO_MANY:
                        print(
                            "Too many players on this team to register for a tournament."
                        )
                    enter_to_leave = input("Enter to exit")
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

    def show_modify_player_menu(self, player: Player):
        """
        Displays a menu of player attributes.
        The user selects one to change.
        """
        refresh_logo()
        while True:
            print(f"\n--- Editing Player: {player.name} ---")
            # Display current values so the user sees what they are changing
            # (Assuming your Player class has name, email, password, etc.)
            print(f"1. Change Name      (Current: {player.name})")
            print(f"2. Change Email     (Current: {player.email})")
            print(f"3. Change Address   (Current: {player.address})")
            print(f"4. Change Number    (Current: {player.phone_number})")
            print(f"5. Change Socials   (Current: {player.social_media})")
            print(f"6. Change Handle    [Current: {player.handle}]")
            print("S. Finish and Save")
            print("C. Cancel (Exit without saving)")

            selection = input("Select the data you want to change (1-6): ")

            if selection == "1":
                new_name = input("Enter new name: ").strip()
                error = validate_player_name(new_name)
                while error != Errors.OK:
                    if error == Errors.EMPTY:
                        print("Name cannot be empty")
                    if error == Errors.NAME_INCLUDE_NUMBERS:
                        print("Name cannot include numbers")
                    new_name = input("Enter new name: ").strip()
                    error = validate_player_name(new_name)
                print("Name updated locally.")

            elif selection == "2":
                new_email = input("Enter new email: ").strip()
                error = validate_player_email(new_email)
                while error != Errors.OK:
                    # Optional: Add email validation logic here
                    if error == Errors.EMPTY:
                        print("Email cannot be empty")
                    if error == Errors.EMAIL_NOT_CONTAINING_AT:
                        print("Email must contain @, example@example.com")

                    new_email = input("Enter new email: ").strip()
                    error = validate_player_email(new_email)
                player.email = new_email
                print("Email updated locally.")

            elif selection == "3":
                new_address = input("Enter new address: ").strip()
                error = validate_address(new_address)
                while error != Errors.OK:
                    if error == Errors.EMPTY:
                        print("Address cannot be empty")
                    if error == Errors.ADDRESS_ONLY_NUMBERS:
                        print("Address cannot be only numbers")
                    new_address = input("Enter new address: ").strip()
                    error = validate_address(new_address)
                player.address = new_address
                print("Address updated locally.")

            elif selection == "4":
                new_number = input("Enter new phone number: ").strip()
                error = validate_phone_number(new_number)
                while error != Errors.OK:
                    if error == Errors.NUMBER_NOT_CORRECT_LENGTH:
                        print("Phone number must be 7 digits")
                    if error == Errors.NUMBER_HAS_CHARACTERS:
                        print("Phone number cannot contain characters")
                    new_number = input("Enter new phone number: ").strip()
                    error = validate_phone_number(new_number)
                player.phone_number = new_number
                print("Address updated locally.")

            elif selection == "5":
                new_socials = input("Enter new social media handle: ").strip()
                error = validate_social_media(new_socials)

                while error != Errors.OK:
                    if error == Errors.EMPTY:
                        print("Social Media cannot be empty")
                    if error == Errors.HANDLE_CONTAINS_SPACE:
                        print("Social Media cannot contain spaces")

                    new_socials = input("Enter new social media handle: ").strip()
                    error = validate_social_media(new_socials)

                player.social_media = new_socials
                print("Socials updated locally.")

            elif selection == "6":
                new_handle = input("Enter new game handle: ").strip()
                error = validate_player_handle(new_handle, self.APILL.APIDATA)

                while error != Errors.OK:
                    if error == Errors.EMPTY:
                        print("Handle cannot be empty")
                    if error == Errors.HANDLE_CONTAINS_SPACE:
                        print("Handle cannot contain spaces")
                    new_handle = input("Enter new game handle: ").strip()
                    error = validate_player_handle(new_handle, self.APILL.APIDATA)
                player.handle = new_handle
                print("Game handle updated locally.")

            elif selection.lower() == "s":
                # Saves the information
                try:
                    self.APILL.modify_player(player)
                    print("Success! Player data saved to database.")
                    return "SHOW_MY_PLAYERS"  # Exit the loop
                except Exception as e:
                    print(f"Error saving data: {e}")

            elif selection.lower() == "c":
                print("Modification cancelled.")
                return "SHOW_MY_PLAYERS"  # Exit without calling modify_player

            else:
                print("Invalid selection. Please try again.")

    def show_my_team(self) -> str | None:
        """Shows the team captains team info"""
        team_name = self.menu_manager.team_name
        team = self.APILL.get_team_by_name(team_name)

        if team:
            print("YOUR TEAM: ", team.name)
            club = "CLUB"

            w_name = 20
            w_social = 15
            w_logo = 15
            w_captain = 15

            team_data_string = f"| CLUB | {team.name:^{w_name}} | {team.social_media:^{w_social}} |  {team.logo:^{w_logo}} |  {team.captain_handle:^{w_captain}} |"

            print("-" * len(team_data_string))
            print(team_data_string)
            print("-" * len(team_data_string))
            print("")
            print(
                "1. Add team to club \n2. Roster \n3. Edit team info \nb. Back \nq. Quit"
            )

            choice: str = self.menu_manager.prompt_choice(["1", "2", "3", "b", "q"])

            if choice == "1":
                return "ADD_TEAM_TO_CLUB"
            if choice == "2":
                return "SHOW_MY_PLAYERS"
            if choice == "3":
                return "EDIT_TEAM_INFO"

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
        registration = self.APILL.register_team_to_tournament(team, tournament)

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

    def show_edit_social_media(self):
        """Edits the social media for a team"""
        team = self.APILL.get_team_by_name(self.menu_manager.team_name)
        if team:
            print("Currrent social media: ", team.social_media)
            new_social_media = input("New social media: ")
            team.social_media = new_social_media

            new_team = self.APILL.modify_team_data(team)
            if new_team:
                print("Updated team info:")
                print("Name: ", new_team.name)
                print("Players:\n  ", *new_team.players, sep=" | ")
                print("Captain: ", new_team.captain_handle)
                print("Social Media: ", new_team.social_media)
                print("Logo: ", new_team.logo)
            else:
                print("Could not update team")
            print("")
            print("b. Back\nq. Quit")
            choice: str = self.menu_manager.prompt_choice(["b", "q"])
            if choice == "b":
                return "EDIT_TEAM_INFO"
            if choice == "b":
                return "QUIT"

    def show_edit_logo(self):
        """Edits the logo for a team"""
        print("EDIT_LOGO")
        team = self.APILL.get_team_by_name(self.menu_manager.team_name)
        if team:
            print("Currrent Logo: ", team.logo)
            logo = input("New Logo: ")
            team.logo = logo

            new_team = self.APILL.modify_team_data(team)
            if new_team:
                print("Updated team info:")
                print("Name: ", new_team.name)
                print("Players:\n  ", *new_team.players, sep=" | ")
                print("Captain: ", new_team.captain_handle)
                print("Social Media: ", new_team.social_media)
                print("Logo: ", new_team.logo)
            else:
                print("Could not update team")
            print("")
            print("b. Back\nq. Quit")
            choice: str = self.menu_manager.prompt_choice(["b", "q"])
            if choice == "b":
                return "EDIT_TEAM_INFO"
            if choice == "b":
                return "QUIT"
        pass

    def show_add_team_to_club(self):
        # TODO
        pass

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
        while validate_team_name(team_name, self.APILL.APIDATA) != Errors.OK:
            error = validate_team_name(team_name, self.APILL.APIDATA)
            if error == Errors.EMPTY:
                print("Team name cannot be empty.")
            if error == Errors.TEAM_NAME_TOO_LONG:
                print("Team name is too many characters.")
                team_name = input("Team name: ")
        # New team captain
        social_media = input("Social media: ")
        if social_media.lower() == "b":
            return "TEAM_CAPTAIN_MENU"
        if social_media.lower() == "q":
            return "QUIT"
        while validate_social_media(social_media) != Errors.OK:
            error = validate_social_media(social_media)
            if error == Errors.EMPTY:
                print("Social media handle cannot be empty.")
            if error == Errors.EMPTY:
                print("Social media handle cannot contain empty spaces.")
            social_media = input("Social media: ")
        team_logo = input("Input team logo in ASCII lettering: ")
        if team_logo.lower() == "q":
            return "QUIT"
        if team_logo.lower() == "b":
            return "TEAM_CAPTAIN_MENU"
        while validate_team_logo(team_logo) != Errors.OK:
            error = validate_team_logo(team_logo)
            if error == Errors.LOGO_EMPTY:
                print("Logo cannot be empty.")
                team_logo = input("Input team logo in ASCII lettering: ")
        team = self.menu_manager.team_name
        # new_team = Team(
        # team_name,
        # captain_handle,
        # social_media,
        # team_logo,
        # )
        pass

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

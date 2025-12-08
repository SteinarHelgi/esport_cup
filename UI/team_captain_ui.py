from LL.api_ll import APILL
from Models.player import Player
from Models.team_captain import TeamCaptain
import UI.functions as f


class TeamCaptainUI:
    def __init__(self, APILL: APILL, menu_manager) -> None:
        self.APILL = APILL
        self.menu_manager = menu_manager

    def show_create_player(self):
        print("Enter in thre required information or 'b' to Back and 'q' to Quit")
        name = input("Player's name: ").strip()
        if name.lower() == "b":
            return "MY_TEAM"
        if name.lower() == "q":
            return "QUIT"
        date_of_birth = input("Player's birthday (YYYY-MM-DD): ").strip()
        if date_of_birth.lower() == "b":
            return "MY_TEAM"
        if date_of_birth.lower() == "q":
            return "QUIT"
        address = input("Enter address: ").strip()
        if address.lower() == "b":
            return "MY_TEAM"
        if address.lower() == "q":
            return "QUIT"
        phone_number = input("Enter phone number: ").strip()
        if phone_number.lower() == "b":
            return "MY_TEAM"
        if phone_number.lower() == "q":
            return "QUIT"
        email = input("Enter email: ").strip()
        if email.lower() == "b":
            return "MY_TEAM"
        if email.lower() == "q":
            return "QUIT"
        social_media = input("Enter social media handle: ").strip()
        if social_media.lower() == "b":
            return "MY_TEAM"
        if social_media.lower() == "q":
            return "QUIT"
        handle = input("Enter player handle: ").strip()
        if handle.lower() == "b":
            return "MY_TEAM"
        if handle.lower() == "q":
            return "QUIT"
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
        team = self.APILL.get_team_by_name(self.menu_manager.team_name)
        captain = TeamCaptain(
            self.menu_manager.team_name, self.menu_manager.captain_handle
        )
        if team:
            tournaments = self.APILL.get_my_tournaments(team)
            print(f.format_tournament_table(tournaments))
            print("r. Register for new tournament\nb. Back\nq. Quit")
            choice: str = self.menu_manager.prompt_choice(["r", "b", "q"])
            if choice == "r":
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
                    print(f"{team} has been registered for {choice}")
                    back_or_quit = input("b to go back to tournament menu or q to quit")
                    if back_or_quit == "b":
                        return "MY_TOURNAMENTS_CAP"
                    if back_or_quit == "q":
                        return "QUIT"
                    else:
                        print("Invalid choice, valid choices are B and Q")
                        back_or_quit = input(
                            "b to go back to tournament menu or q to quit"
                        )

            if choice == "b":
                return "MY_TEAM"
            if choice == "q":
                return "QUIT"

    def show_modify_player_menu(self, player: Player):
        """
        Displays a menu of player attributes.
        The user selects one to change.
        """
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
                if new_name:
                    player.name = new_name
                    print("Name updated locally.")

            elif selection == "2":
                new_email = input("Enter new email: ").strip()
                if new_email:
                    # Optional: Add email validation logic here
                    player.email = new_email
                    print("Email updated locally.")

            elif selection == "3":
                new_address = input("Enter new address: ").strip()
                if new_address:
                    player.address = new_address
                    print("Address updated locally.")

            elif selection == "4":
                new_number = input("Enter new phone number: ").strip()
                if new_number:
                    player.phone_number = new_number
                    print("Address updated locally.")

            elif selection == "5":
                new_socials = input("Enter new social media handle: ").strip()
                if new_socials:
                    player.social_media = new_socials
                    print("Socials updated locally.")

            elif selection == "6":
                new_handle = input("Enter new game handle: ").strip()
                if new_handle:
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
        # TODO laga útlit
        players = self.APILL.get_players_in_team(self.menu_manager.team_name)
        valid_choices = []
        print(f.format_player_list(players))
        print("6. Add player: \n7. Remove player \nb. Back \nq.Quit")
        for i in range(len(players)):
            stringI = str(i + 1)
            valid_choices.append(stringI)
        choice: str = self.menu_manager.prompt_choice(
            valid_choices + ["6", "7", "b", "q"]
        )

        for element in valid_choices:
            if element == choice:
                player = self.show_player_view(players[int(element) - 1])
                return player
        if choice == "6":
            return "CREATE_PLAYER"
        if choice == "7":
            # TODO select_player_to_remove_menu
            pass
        if choice.lower() == "q":
            return "QUIT"
        if choice.lower() == "b":
            return "MY_TEAM"

    def show_player_view(self, player: Player):
        """takes in a player name and shows the menu for the player"""

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
            print("1. Edit player data")
            print("2. Hurt player emotionally")
            print("b. Back")
            print("q. Quit")

        choice: str = self.menu_manager.prompt_choice(["1", "2", "b", "q"])
        if choice == "1":
            # Modify player menuið
            return self.show_modify_player_menu(player)
        if choice == "b":
            return "SHOW_MY_PLAYERS"
        if choice == "q":
            return "QUIT"

    def show_register_team_to_tournament(self, team, tournament):
        # TODO
        self.team = team
        self.tournament = tournament
        registration = self.APILL.register_team_to_tournament(team, tournament)


    def show_update_team_data(self):
        # TODO b krafa
        pass

    def show_add_team_to_club(self):
        # TODO b krafa
        pass

    def show_create_team(self):
        # TODO c krafa
        pass

    #def add_information_about_team():
        #TODO
       # pass

    #def show_add_team_to_club():
        #TODO
        #pass
    

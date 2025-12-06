from LL.api_ll import APILL
from Models.player import Player
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
        print(
            f"PLAYER ADDED!\n{player_name} \n{player_handle} \n{player_social}")

        print("")
        print("b. Back \nq. Quit")
        choice: str = self.menu_manager.prompt_choice(["b", "q"])
        if choice == "b":
            return "MY_TEAM"
        if choice == "q":
            return "QUIT"

    def show_my_tournaments(self):
        team = self.APILL.get_team_by_name(self.menu_manager.team_name)
        if team:
            tournaments = self.APILL.get_my_tournaments(team)
            print(f.format_tournament_table(tournaments))
        print("b. Back\nq. Quit")
        choice: str = self.menu_manager.prompt_choice(["b", "q"])
        if choice == "b":
            return "MY_TEAM"
        if choice == "q":
            return "QUIT"

    def show_modify_player(self):
        # TODO
        pass

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

            team_data_string = f"| CLUB | {team.name:^{w_name}} | {team.social_media:^{w_social}} |  {team.logo:^{w_logo}} |  {team.captain_id:^{w_captain}} |"

            print("-" * len(team_data_string))
            print(team_data_string)
            print("-" * len(team_data_string))
            print("")
            print(
                "1. Add team to club \n2. Roster \n4. Edit team info \nb. Back \nq. Quit"
            )

            choice: str = self.menu_manager.prompt_choice(["1", "2", "3", "4", "b", "q"])
            if choice == "1":
                return "ADD_TEAM_TO_CLUB"
            if choice == "2":
                return "SHOW_MY_PLAYERS"
            if choice == "3":
                return "MY_TOURNAMENTS_CAP"
            if choice == "4":
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
            # select_player_to_remove_menu
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
            # TODO create edit player menu
            return "EDIT_PLAYER"
        if choice == "b":
            return "SHOW_MY_PLAYERS"
        if choice == "q":
            return "QUIT"

    def show_register_team_to_tournament(self):
        # TODO

        # self.menu_manager.team_name = "Pepsi Max Punishers"
        # team = self.APILL.get_team_by_name(self.menu_manager.team_name)
        # if team:
        #     tournaments = self.APILL.get_available_tournaments(team)
        #     print(*tournaments)

        # print("These are the tournaments available for registration \nSelect a tournament to register for")
        # kalla i LL register for tournament

        pass

    def show_update_team_data(self):
        # TODO b krafa
        pass

    def show_add_team_to_club(self):
        # TODO b krafa
        pass

    def show_create_team(self):
        # TODO c krafa
        pass

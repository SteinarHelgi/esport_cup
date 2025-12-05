from datetime import date
from operator import add
from LL.api_ll import APILL
from Models.player import Player
from UI.Menus import print_my_team_menu
import UI.functions as f


class TeamCaptainUI:
    def __init__(self, APILL: APILL, menu_manager) -> None:
        self.APILL = APILL
        self.menu_manager = menu_manager

    def show_create_player(self):
        name = input("Player's name: ").strip()
        date_of_birth = input("Player's birthday (YYYY-MM-DD): ").strip()
        address = input("Enter address: ").strip()
        phone_number = input("Enter phone number: ").strip()
        email = input("Enter email: ").strip()
        social_media = input("Enter social media handle: ").strip()
        handle = input("Enter player handle: ").strip()
        team = self.menu_manager.team_name
        new_player = Player(name, date_of_birth, address, phone_number, email, social_media, handle, team)
        self.APILL.create_player(new_player)

        print(
            f"------ \nNew player created: {name}\n{date_of_birth}\n{address}\n{phone_number}\n{email}\n{social_media}\n{handle}\n{team} "
        )

    def show_my_tournaments(self):
        # TODO listi af motum
        # option i register for tournament
        pass

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
                "1. Add team to club \n2. Roster \n3. Edit team info \nb. Back \nq. Quit"
            )

            choice: str = self.menu_manager.prompt_choice(["1", "2", "3", "b", "q"])
            if choice == "1":
                return "ADD_TEAM_TO_CLUB"
            if choice == "2":
                return "SHOW_MY_PLAYERS"
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
        choice: str = self.menu_manager.prompt_choice(valid_choices + ["6", "7","b", "q"])

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
        # Kall i upcoming sem hafa plass og lista þau upp
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

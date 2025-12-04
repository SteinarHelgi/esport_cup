from datetime import date
from LL.api_ll import APILL
from Models.player import Player
from UI.Menus import print_my_team_menu


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


        new_player_id = 67  # call create_player from LL here
        print(
            f"------ \nNew player created with ID: {new_player_id}\n{name}\n{date_of_birth}\n{address}\n{phone_number}\n{email}\n{social_media}\n{handle}\n{team} "
        )

    def show_my_tournaments(self):
        #TODO listi af motum
        #option i register for tournament
        pass

    def show_modify_player(self):
        # TODO
        pass

    def show_my_team(self) -> str | None:
        team_name = self.menu_manager.team_name
        my_team = self.APILL.get_team_by_name(team_name)

        if my_team:
            print("YOUR TEAM: ", my_team.name)
            club = "TODO"
            team_name = my_team.name
            link = my_team.social_media
            logo = my_team.logo
            captain = my_team.captain_id
            print(f"{club}\n {team_name} \n{link}\n {logo}\n {captain}")
            print(
                "1. Add team to club \n2. Roster \n3. Edit team info \nb. Back \nq. Quit"
            )
            choice: str = self.menu_manager.prompt_choice(["1", "2", "3", "b", "q"])
            if choice == "1":
                return "ADD_TEAM_TO_CLUB"
            if choice == "2":
                return "SHOW_MY_PLAYERS"

    def show_my_players(self):
        # TODO laga útlit
        players = self.APILL.get_players_in_team(self.menu_manager.team_name)
        print(format_player_list(players))
        print("6. Add player: \n7. Remove player \nb. Back \nq.Quit")
        choice: str = self.menu_manager.prompt_choice(["1", "2", "3","4","5","6","7", "b", "q"])
        if choice == "6":
            self.show_create_player()
        if choice == "7":
            #select_player_to_remove_menu
            pass
        if choice.lower() == "q":
            return "QUIT"
        if choice.lower() == "b":
            return "MY TEAM"

    def show_player_view(self, player_name: str):
        """takes in a player name and shows the menu for the player"""
        # TODO GERA ÞETTA FALL self.APILL.get_player_by_name(player_name: name):

        player = Player(
            "Steinar Helgi Halldórsson",
            "1999-10-06",
            "Dofraborgir 15",
            "766-6454",
            "steinarhelgi@outlook.com",
            "@steinarhh",
            "@blabliblu",
            "TEAMNAMEBABY",
        )

        print(f"{player.name.upper()}  |  {player.handle} ")
        print("--------------------")
        print(f"    DATE OF BIRTH: {player.date_of_birth}")
        print(f"    ADDRESS: {player.address}")
        print(f"    PHONE: {player.phone_number}")
        print(f"    EMAIL: {player.email}")
        print(f"    HANDLE: {player.handle}")
        print(f"    SOCIAL MEDIA: {player.social_media}")
        print(f"    TEAM: {player.team_name}")
        print("")
        print("1. Edit player data")
        print("2. Hurt player emotionally")
        choice: str = self.menu_manager.prompt_choice(["1", "2"])
        if choice == "1":
            # TODO create edit player menu
            return "EDIT_PLAYER"

    def show_register_team_to_tournament(self):
        # TODO
        #Kall i upcoming sem hafa plass og lista þau upp
        #kalla i LL register for tournament
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

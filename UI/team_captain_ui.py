from LL.api_ll import APILL
from UI.Menus import new_player_menu, print_my_team_menu
from UI.functions import format_player_list


class TeamCaptainUI:
    def __init__(self, APILL: APILL, menu_manager) -> None:
        self.APILL = APILL
        self.menu_manager = menu_manager

    def show_create_player(self):
        name = input("Player's name: ").strip()
        date_of_birth = input("Player's birthday (YYYY-MM-DD): ").strip()
        
        team = self.menu_manager.team_name

        player_data = {"name": name, "date_of_birth": date_of_birth, "team": team}

        new_player_id = 14  # call create_player from LL here
        print(
            f"------ \nNew player created with ID: {new_player_id}\n{player_data['name']}\n{player_data['date_of_birth']}\n{player_data['team']} "
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

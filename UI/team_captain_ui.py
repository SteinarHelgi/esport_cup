from LL.api_ll import APILL
from UI.Menus import print_my_team_menu


class TeamCaptainUI:
    def __init__(self, APILL: APILL) -> None:
        self.APILL = APILL

    def show_create_player(self):
        name = input("Player's name: ").strip()
        date_of_birth = input("Player's birthday (YYYY-MM-DD): ").strip()
        team = input("Player's team: ").strip()

        player_data = {"name": name, "date_of_birth": date_of_birth, "team": team}

        new_player_id = 14  # call create_player from LL here
        print(
            f"------ \nNew player created with ID: {new_player_id}\n{player_data['name']}\n{player_data['date_of_birth']}\n{player_data['team']} "
        )

    def show_modify_player(self):
        # TODO
        pass

    def show_my_team(self):
        print_my_team_menu()
        valid_options = ["1", "2", "3", "b", "q"]
        option = input("?")
        for option in valid_options:
            if option == "1":
                return "add_team_to_club"
            if option == "2":
                return "roster_menu"
            if option == "3":
                return "edit_team_info_menu"
            if option == "b":
                return "back_button"
            if option == "q":
                return "quit"
        # TODO
        pass

    def show_my_tournaments(self):
        
        # TODO
        pass

    def show_register_team_to_tournament(self):
        # TODO
        pass

    def show_update_team_data(self):
        # TODO
        pass

    def show_add_team_to_club(self):
        # TODO
        pass

    def show_create_team(self):
        # TODO
        pass

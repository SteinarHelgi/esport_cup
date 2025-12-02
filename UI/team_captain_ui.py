from LL.api_ll import APILL


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

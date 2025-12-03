from LL.api_ll import APILL
from Models.models import Team
from UI import menu_manager
from UI.menu_manager import MenuManager



def print_back_and_quit():
    print("")
    print("b. Back")
    print("q. Quit")


class UserUI:
    def __init__(self, APILL: APILL, menu_manager: MenuManager) -> None:
        self.APILL = APILL
        self.menu_manager = menu_manager

    def show_teams(self):
        teams = self.APILL.get_all_teams()
        print("Teams:")
        for id, team in teams.items():
            name = team[0]
            logo = team[2]
            teamCaptain = team[3]
            website = team[4]
            club = team[5]
            points = team[6]
            print("-----------------------------------------------------------")
            print(f"{id}:   {name} {logo} {teamCaptain} {website} {club} {points}")
        print_back_and_quit()

    def show_tournaments(self):
        self.APILL.get_all_tournaments()
        valid_options = ["1", "2", "3", "b", "q"]
        choice: str = self.menu_manager.prompt_choice(valid_options)

        for choice in valid_options:
            if choice == "1":
                return "ONGOING_TOURNAMENTS"
            if choice == "2":
                return "UPOMING_TOURNAMENTS"
            if choice == "3":
                return  # Past_tournaments
            if choice == "b":
                return  # back_button
            if choice == "q":
                return  # quit

    def show_current_tournaments(self):
        tournaments = self.APILL.get_all_tournaments()
        print("Tournaments:")
        for tournament in tournaments:
            print(tournament)
        print_back_and_quit()

    def show_upcoming_tournaments(self):
        # TODO
        pass

    def show_past_tournaments(self):
        # TODO
        pass

    def show_players(self, team: Team):
        # Todo
        pass

    def show_statistics(self):
        # TODO
        pass

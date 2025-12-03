from LL.api_ll import APILL
from Models.models import Team


def print_back_and_quit():
    print("")
    print("b. Back")
    print("q. Quit")


class UserUI:
    def __init__(self, APILL: APILL) -> None:
        self.APILL = APILL

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
        valid_options = ["1", "2", "3", "b", "q"]
        option = "?"
        for option in valid_options:
            if option == "1":
                return  # ongoing_tournaments
            if option == "2":
                return  # upcoming_tournaments
            if option == "3":
                return  # Past_tournaments
            if option == "b":
                return  # back_button
            if option == "q":
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

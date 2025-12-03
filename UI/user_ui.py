from LL.api_ll import APILL
from Models.models import Team


def print_back_and_quit():
    print("")
    print("b. Back")
    print("q. Quit")


class UserUI:
    def __init__(self, APILL: APILL, menu_manager) -> None:
        self.APILL = APILL
        self.menu_manager = menu_manager

    def show_teams(self):
        pass

    def show_tournaments(self):
        tournaments = self.APILL.get_all_tournaments()
        valid_options = ["1", "2", "3", "b", "q"]

        print("1. Ongoing tournaments\n2. Upcoming tournaments")

        choice: str = self.menu_manager.prompt_choice(valid_options)
        print("choice:", choice)

        if choice == "1":
            return "ONGOING_TOURNAMENTS"
        elif choice == "2":
            return "UPCOMING_TOURNAMENTS"
        elif choice == "3":
            return  # Past_tournaments
        elif choice == "b":
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
        print("hello upcoming")

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

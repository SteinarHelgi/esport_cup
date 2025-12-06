from UI.main_ui import MainUI
from IO.club_data import ClubData


def main():
    main_ui = MainUI()
    main_ui.menu_manager.team_captain_ui.show_my_tournaments()


main()

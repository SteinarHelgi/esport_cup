from UI.main_ui import MainUI
from IO.club_data import ClubData


def main():
    club = ClubData()
    clubs = club.get_club_data()
    for cl in clubs:
        print(cl)


main()

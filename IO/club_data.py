import csv


class ClubData:

    def __init__(self):
        self._filepath: str = "\Data\club.csv"
    

    def get_all_club_data(self) -> list[list[str]]:
        clubs = []

from IO.api_data import APIDATA
from Models.models import Team, Club


class ClubLL:
    def __init__(self, api_data: APIDATA, main_ll) -> None:
        """Initializes the ClubLL logic laywer with access to APIDATA"""
        self.APIDATA = api_data
        self.MAINLL = main_ll

    def add_team_to_club(self, team: Team, club: Club):
        """Adds a team to the club with the given ID"""
        self.APIDATA.add_team_to_club(team, club)

    def get_all_club_data(self) -> list[Club]:
        """Returns all clubs in the system."""
        return self.APIDATA.get_all_club_data()

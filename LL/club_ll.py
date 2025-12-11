from Models.team import Team
from IO.api_data import APIDATA
from Models.club import Club


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

    def get_club_by_name(self, club_name: str) -> Club | None:
        all_clubs = self.get_all_club_data()
        for club in all_clubs:
            if club.name == club_name:
                return club

    def get_all_teams_in_a_club(self, club_id) -> list[Team]:
        """Returns all teams that belong to the club with the given ID"""
        clubs = self.APIDATA.get_all_club_data()
        all_teams_with_semicolon: str = ""
        # Find the club and its team-list string
        for club in clubs:
            if club.id == club_id:
                all_teams_with_semicolon = club.teams
                break
        # Split the team names string into a list
        all_teams_names: list[str] = all_teams_with_semicolon.split(";")

        teams_in_club: list[Team] = []
        teams = self.APIDATA.get_all_team_data()
        for team in teams:
            if team.name in all_teams_names:
                teams_in_club.append(team)
        return teams_in_club

from Models.team import Team
from IO.api_data import APIDATA
from Models.club import Club


class ClubLL:
    def __init__(self, api_data: APIDATA, main_ll) -> None:
        """"""
        self.APIDATA = api_data
        self.MAINLL = main_ll

    def add_team_to_club(self, team: Team, club_id: str):
        self.APIDATA.add_team_to_club(team, club_id)

    def get_all_club_data(self) -> list[Club]:
        return self.APIDATA.get_all_club_data()

    def get_all_teams_in_a_club(self, club_id) -> list[Team]:
        clubs = self.APIDATA.get_all_club_data()
        all_teams_with_semicolon: str = ""
        for club in clubs:
            if club.id == club_id:
                all_teams_with_semicolon = club.teams
                break
        all_teams_names: list[str] = all_teams_with_semicolon.split(";")

        teams_in_club: list[Team] = []
        teams = self.APIDATA.get_all_team_data()
        for team in teams:
            if team.name in all_teams_names:
                teams_in_club.append(team)
        return teams_in_club

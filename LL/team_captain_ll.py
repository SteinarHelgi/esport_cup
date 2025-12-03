from Models.team import Team
from IO.api_data import APIDATA


class TeamCaptainLL:
    def __init__(self, APIDATA: APIDATA):
        self.id = 0
        self.APIDATA = APIDATA

    def create_player(self):
        # TODO
        pass

    def modify_player(self):
        # TODO
        pass

    def create_new_team(self):
        # TODO
        pass

    def add_team_to_club(self):
        # TODO
        pass

    def modify_team_info(self):
        # TODO
        pass

    def register_team_to_tournament(self):
        # TODO
        pass

    def get_players_in_team(self, team: Team):
        teams = self.APIDATA.get_team_data()
        players = self.APIDATA.getpl
        return teams

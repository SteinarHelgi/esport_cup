from Models.player import Player
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

    def get_players_in_team(self, team_name: str) -> list[Player]:
        # TEAM
        # id name captain_id social_media logo

        # PLAYERS
        # id name dateofbirth address phone email social handle team_name

        players_in_team = []

        players = self.APIDATA.get_all_player_data()
        for player in players:
            if player.team == team_name:
                players_in_team.append(player)

        return players_in_team

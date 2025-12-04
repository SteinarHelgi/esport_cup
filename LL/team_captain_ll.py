from Models.player import Player
from Models.team import Team
from IO.api_data import APIDATA
from datetime import datetime


class TeamCaptainLL:
    def __init__(self, APIDATA: APIDATA, captain):
        self.id = 0
        self.APIDATA = APIDATA
        self.captain = captain

    def create_player(self, player: Player) -> Player:
        """Creates new player and saves him in the csv file"""
        
        #Fetches all parameters of player
        name: str = player.name
        date_of_birth: datetime.datetime = player.date_of_birth
        address: str = player.address
        phone_number: str = player.phone_number
        email: str = player.email
        social_media: str = player.social_media
        handle: str = player.handle
        team_name: str = player.team_name

        #Fetch all player data
        current_players = self.APIDATA.get_all_player_data(self)

        #Checking if player handle is available
        for p in current_players:
            if p.handle == player.handle:
                raise ValueError()

        #Find next player id
        if current_players:
            next_id: int = max(int(player.id) for player in current_players) + 1
        else:
            next_id = 1
        player_id = str(next_id)

        player.set_id(player_id)

        #Fetch team id from captain
        team_id = self.captain.team_id

        # Búa til nýjan Player
        new_player = Player(
            player_id,
            name,
            date_of_birth,
            address,
            phone_number,
            email,
            social_media,
            handle,
            team_id
        )

        # Vista leikmann í gegnum IO-layer
        self.APIDATA.store_player_data(new_player)

        return new_player


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

    def get_team_by_captain_id(self, captain_id) -> Team | None:
        teams = self.APIDATA.get_all_team_data()

        for team in teams:
            if team.captain_id == captain_id:
                print(team.captain_id, captain_id)
                return team
        return None

    def get_players_in_team(self, team_name: str) -> list[Player]:
        # TEAM
        # id name captain_id social_media logo

        # PLAYERS
        # id name dateofbirth address phone email social handle team_name

        players_in_team = []

        players = self.APIDATA.get_all_player_data()
        for player in players:
            if player.team_name == team_name:
                players_in_team.append(player)

        return players_in_team

    def get_team_by_name(self, name: str) -> Team | None:
        teams = self.APIDATA.get_all_team_data()
        for team in teams:
            if team.name == name:
                return team

    def get_player_by_name(self, name: str) -> Player | None:
        players = self.APIDATA.get_all_player_data()
        for player in players:
            if player.name == name:
                return name

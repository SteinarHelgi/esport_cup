from Models.player import Player
from Models.team import Team
from IO.api_data import APIDATA
from datetime import datetime


class TeamCaptainLL:
    def __init__(self, APIDATA: APIDATA, captain):
        self.id = 0
        self.APIDATA = APIDATA
        self.captain = captain

    def create_player(
            self,
            name: str,
            date_of_birth: str,
            address: str,
            phone: str,
            email: str,
            handle: str,
            link: str,
        ) -> Player:
        """Býr til nýjan leikmann í liði captains og vistar inn í skránni."""

        if name.strip() == "":
            raise ValueError("Nafn má ekki vera tómt")
        if date_of_birth.strip() == "":
            raise ValueError("Fæðingardagur má ekki vera tómur")
        if address.strip() == "":
            raise ValueError("Heimilsfang má ekki vera tómt")
        if phone.strip() == "":
            raise ValueError("Símanúmer má ekki vera tómt")
        if email.strip() == "":
            raise ValueError("Netfang má ekki vera tómt")
        if handle.strip() == "":
            raise ValueError("Handle má ekki vera tómt")
        
        # Athuga að date_of_birth sé á réttu formi
        try: 
            date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Fæðingardagur þarf að vera á forminu YYYY-MM-DD.")
    
        # Ná í alla núverandi leikmenn úr IO-layer
        players = self.APIDATA.get_all_player_data()

        # Athuga hvort handle sé þegar í notkun
        for p in players:
            if p.handle == handle:
                raise ValueError("Þetta handle er þegar í notkun")

        # Finna næsta player_id
        next_id = 1
        for p in players:
            try:
                current_id = int(p.player_id)
                if current_id >= next_id:
                    next_id = current_id + 1
            except ValueError:
                pass

        player_id = str(next_id)

        # Ná í liðið út frá team_id hjá captain
        team_id = self.captain.team_id
    
        # Búa til nýjan Player
        new_player = Player(
            player_id,
            name,
            date_of_birth,
            address,
            phone,
            email,
            link,
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
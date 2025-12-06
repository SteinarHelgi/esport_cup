from Models.player import Player
from Models.team import Team
from IO.api_data import APIDATA
from datetime import datetime
from Models.tournament import Tournament
from Models.team_registry import TeamRegistry
from Models.team_captain import TeamCaptain

class TeamCaptainLL:
    def __init__(self, APIDATA: APIDATA):
        self.id = 0
        self.APIDATA = APIDATA

    def create_player(self, player: Player) -> Player:
        """Creates new player and saves him in the csv file"""

        # Fetch all player data
        current_players = self.APIDATA.get_all_player_data()

        # Checking if player handle is available
        for p in current_players:
            if p.handle == player.handle:
                raise ValueError()

        # Find next player id
        nums = [
            int(p.id[1:])
            for p in current_players if p.id.startswith(("p", "P")) and p.id[1:].isdigit
        ]
        
        next_num = max(nums) + 1 if nums else 1
        new_id = f"P{next_num:03d}"

        player.id = new_id
        player.player_id = new_id

        # Vista leikmann í gegnum IO-layer
        self.APIDATA.store_player_data(player)

        return player

    def modify_player(self, player: Player):
        self.APIDATA.modify_player_data(player)
    
    def delete_player(self, player_id: str):
        self.APIDATA.delete_player_data(player_id)

    def create_new_team(self, team: Team) -> Team:
        """Creates new team and saves it in the csv file."""

        name: str = team.name
        captain_id: str = team.captain_id
        social_media: str | None = team.social_media
        logo: str = team.logo

        current_teams = self.APIDATA.get_all_team_data()

        # checking if team name is available
        for t in current_teams:
            if t.name == team.name:
                raise ValueError
            
        # Find next team id
        if current_teams:
            next_id: int = max(int(team.id) for team in current_teams) + 1
        else:
            next_id = 1
        id = str(next_id)

        team.set_id(id)

        new_team = Team(
            id,
            name,
            captain_id,
            social_media,
            logo
        )

        self.APIDATA.store_team_data(new_team)

        return new_team
    

    def add_team_to_club(self, team: Team, club_id: str):
        # TODO
        pass

    def modify_team_info(self):
        # TODO
        pass

    def register_team_to_tournament(self, team: Team, tournament: Tournament) -> None:
        team_id: str = team.id
        tournament_id: str = tournament.id
        team_registry = TeamRegistry(team_id, tournament_id)
        new_team_registry = self.APIDATA.store_team_registry_data(team_registry)


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
                return player
    

    def show_all_tournaments_for_captain(self, captain: TeamCaptain) -> TeamCaptain:
        """Finds all tournaments the captain's team is registered for and stores them in captain.tournaments before returning the captain."""
        captain.tournaments = []

        # Find the team captain is registered for
        team = self.get_team_by_captain_id(captain.id)
        if team is None:
            return captain
        
        # Get all team registrations and all tournaments
        team_registry = self.APIDATA.get_all_team_registry_data()
        tournaments = self.APIDATA.get_all_tournament_data()

        # For each registration that matches this team, find the corresponding tournament
        for registry in team_registry:
            if registry.team_id == team.id:
                for tournament in tournaments:
                    if tournament.id == registry.tournament_id:
                        if tournament not in captain.tournaments:
                            captain.tournaments.append(tournament)

        return captain
    

    def show_all_open_tournaments_for_captain(self,captain: TeamCaptain) -> TeamCaptain:
        """Finds all tournaments the captain's team can register for and stores them in captain.available_tournaments before returning the captain."""
        
        captain.available_tournaments = []

        # Find the team captain is registered for
        team = self.get_team_by_captain_id(captain.id)
        if team is None:
            return captain
        
        # Get all team registrations and all tournaments
        team_registry = self.APIDATA.get_all_team_registry_data()
        tournaments = self.APIDATA.get_all_tournament_data()

        now = datetime.now()

        # For each tournament, check if the team can register
        for tournament in tournaments:
            # Only look at tournaments that have not started yet
            if tournament.start_date <= now:
                continue
            # Check if the team is already registered
            is_registered = False
            for registry in team_registry:
                if registry.team_id == team.id and registry.tournament_id == tournament.id:
                    is_registered = True
                    break
            
            # If not registered, add to available tournaments
            if not is_registered:
                captain.available_tournaments.append(tournament)

        return captain
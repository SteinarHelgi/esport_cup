from Models.player import Player
from Models.team import Team
from IO.api_data import APIDATA
from datetime import datetime
from Models.tournament import Tournament
from Models.team_registry import TeamRegistry
from Models.team_captain import TeamCaptain
from Models.club import Club



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

        player.set_id(new_id)

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
        captain_id: str = team.captain_handle
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

        new_team = Team(name, captain_id, social_media, logo)

        self.APIDATA.store_team_data(new_team)

        return new_team

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


    def modify_team_data(self, team: Team):
        self.APIDATA.modify_team_data(team)
        pass

    def register_team_to_tournament(self, team: Team, tournament: Tournament) -> None:
        team_id: str = team.id
        tournament_id: str = tournament.id
        team_name: str = team.name
        tournament_name: str = tournament.name
        team_registry = TeamRegistry(team_id, tournament_id, team_name, tournament_name)
        new_team_registry = self.APIDATA.store_team_registry_data(team_registry)

    def get_my_tournaments(self, team: Team) -> list[Tournament]:
        team_tournament_registry = self.APIDATA.get_all_team_registry_data()
        tournaments_ids = []
        for team_tournament in team_tournament_registry:
            if team.id == team_tournament.team_id:
                tournaments_ids.append(team_tournament.tournament_id)
        tournaments = []
        for tournament_id in tournaments_ids:
            tournament = self.get_tournament_by_id(tournament_id)
            tournaments.append(tournament)
        return tournaments

    def get_tournament_by_id(self, tournament_id: str) -> Tournament | None:
        tournaments = self.APIDATA.get_all_tournament_data()
        matches = self.APIDATA.get_all_match_data()
        for tournament in tournaments:
            if tournament.id == tournament_id:
                for match in matches:
                    if match.tournament_id == tournament.id:
                        tournament.add_match(match)

                return tournament

    def get_team_by_captain_handle(self, captain_handle) -> Team | None:
        teams = self.APIDATA.get_all_team_data()

        for team in teams:
            if team.captain_handle == captain_handle:
                print(team.captain_handle, captain_handle)
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
    

    def show_all_tournaments_for_captain(self, captain: TeamCaptain) -> list[Tournament]:
        """Returns a list of tournaments that the captain's team is registered for."""
        tournaments_for_captain = []

        # Find the team captain is registered for
        team = self.get_team_by_captain_handle(captain.handle)
        if team is None:
            return tournaments_for_captain
        
        # Get all team registrations and all tournaments
        team_registry = self.APIDATA.get_all_team_registry_data()
        tournaments = self.APIDATA.get_all_tournament_data()

        # For each registration that matches this team, find the corresponding tournament
        for registry in team_registry:
            if registry.team_id == team.id:
                for tournament in tournaments:
                    if tournament.id == registry.tournament_id:
                        if tournament not in tournaments_for_captain:
                            tournaments_for_captain.append(tournament)

        return tournaments_for_captain
    

    def show_all_open_tournaments_for_captain(self, captain: TeamCaptain) -> list[Tournament]:
        """
        Returns a list of tournaments that the captain's team can register for.
        A tournament is considered open if it has not started yet and the team
        is not already registered for it.
        """
        
        open_tournaments = []

        # Find the team captain is registered for
        team = self.get_team_by_captain_handle(captain.handle)
        if team is None:
            return open_tournaments
        
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
            
            # If not registered, add to open tournaments list
            if not is_registered:
                open_tournaments.append(tournament)

        return open_tournaments
    

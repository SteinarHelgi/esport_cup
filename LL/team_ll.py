from IO.api_data import APIDATA
from Models.models import Team, Tournament, Player, TeamRegistry

MIN_PLAYERS_PER_TEAM = 3
MAX_PLAYERS_PER_TEAM = 5


class TeamLL:
    def __init__(self, api_data: APIDATA, main_ll):
        self.APIDATA = api_data
        self.MAINLL = main_ll

    def get_all_teams(self) -> list[Team]:
        teams = self.APIDATA.get_all_team_data()
        players = self.APIDATA.get_all_player_data()
        for team in teams:
            for player in players:
                if player.team_name == team.name:
                    team.add_player(player.handle)
        return teams

    def get_all_players(self) -> list:
        players = self.APIDATA.get_all_player_data()
        return players

    def get_my_tournaments(self, team: Team) -> list[Tournament]:
        team_tournament_registry = self.APIDATA.get_all_team_registry_data()
        tournaments_ids = []
        for team_tournament in team_tournament_registry:
            if team.id == team_tournament.team_id:
                tournaments_ids.append(team_tournament.tournament_id)
        tournaments = []
        for tournament_id in tournaments_ids:
            tournament = self.MAINLL.tournament_ll.get_tournament_by_id(tournament_id)
            tournaments.append(tournament)
        return tournaments

    def create_player(self, player: Player) -> Player:
        """Creates new player and saves him in the csv file"""

        # Fetch all player data
        current_players = self.APIDATA.get_all_player_data()

        # Max 5 players in a team
        players_in_team = [
            p for p in current_players if p.team_name == player.team_name
        ]
        if len(players_in_team) >= 5:
            raise ValueError()

        # Checking if player handle is available
        for p in current_players:
            if p.handle == player.handle:
                raise ValueError()

        # Find next player id
        nums = [
            int(p.id[1:])
            for p in current_players
            if p.id.startswith(("p", "P")) and p.id[1:].isdigit
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

    def modify_team_data(self, team: Team) -> Team | None:
        return self.APIDATA.modify_team_data(team)

    def register_team_to_tournament(self, team: Team, tournament: Tournament) -> None:
        players_in_team = self.get_players_in_team(team.name)
        num_players = len(players_in_team)
        if num_players < MIN_PLAYERS_PER_TEAM or num_players > MAX_PLAYERS_PER_TEAM:
            raise ValueError
        team_id: str = team.id
        tournament_id: str = tournament.id
        team_name: str = team.name
        tournament_name: str = tournament.name
        team_registry = TeamRegistry(team_id, tournament_id, team_name, tournament_name)
        new_team_registry = self.APIDATA.store_team_registry_data(team_registry)

    def get_team_by_id(self, id) -> Team | None:
        teams = self.get_all_teams()
        for team in teams:
            if team.id == id:
                return team

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
        players = self.get_players_in_team(name)
        for team in teams:
            if team.name == name:
                for player in players:
                    team.add_player(player.name)
                return team

    def get_player_by_name(self, name: str) -> Player | None:
        players = self.APIDATA.get_all_player_data()
        for player in players:
            if player.name == name:
                return player

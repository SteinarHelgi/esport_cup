from IO.contact_person_data import ContactPersonData
from IO.player_data import PlayerData
from IO.team_data import TeamData
from IO.tournament_data import TournamentData
from IO.game_data import GameData
from IO.club_data import ClubData
from IO.match_data import MatchData
from IO.team_registry_data import TeamRegistryData
from Models.models import ContactPerson
from Models.team import Team
from Models.tournament import Tournament
from Models.game import Game
from Models.player import Player
from Models.club import Club
from Models.match import Match
from Models.team_registry import TeamRegistry


class APIDATA:
    def __init__(self) -> None:
        self.club_data = ClubData()
        self.contact_person_data = ContactPersonData()
        self.game_data = GameData()
        self.match_data = MatchData()
        self.player_data = PlayerData()
        self.team_data = TeamData()
        self.tournament_data = TournamentData()
        self.team_registry_data = TeamRegistryData()

    def get_all_club_data(self) -> list[Club]:
        return self.club_data.get_all_club_data()

    def store_club_data(self, club: Club):
        return self.club_data.store_club_data(club)

    def get_all_contact_person_data(self) -> list[ContactPerson]:
        return self.contact_person_data.get_all_contact_person_data()

    def store_contact_person_data(self, contact: ContactPerson):
        return self.contact_person_data.store_contact_person_data(contact)

    def get_all_game_data(self) -> list[Game]:
        return self.game_data.get_all_game_data()

    def store_game_data(self, game: Game):
        return self.game_data.store_game_data(game)

    def get_all_match_data(self) -> list[Match]:
        return self.match_data.get_all_match_data()

    def store_match_data(self, match: Match):
        return self.match_data.store_match_data(match)

    def get_all_player_data(self) -> list[Player]:
        return self.player_data.get_all_player_data()

    def store_player_data(self, player: Player):
        return self.player_data.store_player_data(player)

    def get_all_team_data(self) -> list[Team]:
        return self.team_data.get_all_team_data()

    def store_team_data(self, team: Team):
        return self.team_data.store_team_data(team)

    def get_all_tournament_data(self) -> list[Tournament]:
        return self.tournament_data.get_all_tournament_data()

    def store_tournament_data(self, tournament: Tournament):
        return self.tournament_data.store_tournament_data(tournament)

    def get_all_team_registry_data(self) -> list[TeamRegistry]:
        return self.team_registry_data.get_all_team_registry_data()

    def store_team_registry_data(self, team_registry: TeamRegistry):
        return self.team_registry_data.store_team_registry_data(team_registry)

    def modify_player_data(self, player: Player):
        return self.player_data.modify_player_data(player)

    def delete_player_data(self, player_id: str):
        return self.player_data.delete_player_data(player_id)

    def delete_tournament_data(self, tournament_id: str):
        return self.tournament_data.delete_tournament_data(tournament_id)

    def register_match_results(
        self, match_id: str, home_score: int, away_score: int, completed_match: str
    ):
        return self.match_data.register_match_results(
            match_id, home_score, away_score, completed_match
        )

    def modify_team_data(self, team: Team) -> Team | None:
        return self.team_data.modify_team_data(team)

    def add_team_to_club(self, team: Team, club_id: str):
        return self.club_data.add_team_to_club(team, club_id)

    def give_player_points(self, handle: str, points: int):
        return self.player_data.give_player_points(handle, points)

    def give_team_points(self, team_name: str, points: int):
        return self.team_data.give_team_points(team_name, points)

    def give_club_points(self, club_name: str, points: int):
        return self.club_data.give_club_points(club_name, points)

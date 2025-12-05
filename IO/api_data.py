from IO.contact_person_data import ContactPersonData
from IO.player_data import PlayerData
from IO.team_data import TeamData
from IO.tournament_data import TournamentData
from IO.game_data import GameData
from IO.club_data import ClubData
from IO.match_data import MatchData
from Models.models import ContactPerson
from Models.team import Team
from Models.tournament import Tournament
from Models.game import Game
from Models.player import Player
from Models.club import Club
from Models.match import Match


# Steinar

class APIDATA:
    def __init__(self) -> None:
        self.club_data = ClubData()
        self.contact_person_data = ContactPersonData()
        self.game_data = GameData()
        self.match_data = MatchData()
        self.player_data = PlayerData()
        self.team_data = TeamData()
        self.tournament_data = TournamentData()

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
from IO.contact_person_data import ContactPersonData
from IO.player_data import PlayerData
from IO.team_data import TeamData
from IO.tournament_data import TournamentData
from IO.game_data import GameData

from Models.models import ContactPerson
from Models.team import Team
from Models.tournament import Tournament
from Models.game import Game
from Models.player import Player

# Steinar


class APIDATA:
    def __init__(self) -> None:
        self.tournament_data = TournamentData()
        self.contact_person_data = ContactPersonData()
        self.team_data = TeamData()
        self.player_data = PlayerData()
        self.game_data = GameData()
        # TODO setja alla data clasana hér

    def get_all_game_data(self) -> list[Game]:
        return self.game_data.get_all_game_data()

    def store_game_data(self, game: Game):
        return self.game_data.store_game_data(game)

    def get_all_contact_person_data(self) -> list[ContactPerson]:
        return self.contact_person_data.get_contact_person_data()

    def get_contact_person_by_id(self, id: int) -> ContactPerson | None:
        return self.contact_person_data.get_contact_person_by_id(id)

    def get_all_tournament_data(self):
        return self.tournament_data.get_tournament_data()

    def store_tournament_data(self, tournament: Tournament):
        return self.tournament_data.store_tournament_data(tournament)

    def get_all_team_data(self):
        return self.team_data.get_all_team_data()

    def store_team_data(self, team: Team):
        return self.team_data.store_team_data(team)

    def get_all_player_data(self):
        return self.player_data.get_all_player_data()
    
    def store_player_data(self, player: Player):
        return self.player_data.store_player_data(player)
    
    def store_contact_person_data(self, contact: ContactPerson):
        return self.contact_person_data.store_contact_person_data(contact)
    
    def get_all_contact_person_data(self):
        return self.contact_person_data.get_all_contact_person_data()
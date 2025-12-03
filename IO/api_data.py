from IO.contact_person_data import ContactPersonData
from IO.player_data import PlayerData
from IO.team_data import TeamData
from IO.tournament_data import TournamentData
from Models.models import ContactPerson
from Models.team import Team
from Models.tournament import Tournament


# Steinar


class APIDATA:
    def __init__(self) -> None:
        self.tournament_data = TournamentData()
        self.contact_person = ContactPersonData()
        self.team_data = TeamData()
        self.player_data = PlayerData()
        # TODO setja alla data clasana hér

    def get_contact_person_data(self) -> list[ContactPerson]:
        return self.contact_person.get_contact_person_data()

    def get_contact_person_by_id(self, id: int) -> ContactPerson | None:
        return self.contact_person.get_contact_person_by_id(id)

    def get_tournament_data(self):
        return self.tournament_data.get_tournament_data()

    def store_tournament_data(self, tournament: Tournament):
        return self.tournament_data.store_tournament_data(tournament)

    def get_team_data(self):
        return self.team_data.get_all_team_data()

    def store_team_data(self, team: Team):
        return self.team_data.store_team_data(team)

    def get_all_player_data(self):
        return self.player_data.get_all_player_data()

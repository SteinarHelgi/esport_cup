from IO.contact_person_data import ContactPersonData
from IO.tournament_data import TournamentData
from Models.models import ContactPerson


# Steinar


class APIDATA:
    def __init__(self) -> None:
        self.tournament_data = TournamentData()
        self.contact_person = ContactPersonData()
        # TODO setja alla data clasana hér

    def get_contact_person_data(self) -> ContactPerson:
        return self.contact_person.get_contact_person_data()

    def get_contact_person_by_id(self, id: int) -> ContactPerson:
        return self.contact_person.get_contact_person_by_id(id)

    def get_tournament_data(self):
        return self.tournament_data.get_tournament_data()

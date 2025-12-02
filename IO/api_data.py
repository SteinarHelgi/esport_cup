from IO import tournament_data
from IO.contact_person import ContactPersonData
from IO.tournament_data import TournamentData
from Models.models import ContactPerson

# Steinar


class APIDATA:
    def __init__(self) -> None:
        self.tournament_data = TournamentData()
        self.contact_person = ContactPersonData()
        # TODO setja alla data clasana hér

    def get_contact_person_by_id(self, name) -> ContactPerson:
        contact = ContactPerson("1", name, "hilmir@rasshaus.is", "855-2449", "1")
        return contact

    def get_all_tournaments(self):
        return self.tournament_data.get_all_tournaments()

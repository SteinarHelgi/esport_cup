from datetime import datetime

from IO.api_data import APIDATA
from IO.contact_person_data import ContactPersonData
from Models.tournament import Tournament
from Models.match import Match
from Models.contact_person import ContactPerson


class OrganiserLL:
    def __init__(self, api_data: APIDATA) -> None:
        self.api_data = api_data
        self._next_contact_id = 1
        self._next_match_id = 1

    def create_tournament(self, tournament: Tournament) -> Tournament | None:
        if tournament.end_date < tournament.start_date:
            raise

        all_tournaments = self.api_data.get_all_tournament_data()

        """ notað til að búa til tournament id """
        if all_tournaments:
            next_id = max(int(tournament.id) for tournament in all_tournaments) + 1

        else:
            next_id = 1

        tournament.set_id(next_id)

        # TODO
        # mögulegar aðrar reglur ( t.d. start date ekki í fortíð)

        stored = self.api_data.store_tournament_data(tournament)

        return stored

    def delete_tournament(self):
        # TODO
        pass

    def create_schedule(self):
        # TODO
        pass

    def create_match(self, match: Match) -> Match:
        if match.team_1_id == match.team_2_id:
            return ValueError

        match.match_id = self._next_match_id
        self._next_match_id += 1

        stored = self.api_data.store_match_data(match)
        return stored

    def register_result(self):
        # TODO
        pass

    def create_contact_person(self, contact: ContactPerson) -> ContactPerson:
        contact.id = self._next_contact_id
        self._next_contact_id += 1

        stored = self.api_data.store_contact_person_data(contact)
        return stored

    def get_contact_person_by_id(self, id: str) -> ContactPerson | None:
        contact_persons = self.api_data.get_all_contact_person_data()
        for contact in contact_persons:
            try:
                if contact.id == id:
                    return contact
            except:
                return None

    def get_contact_person(self, tournament_id: str) -> ContactPerson | None:
        """Skilar tengiliðnum sem tengist þessu tiltekna móti."""
        tournaments = self.api_data.get_all_contact_person_data()

        for t in tournaments:
            if t.id == tournament_id:
                contact_person_id = t.id
                return self.contact_person_data.get_contact_person_by_id(
                    contact_person_id
                )
        return None

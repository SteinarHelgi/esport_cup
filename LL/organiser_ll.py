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

    def create_match(
        self,
        tournament_id: int,
        team_1_id: int,
        team_2_id: int,
        date_time: datetime,
        server_id: int,
        game_id: str,
    ) -> Match:
        if team_1_id == team_2_id:
            return ValueError

        match_id = self._next_match_id
        self._next_match_id += 1

        new_match = Match(
            match_id=match_id,
            tournament_id=tournament_id,
            date_time=date_time,
            team_1_id=team_1_id,
            team_2_id=team_2_id,
            server_id=server_id,
            game_id=game_id,
        )
        # TODO (DATA-LAYER):
        # Þegar TournamentData/APIDATA fá stuðning fyrir leiki
        # má kalla
        #
        #   stored = self.api_data.store_match_data(new_match)
        #   return stored
        return new_match

    def register_result(self):
        # TODO
        pass

    def create_contact_person(
        self,
        name: str,
        email: str,
        phone: str,
        tournament_id: int,
    ) -> ContactPerson:
        contact_id = self._next_contact_id
        self._next_contact_id += 1

        new_contact = ContactPerson(
            id=contact_id,
            name=name,
            email=email,
            phone=phone,
            tournament_id=tournament_id,
        )

        stored = self.api_data.store_contact_person_data(new_contact)
        return stored

    def get_contact_person_by_id(self, id: int) -> ContactPersonData:
        contact_persons = self.get_contact_person_by_id()
        for contact in contact_persons:
            try:
                if contact.id == id:
                    return contact
            except:
                return None


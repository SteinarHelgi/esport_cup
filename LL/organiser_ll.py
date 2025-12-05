from IO.api_data import APIDATA
from Models.tournament import Tournament
from Models.match import Match
from Models.contact_person import ContactPerson
from Models.team_registry import TeamRegistry
from Models.team import Team


class OrganiserLL:
    def __init__(self, api_data: APIDATA) -> None:
        self.api_data = api_data

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

    def get_tournament_by_name(self, tournament_name) -> Tournament | None:
        tournaments = self.api_data.get_all_tournament_data()
        matches = self.api_data.get_all_match_data()
        for tournament in tournaments:
            if tournament.name == tournament_name:
                for match in matches:
                    if match.tournament_id == tournament.id:
                        tournament.add_match(match)

                return tournament

    def delete_tournament(self, tournament_id: str):
        self.api_data.delete_tournament_data(tournament_id)

    def create_schedule(self):
        # TODO
        pass

    def create_match(self, match: Match) -> Match | None:
        if match.team_1_id == match.team_2_id:
            raise ValueError

        matches = self.api_data.get_all_match_data()
        next_id = max(int(match.match_id) for match in matches) + 1
        match.set_id(next_id)

        self._next_match_id += 1

        stored = self.api_data.store_match_data(match)
        return stored

    def register_result(self):
        # TODO
        pass

    def create_contact_person(self, contact: ContactPerson) -> ContactPerson | None:
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
        """Returns contact person that is connected to certain tournament."""
        tournaments = self.api_data.get_all_contact_person_data()
        for t in tournaments:
            if t.id == tournament_id:
                contact_person_id = t.id
                return self.get_contact_person_by_id(contact_person_id)
        return None
    

    def show_all_teams_on_tournament(self, target_tournament_id: str) -> list[Team]:

        #Fetch team registry and search for team_id in a specific tournament id
        team_registry = self.api_data.get_all_team_registry_data()
        all_teams_id_in_tournament: list[str] = []
        for registry in team_registry:
            if registry.tournament_id == target_tournament_id:
                all_teams_id_in_tournament.append(registry.team_id)

        #Fetch a list of teams and their id
        all_teams_in_tournament: list[Team] = []
        teams: Team = self.api_data.get_all_team_data()
        for team in teams:
            if team.id in all_teams_id_in_tournament:
                all_teams_in_tournament.append(team)
        return all_teams_in_tournament
    
    def register_match_result(self, match_id: str, home_score: int, away_score: int, completed: bool):
        self.api_data.register_match_results(match_id, home_score, away_score, completed)
        


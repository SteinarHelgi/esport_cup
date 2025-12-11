from IO.api_data import APIDATA
from datetime import datetime
from Models.models import Tournament, ContactPerson, Team, TeamCaptain, Match

VALID_TEAM_COUNT = 16


class TournamentLL:
    def __init__(self, api_data: APIDATA, main_ll):
        """Initializes the TournamentLL logic layer with access to APIDATA and the main logic layer."""
        self.APIDATA = api_data
        self.MAINLL = main_ll

    def get_all_tournaments(self) -> list[Tournament]:
        """Returns all tournaments with their matches attached."""
        tournaments = self.APIDATA.get_all_tournament_data()
        matches = self.APIDATA.get_all_match_data()

        for tournament in tournaments:
            for match in matches:
                if match.tournament_id == tournament.id:
                    tournament.add_match(match)

        tournaments.sort(key=lambda t: t.start_date)

        return tournaments

    def get_ongoing_tournament(self) -> list[Tournament]:
        """Returns all tournaments that are ongoing."""
        today = datetime.today()
        tournament = self.get_all_tournaments()
        ongoing = []

        for t in tournament:
            if t.start_date <= today <= t.end_date:
                ongoing.append(t)
        return ongoing

    def get_past_tournament(self) -> list[Tournament]:
        """Returns all tournaments that have already finished."""
        tournament = self.get_all_tournaments()
        today = datetime.today()
        past = []

        for t in tournament:
            if t.end_date < today:
                past.append(t)

        return past

    def get_upcoming_tournament(self) -> list[Tournament]:
        """Returns all tournaments that start in the future."""
        tournament = self.get_all_tournaments()
        upcoming = []
        today = datetime.today()

        for t in tournament:
            if t.end_date > today:  # kíkja á
                upcoming.append(t)

        return upcoming

    def get_tournament_by_id(self, tournament_id: str) -> Tournament | None:
        """Returns the tournament with the given ID and attached its matches, or None if not found."""
        tournaments = self.APIDATA.get_all_tournament_data()
        matches = self.APIDATA.get_all_match_data()
        for tournament in tournaments:
            if tournament.id == tournament_id:
                for match in matches:
                    if match.tournament_id == tournament.id:
                        tournament.add_match(match)

                return tournament

    def get_all_matches_by_type(
        self, tournament: Tournament, type_of_round: str
    ) -> list[Match]:
        matches = []
        for match in tournament.matches:
            if str(match.round) == type_of_round:
                matches.append(match)
        return matches

    def get_all_tournaments_for_team(self, team: Team) -> list[Tournament]:
        """Returns all tournaments that the captain's team is registered for."""
        tournaments_for_team = []

        # Find the team captain is registered for

        # Get all team registrations and all tournaments
        team_registry = self.APIDATA.get_all_team_registry_data()
        tournaments = self.APIDATA.get_all_tournament_data()

        # For each registration that matches this team, find the corresponding tournament
        for registry in team_registry:
            if registry.team_id == team.id:
                for tournament in tournaments:
                    if tournament.id == registry.tournament_id:
                        if tournament not in tournaments_for_team:
                            tournaments_for_team.append(tournament)

        return tournaments_for_team

    def get_available_teams_for_next_round(
        self, tournament: Tournament, current_round: str
    ) -> list[Team]:
        """
        Returns teams that:
        - have never lost any completed match in the tournament
        - are not already in a match in the current round
        """

        all_team_names: set[str] = set()
        lost_team_names: set[str] = set()
        teams_in_current_round_names: set[str] = set()

        for match in tournament.matches:
            all_team_names.update([match.team_a_name, match.team_b_name])

            if match.round == current_round:
                teams_in_current_round_names.update(
                    [match.team_a_name, match.team_b_name]
                )

            if match.winner_team_name:
                if match.winner_team_name == match.team_a_name:
                    loser = match.team_b_name
                else:
                    loser = match.team_a_name

                lost_team_names.add(loser)

        undefeated_team_names = all_team_names - lost_team_names

        eligible_team_names = undefeated_team_names - teams_in_current_round_names

        eligible_teams = []
        for name in eligible_team_names:
            team = self.MAINLL.team_ll.get_team_by_name(name)
            eligible_teams.append(team)
        return eligible_teams

    def get_teams_in_tournament(self, tournament: Tournament) -> list[Team]:
        """Returns all teams that are registered to the given tournament."""
        all_teams_in_tournament = self.APIDATA.get_all_team_registry_data()
        teams_in_tournament = []
        for team_tournamnet in all_teams_in_tournament:
            if team_tournamnet.tournament_id == tournament.id:
                team = self.MAINLL.team_ll.get_team_by_id(team_tournamnet.team_id)
                teams_in_tournament.append(team)
        return teams_in_tournament

    def get_all_open_tournaments_for_captain(
        self, captain: TeamCaptain
    ) -> list[Tournament]:
        """Returns all tournaments the captain's team can register for (not started and not already registered.)"""
        open_tournaments = []

        # Find the team captain is registered for
        team = self.MAINLL.team_ll.get_team_by_captain_handle(captain.handle)
        if team is None:
            return open_tournaments

        # Get all team registrations and all tournaments
        team_registry = self.APIDATA.get_all_team_registry_data()
        tournaments = self.APIDATA.get_all_tournament_data()

        now = datetime.now()

        # For each tournament, check if the team can register
        for tournament in tournaments:
            # Only look at tournaments that have not started yet
            if tournament.start_date <= now:
                continue
            # Check if the team is already registered
            is_registered = False
            for registry in team_registry:
                if (
                    registry.team_id == team.id
                    and registry.tournament_id == tournament.id
                ):
                    is_registered = True
                    break

            # If not registered, add to open tournaments list
            if not is_registered:
                open_tournaments.append(tournament)

        return open_tournaments

    def create_tournament(self, tournament: Tournament) -> Tournament | None:
        """Creates a new tournament, validates dates, assigns an ID and saves it."""
        all_tournaments = self.APIDATA.get_all_tournament_data()

        if all_tournaments:
            next_id = max(int(tournament.id) for tournament in all_tournaments) + 1
        else:
            next_id = 1

        tournament.set_id(next_id)
        stored = self.APIDATA.store_tournament_data(tournament)
        return stored

    def get_tournament_by_name(self, tournament_name) -> Tournament | None:
        """Returns the tournament with the given name and attaches its matches, or None if not found."""
        tournaments = self.APIDATA.get_all_tournament_data()
        matches = self.APIDATA.get_all_match_data()
        for tournament in tournaments:
            if tournament.name == tournament_name:
                for match in matches:
                    if match.tournament_id == tournament.id:
                        tournament.add_match(match)

                return tournament

    def delete_tournament(self, tournament_id: str) -> None:
        """Deletes the tournament with the given ID from the data storage."""
        self.APIDATA.delete_tournament_data(tournament_id)

    def cancel_tournament_if_not_enough_teams(self, tournament: Tournament) -> None:
        """Cancels the tournament if the number of registered teams is below VALID_TEAM_COUNT"""
        teams_in_tournament = self.get_all_teams_on_tournament(tournament.id)
        num_teams = len(teams_in_tournament)

        if num_teams < VALID_TEAM_COUNT:
            self.delete_tournament(tournament.id)

    def create_match(self, match: Match) -> Match | None:
        """Creates a new match, assigns ID and match number, and stores it."""
        round = match.round

        matches = self.APIDATA.get_all_match_data()
        next_id = max(int(match.match_id) for match in matches) + 1
        match.set_id(next_id)

        # Finding the max match number for the specific round we are playing
        max_match_number: int = 0
        for matchcsv in matches:
            if round == matchcsv.round:
                if int(matchcsv.match_number) > max_match_number:
                    max_match_number = int(matchcsv.match_number)

        next_match_number = max_match_number + 1
        match.set_match_number(next_match_number)

        return self.APIDATA.store_match_data(match)

    def delete_match(self, match_id: str) -> None:
        self.APIDATA.delete_match_data(match_id)

    def get_all_teams_on_tournament(self, target_tournament_id: str) -> list[Team]:
        """Returns all teams that are registered to the given tournament ID."""
        team_registry = self.APIDATA.get_all_team_registry_data()
        all_teams_id_in_tournament: list[str] = []
        for registry in team_registry:
            if registry.tournament_id == target_tournament_id:
                all_teams_id_in_tournament.append(registry.team_id)

        # Fetch a list of teams and their id
        all_teams_in_tournament: list[Team] = []
        teams = self.APIDATA.get_all_team_data()
        for team in teams:
            if team.id in all_teams_id_in_tournament:
                all_teams_in_tournament.append(team)
        return all_teams_in_tournament

    def create_contact_person(
        self, contact_person: ContactPerson
    ) -> ContactPerson | None:
        """Creates a new contact person, assigns and ID and stores it."""
        all_contact_person = self.APIDATA.get_all_contact_person_data()

        if all_contact_person:
            next_id = (
                max(int(contact_person.id) for contact_person in all_contact_person) + 1
            )
            contact_person.set_id(next_id)

        stored = self.APIDATA.store_contact_person_data(contact_person)
        return stored

    def get_contact_person_by_id(self, id: str) -> ContactPerson | None:
        """Returns the contact person with the given ID, or None if not found."""
        contact_persons = self.APIDATA.get_all_contact_person_data()
        for contact in contact_persons:
            if contact.id == id:
                return contact

    def get_contact_person(self, tournament_id: str) -> ContactPerson | None:
        """Returns contact person that is connected to the given tournament ID."""
        tournaments = self.APIDATA.get_all_contact_person_data()
        for t in tournaments:
            if t.id == tournament_id:
                contact_person_id = t.id
                return self.get_contact_person_by_id(contact_person_id)
        return None

    def register_match_result(self, match_id: str, winner_name: str, completed: str):
        self.APIDATA.register_match_results(match_id, winner_name, completed)

    def give_team_points(self, team_name: str, points: int) -> None:
        """Adds points to the team with the given name."""
        self.APIDATA.give_team_points(team_name, points)

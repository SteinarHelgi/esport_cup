from IO.api_data import APIDATA
from datetime import datetime
from Models.models import (
    Tournament,
    TeamRegistry,
    ContactPerson,
    Player,
    Club,
    Team,
    TeamCaptain,
    Match,
)


class TouranamentLL:
    def __init__(self, api_data: APIDATA, main_ll):
        self.APIDATA = api_data
        self.MAINLL = main_ll

    def get_all_tournaments(self) -> list:
        tournaments = self.APIDATA.get_all_tournament_data()
        matches = self.APIDATA.get_all_match_data()

        for tournament in tournaments:
            for match in matches:
                if match.tournament_id == tournament.id:
                    print(match)
                    tournament.add_match(match)
        return tournaments

    def get_ongoing_tournament(self):
        today = datetime.today()
        tournament = self.get_all_tournaments()
        ongoing = []

        for t in tournament:
            if t.start_date <= today <= t.end_date:
                ongoing.append(t)
        return ongoing

    def get_past_tournament(self):
        tournament = self.get_all_tournaments()
        today = datetime.today()
        past = []

        for t in tournament:
            if t.end_date < today:
                past.append(t)

        return past

    def get_upcoming_tournament(self):
        tournament = self.get_all_tournaments()
        upcoming = []
        today = datetime.today()

        for t in tournament:
            if t.end_date > today:  # kíkja á
                upcoming.append(t)

        return upcoming

    def get_tournament_by_id(self, tournament_id: str) -> Tournament | None:
        tournaments = self.APIDATA.get_all_tournament_data()
        matches = self.APIDATA.get_all_match_data()
        for tournament in tournaments:
            if tournament.id == tournament_id:
                for match in matches:
                    if match.tournament_id == tournament.id:
                        tournament.add_match(match)

                return tournament

    def get_all_tournaments_for_captain(self, captain: TeamCaptain) -> list[Tournament]:
        """Returns a list of tournaments that the captain's team is registered for."""
        tournaments_for_captain = []

        # Find the team captain is registered for
        team = self.MAINLL.team_ll.get_team_by_captain_handle(captain.handle)
        if team is None:
            return tournaments_for_captain

        # Get all team registrations and all tournaments
        team_registry = self.APIDATA.get_all_team_registry_data()
        tournaments = self.APIDATA.get_all_tournament_data()

        # For each registration that matches this team, find the corresponding tournament
        for registry in team_registry:
            if registry.team_id == team.id:
                for tournament in tournaments:
                    if tournament.id == registry.tournament_id:
                        if tournament not in tournaments_for_captain:
                            tournaments_for_captain.append(tournament)

        return tournaments_for_captain

    def get_all_open_tournaments_for_captain(
        self, captain: TeamCaptain
    ) -> list[Tournament]:
        """
        Returns a list of tournaments that the captain's team can register for.
        A tournament is considered open if it has not started yet and the team
        is not already registered for it.
        """

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
        if tournament.end_date < tournament.start_date:
            raise

        all_tournaments = self.APIDATA.get_all_tournament_data()

        """ notað til að búa til tournament id """
        if all_tournaments:
            next_id = max(int(tournament.id) for tournament in all_tournaments) + 1

        else:
            next_id = 1

        tournament.set_id(next_id)

        # TODO
        # mögulegar aðrar reglur ( t.d. start date ekki í fortíð)

        stored = self.APIDATA.store_tournament_data(tournament)

        return stored

    def get_tournament_by_name(self, tournament_name) -> Tournament | None:
        tournaments = self.APIDATA.get_all_tournament_data()
        matches = self.APIDATA.get_all_match_data()
        for tournament in tournaments:
            if tournament.name == tournament_name:
                for match in matches:
                    if match.tournament_id == tournament.id:
                        tournament.add_match(match)

                return tournament

    def delete_tournament(self, tournament_id: str):
        self.APIDATA.delete_tournament_data(tournament_id)

    def create_match(self, match: Match) -> Match | None:
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

        # This tracks the 4 criteria needed to validate a match
        teams_valid: list[str] = []

        # Critera #1
        if match.team_a_name != match.team_b_name:
            teams_valid.append("criteria #1")

        # Criteria #2 and 3. Check to see if the teams won in the previous round
        round = match.round
        if round != "R16":
            index = match.rounds.index(round)
            prev_round = match.rounds[index - 1]

            for matchcsv in matches:
                if matchcsv.round == prev_round:
                    if match.team_a_name == matchcsv.winner_team_name:
                        teams_valid.append("Criteria #2")
                    if match.team_b_name == matchcsv.winner_team_name:
                        teams_valid.append("Criteria #3")
        else:
            # If this is the first round, we don't need to check anything
            teams_valid.append("Criteria #2")
            teams_valid.append("Criteria #3")

        # Criteria #4. Check to see if the teams have already been registered to this round
        criteria = True
        for matchcsv in matches:
            if round == matchcsv.round:
                if (
                    match.team_a_name == matchcsv.team_a_name
                    or match.team_a_name == matchcsv.team_b_name
                ):
                    criteria = False
                if (
                    match.team_b_name == matchcsv.team_b_name
                    or match.team_b_name == matchcsv.team_b_name
                ):
                    criteria = False
        if criteria:
            teams_valid.append("Criteria #4")

        # Critera #5 - Checking to see if a server is free
        server_names = [
            "SRV-PEPSI",
            "SRV-CHUCK",
            "SRV-DATALAB",
            "SRV-BOMBLAB",
            "SRV-DUSTY",
        ]

        # 4 values means all criteria was met and we can add the match to matches.csv
        if len(teams_valid) == 4:
            stored = self.APIDATA.store_match_data(match)
            print("Len == 4")
        else:
            stored = None
            print("Len != 4")
            raise ValueError
        return stored

    def get_all_teams_on_tournament(self, target_tournament_id: str) -> list[Team]:
        # Fetch team registry and search for team_id in a specific tournament id
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

    def create_contact_person(self, contact: ContactPerson) -> ContactPerson | None:
        contact.id = self._next_contact_id
        self._next_contact_id += 1

        stored = self.APIDATA.store_contact_person_data(contact)
        return stored

    def get_contact_person_by_id(self, id: str) -> ContactPerson | None:
        contact_persons = self.APIDATA.get_all_contact_person_data()
        for contact in contact_persons:
            try:
                if contact.id == id:
                    return contact
            except:
                return None

    def get_contact_person(self, tournament_id: str) -> ContactPerson | None:
        """Returns contact person that is connected to certain tournament."""
        tournaments = self.APIDATA.get_all_contact_person_data()
        for t in tournaments:
            if t.id == tournament_id:
                contact_person_id = t.id
                return self.get_contact_person_by_id(contact_person_id)
        return None

    def register_match_result(
        self, match_id: str, home_score: int, away_score: int, completed: str
    ):
        self.APIDATA.register_match_results(match_id, home_score, away_score, completed)

    def give_player_points(self, handle: str, points: int):
        self.APIDATA.give_player_points(handle, points)

    def give_team_points(self, team_name: str, points: int):
        self.APIDATA.give_team_points(team_name, points)

    def give_club_points(self, club_name: str, points: int):
        self.APIDATA.give_club_points(club_name, points)

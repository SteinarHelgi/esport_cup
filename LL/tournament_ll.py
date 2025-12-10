import random
from IO.api_data import APIDATA
from datetime import datetime
from Models.models import (
    Tournament,
    ContactPerson,
    Team,
    TeamCaptain,
    Match,
)


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

    def get_all_tournaments_for_captain(self, captain: TeamCaptain) -> list[Tournament]:
        """Returns all tournaments that the captain's team is registered for."""
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

    def get_teams_not_in_round(self, tournament):
        teams_in_tournament = self.get_teams_in_tournament(tournament)
        if len(tournament.matches) < 8:
            round = "R16"
        elif len(tournament.matches) < 12:
            round = "QF"
        elif len(tournament.matches) < 14:
            round = "SF"
        else:
            round = "Final"
        matches = self.get_all_matches_by_type(tournament, round)
        teams_not_in_round = []

        for team in teams_in_tournament:
            in_match = False  # assume not in a match
            for match in matches:
                if match.team_a_name == team.name or match.team_b_name == team.name:
                    in_match = True
                    break  # no need to check more matches

            if not in_match:
                teams_not_in_round.append(team)
        return teams_not_in_round

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
        if tournament.end_date < tournament.start_date:
            raise

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

        # # This tracks the 4 criteria needed to validate a match
        # teams_valid: list[str] = []
        #
        # # Critera #1
        # if match.team_a_name != match.team_b_name:
        #     teams_valid.append("criteria #1")
        #
        # # Criteria #2 and 3. Check to see if the teams won in the previous round
        # round = match.round
        # if round != "R16":
        #     index = match.rounds.index(round)
        #     prev_round = match.rounds[index - 1]
        #
        #     for matchcsv in matches:
        #         if matchcsv.round == prev_round:
        #             if match.team_a_name == matchcsv.winner_team_name:
        #                 teams_valid.append("Criteria #2")
        #             if match.team_b_name == matchcsv.winner_team_name:
        #                 teams_valid.append("Criteria #3")
        # else:
        #     # If this is the first round, we don't need to check anything
        #     teams_valid.append("Criteria #2")
        #     teams_valid.append("Criteria #3")
        #
        # # Criteria #4. Check to see if the teams have already been registered to this round
        # criteria = True
        # for matchcsv in matches:
        #     if round == matchcsv.round:
        #         if (
        #             match.team_a_name == matchcsv.team_a_name
        #             or match.team_a_name == matchcsv.team_b_name
        #         ):
        #             criteria = False
        #         if (
        #             match.team_b_name == matchcsv.team_b_name
        #             or match.team_b_name == matchcsv.team_b_name
        #         ):
        #             criteria = False
        # if criteria:
        #     teams_valid.append("Criteria #4")
        #
        # # Critera #5 - Checking to see if a server is free
        # server_names = [
        #     "SRV-PEPSI",
        #     "SRV-CHUCK",
        #     "SRV-DATALAB",
        #     "SRV-BOMBLAB",
        #     "SRV-DUSTY",
        # ]
        #
        # # Check to see if a valid server has been selected
        # # COMMENTA AF ÞVI VEIT EKKI HVORT ÞETTA MEIKI SENSE
        # # if match.server_id not in server_names:
        # #     raise ValueError
        #
        # # Check to see if the selected server is busy
        # for matchcsv in matches:
        #     if (
        #         matchcsv.match_date == match.match_date
        #         and matchcsv.match_time == match.match_time
        #         and matchcsv.server_id == match.server_id
        #     ):
        #         raise ValueError
        #
        # # 4 values means all criteria was met and we can add the match to matches.csv
        # if len(teams_valid) == 4:
        #     stored = self.APIDATA.store_match_data(match)
        #     print("Len == 4")
        # else:
        #     stored = None
        #     print("Len != 4")
        #     raise ValueError

        return self.APIDATA.store_match_data(match)

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

    def create_contact_person(self, contact_person: ContactPerson) -> ContactPerson | None:
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

    def register_match_result(self, match_id: str, home_score: int, away_score: int, completed: str) -> None:
        """Registers the result of a match in the data storage."""
        self.APIDATA.register_match_results(match_id, home_score, away_score, completed)

    def give_player_points(self, handle: str, points: int) -> None:
        """Adds points to the player with the given handle."""
        self.APIDATA.give_player_points(handle, points)

    def give_team_points(self, team_name: str, points: int) -> None:
        """Adds points to the team with the given name."""
        self.APIDATA.give_team_points(team_name, points)

    def give_club_points(self, club_name: str, points: int) -> None:
        """Adds points to the club with the given name."""
        self.APIDATA.give_club_points(club_name, points)

    def setup_R16_qualifying_matches(self, tournament_id: str) -> None:
        """Creates R16 qualifying matches for the given tournament."""
        team_registry = self.APIDATA.get_all_team_registry_data()
        all_tournaments = self.APIDATA.get_all_tournament_data()
        playing_times: list[str] = ["10:00", "12:00", "14:00", "16:00"]

        start_date: datetime = datetime(year=2000, month=1, day=1)
        for t in all_tournaments:
            if t.id == tournament_id:
                start_date = t.start_date
                break
        # If tournament id was not found - raise valueerror
        if start_date.year == 2000:
            raise ValueError
        next_day = start_date.day + 1
        next_date: datetime = datetime(
            year=start_date.year, month=start_date.month, day=next_day
        )

        dates: list[datetime] = [start_date, next_date]

        teams_playing: list[str] = []
        for registry in team_registry:
            if registry.tournament_id == tournament_id:
                teams_playing.append(registry.team_name)

        # R16 is 8 matches Four matches per day for 2 days
        match_id = 1
        for j in range(2):
            date_of_game = dates[j]
            for i in range(4):
                new_tournament_id: str = tournament_id
                round: str = "R16"
                team_a_name: str = random.choice(teams_playing)
                teams_playing.remove(team_a_name)
                team_b_name: str = random.choice(teams_playing)
                teams_playing.remove(team_b_name)
                time_of_match = playing_times[i]
                new_match = Match(
                    new_tournament_id,
                    round,
                    team_a_name,
                    team_b_name,
                    str(date_of_game),
                    time_of_match,
                )
                new_match.match_id = str(match_id)
                new_match.match_number = str(match_id)
                server_id = "SRV-PEPSI"
                new_match.server_id = server_id
                self.APIDATA.store_match_data(new_match)
                match_id += 1

from IO.api_data import APIDATA
from Models.tournament import Tournament
from Models.match import Match
from Models.contact_person import ContactPerson
from Models.team_registry import TeamRegistry
from Models.team import Team
from Models.stat import Stat
import matplotlib.pyplot as plt

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

    def create_match(self, match: Match) -> Match | None:
        round = match.round
        
        matches = self.api_data.get_all_match_data()
        next_id = max(int(match.match_id) for match in matches) + 1
        match.set_id(next_id)

        #Finding the max match number for the specific round we are playing
        max_match_number = 0
        for matchcsv in matches:
            if round == matchcsv.round:
                if matchcsv.match_number > max_match_number:
                    max_match_number = matchcsv.match_number
                
        next_match_number = max_match_number + 1
        match.set_match_number(next_match_number)

        #This tracks the 4 criteria needed to validate a match
        teams_valid: list[str] = []

        #Critera #1
        if match.team_a_name != match.team_b_name:
            teams_valid.append("criteria #1")

        #Criteria #2 and 3. Check to see if the teams won in the previous round
        round = match.round
        #If this is the first round, we don't need to check anything
        if round != "R16":
            index = match.rounds.index(round)
            prev_round = match.rounds[index - 1]

            for matchcsv in matches:
                if matchcsv.round == prev_round:
                    if match.team_a_name == matchcsv.winner_team_name:
                        teams_valid.append("Criteria #2")
                    if match.team_b_name == matchcsv.winner_team_name:
                        teams_valid.append("Criteria #3")
        
        #Criteria #4. Check to see if the teams have already been registered to this round
        criteria = True
        for matchcsv in matches:
            if round == matchcsv.round:
                if match.team_a_name == matchcsv.team_a_name or match.team_a_name == matchcsv.team_b_name:
                    criteria = False
                if match.team_b_name == matchcsv.team_b_name or match.team_b_name == matchcsv.team_b_name:
                    criteria = False
        if criteria:
            teams_valid.append("Criteria #4")

        # 4 values means all criteria was met and we can add the match to matches.csv
        if len(teams_valid) == 4:
            stored = self.api_data.store_match_data(match)
        else:
            stored = None
            raise ValueError
        return stored

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
        # Fetch team registry and search for team_id in a specific tournament id
        team_registry = self.api_data.get_all_team_registry_data()
        all_teams_id_in_tournament: list[str] = []
        for registry in team_registry:
            if registry.tournament_id == target_tournament_id:
                all_teams_id_in_tournament.append(registry.team_id)

        # Fetch a list of teams and their id
        all_teams_in_tournament: list[Team] = []
        teams = self.api_data.get_all_team_data()
        for team in teams:
            if team.id in all_teams_id_in_tournament:
                all_teams_in_tournament.append(team)
        return all_teams_in_tournament

    def register_match_result(
        self, match_id: str, home_score: int, away_score: int, completed: bool
    ):
        self.api_data.register_match_results(
            int(match_id), home_score, away_score, completed
        )

    def give_player_points(self, handle: str, points: int):
        self.api_data.give_player_points(handle, points)
    
    def give_team_points(self, team_name: str, points: int):
        self.api_data.give_team_points(team_name, points)
    
    def give_club_points(self, club_name: str, points: int):
        self.api_data.give_club_points(club_name, points)
    
    def get_player_stats(self):
        players = self.api_data.get_all_player_data()
        stats: list[list[int, str]] = []
        for player in players:
            results: list[int, str] = []
            results = [player.points, player.handle]
            stats.append(results)
        sorted_results = sorted(stats, key=lambda item: item[0], reverse = True)
        
        #Going to show this many players in our stats
        number_of_players_to_display = 5
        #creating the value and keys for the bar chart 
        handle: list[str] = []
        points: list[int] = []
        for i in range(number_of_players_to_display):
            handle.append(sorted_results[i][1])
            points.append(sorted_results[i][0])
        plt.bar(handle, points)
        plt.show()

    def show_elimination_stats(self, tournament_id):
        matches = self.api_data.get_all_match_data()
        team_registry = self.api_data.get_all_team_registry_data()
        stats: list[Stat] = []
        for registry in team_registry:
            stat = Stat(registry.team_name)
            for match in matches:
                if match.completed == "TRUE":
                    if match.team_a_name == stat.team_name:
                        stat.games_played += 1
                        stat.score_for += int(match.score_a)
                        stat.score_against += int(match.score_b)
                    if match.team_b_name == stat.team_name:
                        stat.games_played += 1
                        stat.score_for += int(match.score_b)
                        stat.score_against += int(match.score_a)
                    if match.winner_team_name == stat.team_name:
                        stat.won += 1
            stat.lost = stat.games_played - stat.won
            if stat.games_played == 0:
                stat.winning_ratio = 0
            else:
                stat.winning_ratio = stat.won/stat.games_played * 100
            stats.append(stat)
        
        sorted_by_winning_ratio = sorted(stats, key=lambda s: s.winning_ratio, reverse = True)
        
        return sorted_by_winning_ratio
                    
                


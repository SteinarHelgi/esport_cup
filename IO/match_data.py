# Sigrún
import csv
from Models.models import Match
import datetime


class MatchData:
    def __init__(self) -> None:
        self.match_file_path = "Data/matches.csv"

    def get_all_match_data(self) -> list[Match]:
        matches: list[Match] = []

        with open(self.match_file_path, "r", encoding="utf-8") as file:
            csv_reader = csv.reader(file)
            next(csv_reader, None)  # Skip header line

            # match_id,tournament_id,round,match_number,team_a_name,team_b_name,match_date,match_time,server_id,score_a,score_b,winner_team_name,completed
            for line in csv_reader:
                match_id: str = line[0]
                tournament_id: str = line[1]
                round: str = line[2]
                team_1_id: str = line[4]
                team_2_id: str = line[5]
                match_date: str = line[6]
                match_time: str = line[7]
                server_id: str = line[8]
                winner_team: str = line[11]
                game_name: str = line[
                    9
                ]  # Game name is not in the csv file, need to fix
                completed: str = line[10]

                match = Match(
                    tournament_id,
                    round,
                    team_1_id,
                    team_2_id,
                    match_date,
                    match_time,
                    server_id,
                    game_name,
                )

                match.set_id(match_id)
                match.set_winner(winner_team)
                matches.append(match)

        return matches

    def store_match_data(self, match: Match) -> Match | None:
        with open(self.match_file_path, "a", encoding="utf-8") as file:
            csv_writer = csv.writer(file)
            try:
                csv_writer.writerow(match.toCSVList())
            except:
                return None
        return match

    def register_match_results(self, match_id: str, home_score: int, away_score: int, completed_match: bool) -> Match | None:
        temp_data = []
        target_id: str = match_id
        
        #Creates a temporary data file
        try:
            with open(self.match_file_path, 'r', newline='') as file:
                reader = csv.reader(file)
        
        # Read the header row first
                header = next(reader) 
                temp_data.append(header) # Add header to the data we are keeping

        # Read the rest of the rows
                for line in reader:
                    # Check the value in the first column (index 0)
                    if line[0] != target_id:
                        temp_data.append(line)
                    else:
                        new_match_id: str = line[0]
                        tournament_id: str = line[1]
                        round: str = line[2]
                        match_number: str = line[3]
                        team_a_name: str = line[4]
                        team_b_name: str = line[5]
                        match_date: datetime = line[6]
                        match_time: datetime = line[7]
                        server_id: str = line[8]
                        score_a: int = home_score
                        score_b: int = away_score
                        if home_score > away_score:
                            winner_team_name: str = team_a_name
                        else:
                            winner_team_name: str = team_b_name
                        completed: bool = completed_match
                        new_line = [
                            match_id,
                            tournament_id,
                            round,
                            match_number,
                            team_a_name,
                            team_b_name,
                            match_date,
                            match_time,
                            server_id,
                            score_a,
                            score_b,
                            winner_team_name,
                            completed]
                        temp_data.append(new_line)
                        
                        
        except FileNotFoundError:
            exit()
        
        #Overwrites temporary datafile to csv file
        try:
            with open(self.match_file_path, 'w', newline='', encoding='utf-8') as csvfile:
                # Create a writer object
                writer = csv.writer(csvfile)
            
                # Iterate through the list of strings
                for line in temp_data:
                    writer.writerow(line)
        except:
            return None
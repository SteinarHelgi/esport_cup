import csv
from Models.models import Match


class MatchData:

    def __init__(self) -> None:
        self.match_file_path = "Data/matches.csv"

    def get_all_match_data(self) -> list[Match]:
        """Reads all matches from the CSV file and returns them as a list of Match objects."""

        matches: list[Match] = []

        # Open the CSV file in read mode
        with open(self.match_file_path, "r", encoding="utf-8") as file:
            csv_reader = csv.reader(file)

            # Skip header line
            next(csv_reader, None) 

            # Read each remaining line in the CSV file
            for line in csv_reader:
                # Skip empty lines if any
                if line != []:
                    match_id: str = line[0]
                    tournament_id: str = line[1]
                    round: str = line[2]
                    match_number: int = int(line[3])
                    team_a_name: str = line[4]
                    team_b_name: str = line[5]
                    match_date: str = line[6]
                    match_time: str = line[7]
                    server_id: str = line[8]
                    score_a: str = line[9]
                    score_b: str = line[10]
                    winner_team_name: str = line[11]
                    completed: str = line[12]
                    
                    # Create Match object from the CSV line
                    match = Match(
                        tournament_id,
                        round,
                        team_a_name,
                        team_b_name,
                        match_date,
                        match_time,
                    )
                    # Set additional attributes that are not in the constructor
                    match.set_id(match_id)
                    match.set_match_number(match_number)
                    match.set_score(score_a, score_b)
                    match.set_winner(winner_team_name)
                    match.set_server_id()

                    matches.append(match)

        return matches

    def store_match_data(self, match: Match) -> Match | None:
        """Appends a single match to the CSV file. Returns the match if successful, otherwise None."""
        with open(self.match_file_path, "a", newline="", encoding="utf-8") as file:
            csv_writer = csv.writer(file)
            try:
                csv_writer.writerow(match.toCSVList())
            except:
                return None
        return match

    def register_match_results(self, match_id: str, home_score: int, away_score: int, completed_match: str) -> Match | None:
        """Updates the results of a given match in the CSV file."""
        temp_data: list[list[str]] = []
        target_id: str = match_id

        # Creates a temporary data list
        try:
            with open(self.match_file_path, "r", newline="") as file:
                reader = csv.reader(file)

                header = next(reader)
                if header:
                    temp_data.append(header)  

                # Read the rest of the rows
                for line in reader:
                    if line[0] != target_id:
                        temp_data.append(line)
                    else:
                        new_match_id: str = line[0]
                        tournament_id: str = line[1]
                        round: str = line[2]
                        match_number: str = line[3]
                        team_a_name: str = line[4]
                        team_b_name: str = line[5]
                        match_date: str = line[6]
                        match_time: str = line[7]
                        server_id: str = line[8]
                        score_a: int = home_score
                        score_b: int = away_score
                        if home_score > away_score:
                            winner_team_name: str = team_a_name
                        else:
                            winner_team_name: str = team_b_name
                        completed: str = completed_match
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
                            completed,
                        ]
                        temp_data.append(new_line)

        except FileNotFoundError:
            exit()

        # Overwrites temporary datafile to csv file
        try:
            with open(
                self.match_file_path, "w", newline="", encoding="utf-8"
            ) as csvfile:
                # Create a writer object
                writer = csv.writer(csvfile)

                # Iterate through the list of strings
                for line in temp_data:
                    writer.writerow(line)
        except:
            return None

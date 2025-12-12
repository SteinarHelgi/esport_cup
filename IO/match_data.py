import csv
from Models.models import Match


class MatchData:
    def __init__(self) -> None:
        self.match_file_path = "Data/matches.csv"

    def get_all_match_data(self, filepath: str = "Data/matches.csv") -> list[Match]:
        """Reads all matches from the CSV file and returns them as a list of Match objects."""

        matches: list[Match] = []

        # Open the CSV file in read mode
        with open(filepath, "r", encoding="utf-8") as file:
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
                    match.set_winner(winner_team_name, completed)
                    match.set_server_id(server_id)

                    matches.append(match)

        return matches

    def store_match_data(
        self, match: Match, filepath: str = "Data/matches.csv"
    ) -> Match | None:
        """Appends a single match to the CSV file. Returns the match if successful, otherwise None."""
        with open(filepath, "a", newline="", encoding="utf-8") as file:
            csv_writer = csv.writer(file)
            try:
                csv_writer.writerow(match.toCSVList())
            except (OSError, csv.Error):
                return None
        return match

    def register_match_results(
        self,
        match_id: str,
        winner_name: str,
        completed_match: str,
        filepath: str = "Data/matches.csv",
    ) -> Match | None:
        """Updates the winner and completion status in the CSV, ignoring scores."""
        temp_data: list[list[str]] = []
        found = False

        try:
            with open(filepath, "r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)

                header = next(reader, None)
                if header:
                    temp_data.append(header)

                for line in reader:
                    if not line:
                        continue

                    # Check if this is the target match
                    if line[0] == match_id:
                        # update winner
                        line[11] = winner_name
                        line[12] = completed_match
                        found = True

                    temp_data.append(line)

        except FileNotFoundError:
            return None

        if not found:
            return None

        # Write updated data back to CSV
        try:
            with open(filepath, "w", newline="", encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(temp_data)
        except (OSError, csv.Error):
            return None

    def delete_match_data(self, match: Match) -> None:
        target_id = match.match_id

        # Creates a temporary data file
        temp_data = []

        try:
            with open(self.match_file_path, "r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)

                # Read the header row first
                header = next(reader)
                temp_data.append(header)  # Add header to the data we are keeping

                # Read the rest of the rows
                for line in reader:
                    # Check the value in the first column (index 0)
                    if line[0] != target_id:
                        temp_data.append(line)

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
        except (OSError, csv.Error):
            return None

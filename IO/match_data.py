# Sigrún
import csv
from Models.models import Match


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

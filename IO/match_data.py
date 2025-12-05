# Sigrún
import csv
import datetime as dt
from Models.models import Match


class MatchData:
    def __init__(self) -> None:
        self.match_file_path = "Data/Matches.csv"

    def get_all_match_data(self) -> list[Match]:
        matches: list[Match] = []

        with open(self.match_file_path, "r", encoding="utf-8") as file:
            csv_reader = csv.reader(file)
            next(csv_reader, None)  # Skip header line

            for line in csv_reader:
                match_id: str = line[0]
                date_time: dt.datetime = dt.datetime.fromisoformat(line[1])
                team_1_id: str = line[2]
                team_2_id: str = line[3]
                server_id: str = line[4]
                game: str = line[5]

                match = Match(
                    match_id,
                    date_time,
                    team_1_id,
                    team_2_id,
                    server_id,
                    game,
                )
                matches.append(match)

        return matches

    # TODO færa í Logic layer
    # def get_match_data(self, match_id: str) -> Match | None:
    #     matches = self.get_all_match_data()
    #
    #     for match in matches:
    #         if match.match_id == match_id:
    #             return match
    #     return None

    def store_match_data(self, match: Match) -> Match | None:
        with open(self.match_file_path, "a", encoding="utf-8") as file:
            csv_writer = csv.writer(file)
            try:
                csv_writer.writerow(match.toCSVList())
            except:
                return None
        return match


# Sigrún
import csv
import datetime as dt
from Models.models import Match


class MatchData:
    def __init__(self) -> None:
        self.match_file_path = "Data/Matches.csv"

    def get_match_data(self) -> list[Match]:
        """Les alla leiki úr CSV skránni og skilar lista af Match hlutum."""
        matches = []

        with open(self.match_file_path, "r", encoding="utf-8") as file:
            csv_reader = csv.reader(file)

            # sleppum header-línu ef hún er til staðar
            next(csv_reader, None)

            for line in csv_reader:
                match_id = int(line[0])
                date_time = dt.datetime.fromisoformat(line[1])
                team_1_id = int(line[2])
                team_2_id = int(line[3])
                server_id = int(line[4])
                game = line[5]

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

    def get_match_info(self, match_id: int) -> str:
        """Skilar upplýsingum um tiltekinn leik sem streng."""
        matches = self.get_match_data()

        for m in matches:
            if m.match_id == match_id:
                return f"Match {m.match_id} : team {m.team_1_id} vs team {m.team_2_id} on server {m.server_id} (game {m.game_id})"
        return ""

    def store_match_info(self, match: Match) -> Match | None:
        """Bætir nýjum leik aftast í Matches.csv skrána."""
        with open(self.match_file_path, "a", encoding="utf-8") as file:
            csv_writer = csv.writer(file)
            try:
                csv_writer.writerow(match.toCSVList())
            except:
                return None

        return match
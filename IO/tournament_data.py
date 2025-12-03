# Höfundur: Þröstur
import csv
from Models.models import Tournament
from datetime import datetime

# Steinar


class TournamentData:
    def __init__(self):
        self.tournament_file_path = "Data/Tournaments.csv"

    def get_tournament_data(self) -> list[Tournament]:
        tournaments = []
        with open(self.tournament_file_path, "r+", encoding = "utf-8") as file:
            csvReader = csv.reader(file)
            next(csvReader)  # skip header
            for line in csvReader:
                if line != []:
                    id = int(line[0])
                    name = line[1]
                    start_date = datetime.fromisoformat(line[2])
                    end_date = datetime.fromisoformat(line[3])
                    venue = line[4]
                    game_id = line[5]
                    number_of_servers = int(line[6])
                    contact_person_name = line[7]

                    tournament = Tournament(
                        id,
                        name,
                        start_date,
                        end_date,
                        venue,
                        game_id,
                        number_of_servers,
                        contact_person_name,
                    )
                tournaments.append(tournament)
        return tournaments

    def store_tournament_data(self, tournament: Tournament)->Tournament:
        with open(self.tournament_file_path, "a") as file:
            csvWriter = csv.writer(file)
            try:
                csvWriter.writerow(tournament.toCSVList())
            except:
                return None
        return tournament

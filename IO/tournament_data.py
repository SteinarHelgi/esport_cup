# Höfundur: Þröstur
# Tilbúið til rýni: Já
# Rýnir:
import csv
from Models.models import Tournament
from datetime import datetime


class TournamentData:
    def __init__(self):
        self.tournamentFilepath = "Data/Tournaments.csv"

    def get_all_tournaments(self) -> list[Tournament]:
        tournaments = []
        with open(self.tournamentFilepath, "r+") as file:
            csvReader = csv.reader(file)
            next(csvReader)  # skip header
            for line in csvReader:
                id = int(line[0])
                name = line[1]
                start_date = datetime.fromisoformat(line[2])
                end_date = datetime.fromisoformat(line[3])
                venue = line[4]
                game_id = line[5]
                number_of_servers = int(line[6])
                # contact_person_id = ContactPerson(line[7],"Hilmir","hilmir@rasshaus.is","8410536",)
                contact_person_id = line[7]

                tournament = Tournament(
                    id,
                    name,
                    start_date,
                    end_date,
                    venue,
                    game_id,
                    number_of_servers,
                    contact_person_id,
                )
                tournaments.append(tournament)
        return tournaments

    def storeNewTournament(self, tournament: Tournament):
        with open(self.tournamentFilepath, "a") as file:
            csvWriter = csv.writer(file)
            try:
                csvWriter.writerow(tournament.toCSVList())
            except:
                return None
        return tournament

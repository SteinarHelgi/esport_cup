#Höfundur: Þröstur
import csv
from Models.models import Tournament
from datetime import datetime
from IO.contact_person_data import ContactPersonData
from Models.models import ContactPerson
from IO.match_data import MatchData


# Steinar

class TournamentData:
    def __init__(self):
        self.tournament_file_path = "Data/Tournaments.csv"
        self.contact_person_data = ContactPersonData()
        self.match_data = MatchData()

    def get_tournament_data(self) -> list[Tournament]:
        tournaments = []
        with open(self.tournament_file_path, "r") as file:
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

    def store_tournament_data(self, tournament: Tournament)->Tournament:
        with open(self.tournament_file_path, "a") as file:
            csvWriter = csv.writer(file)
            try:
                csvWriter.writerow(tournament.toCSVList())
            except:
                return None
        return tournament

# Sigrún

    def get_contact_person_info(self, tournament_id: int) -> ContactPerson | None:
        """Skilar tengiliðnum sem tengist þessu tiltekna móti."""
        tournaments = self.get_tournament_data()

        for t in tournaments:
            if t.id == tournament_id:
                contact_person_id = int(t.contact_person)
                return self.contact_person_data.get_contact_person_by_id(contact_person_id)
        return None

    def store_contact_person_info(self, contact_person: ContactPerson):
        """Vistar tengilið. Notar ContactPersonData. Skilar ContactPerson ef þetta tókst, annars None."""
        return self.contact_person_data.store_contact_person_data(contact_person)

    def get_tournament_info(self) -> str:
        """Skilar upplýsingum um mót sem streng."""
        tournaments = self.get_tournament_data()
        lines = []
        for t in tournaments:
            lines.append(f"{t.id}: {t.name} ({t.start_date} - {t.end_date}) @ {t.venue}")
        return "\n".join(lines)
    
    def get_schedule_info(self) -> str: 
        """Skilar leikjadagskránni sem streng"""
        matches = self.match_data.get_match_data()

        # Röðum leikjum eftir date_time
        matches.sort(key=lambda m: m.date_time)

        lines = []
        for m in matches:
            time_str = m.date_time.strftime("%Y-%m-%d %H:%M")
            lines.append(
                f"{time_str}: Match {m.match_id} - team {m.team_1_id} vs team {m.team_2_id} on server {m.server_id} game {m.game_id}"
            )
        return "\n".join(lines)

    def store_schedule_info(self, matches) -> None:
        for match in matches:
            self.match_data.store_match_info(match)
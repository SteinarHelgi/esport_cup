import csv
from Models.models import Tournament
from datetime import datetime
from IO.contact_person_data import ContactPersonData
from Models.models import ContactPerson
from IO.match_data import MatchData


class TournamentData:
    def __init__(self):
        self.tournament_file_path = "Data/Tournaments.csv"
        self.contact_person_data = ContactPersonData()
        self.match_data = MatchData()

    def get_all_tournament_data(self) -> list[Tournament]:
        tournaments = []
        with open(self.tournament_file_path, "r") as file:
            csvReader = csv.reader(file)
            next(csvReader)  # skip header
            for line in csvReader:
                if line != []:
                    id = line[0]
                    name = line[1]
                    start_date = datetime.fromisoformat(line[2])
                    end_date = datetime.fromisoformat(line[3])
                    venue = line[4]
                    game_id = line[5]
                    number_of_servers = line[6]
                    # contact_person_id = ContactPerson(line[7],"Hilmir","hilmir@rasshaus.is","8410536",)
                    contact_person_id = line[7]

                    tournament = Tournament(
                        name,
                        start_date,
                        end_date,
                        venue,
                        game_id,
                        number_of_servers,
                        contact_person_id,
                    )
                    tournament.set_id(id)
                    tournaments.append(tournament)
        return tournaments

    def store_tournament_data(self, tournament: Tournament) -> Tournament | None:
        with open(self.tournament_file_path, "a") as file:
            csvWriter = csv.writer(file)
            try:
                csvWriter.writerow(tournament.toCSVList())
            except:
                return None
        return tournament

    def delete_tournament_data(self, tournament_id: str) -> None:
        target_id = tournament_id

        #Creates a temporary data file
        temp_data = []
        
        try:
            with open(self.tournament_file_path, 'r', newline='') as file:
                reader = csv.reader(file)
        
        # Read the header row first
                header = next(reader) 
                temp_data.append(header) # Add header to the data we are keeping

        # Read the rest of the rows
                for line in reader:
                    # Check the value in the first column (index 0)
                    if line[0] != target_id:
                        temp_data.append(line)
                            
        except FileNotFoundError:
            exit()
        
        #Overwrites temporary datafile to csv file
        try:
            with open(self.tournament_file_path, 'w', newline='', encoding='utf-8') as csvfile:
                # Create a writer object
                writer = csv.writer(csvfile)
            
                # Iterate through the list of strings
                for line in temp_data:
                    writer.writerow(line)
        except:
            return None

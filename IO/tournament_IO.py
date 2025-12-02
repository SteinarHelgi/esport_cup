#Höfundur: Þröstur
#Tilbúið til rýni: Já
#Rýnir:
import csv
from Models.tournament import Tournament


class Tournament_IO:
    
    def __init__(self):
        self.tournamentFilepath = "Data/Tournaments.csv"
        

    def loadAllTournamentsFromCSV(self):
        tournaments = []
        with open(self.tournamentFilepath, "r+") as file:
            csvReader = csv.reader(file)
            next(csvReader) # skip header
            for line in csvReader:
                tournament = Tournament(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7])
                tournaments.append(tournament)
        file.close()
        return tournaments


    def storeNewTournament(self, tournament: Tournament):
        with open (self.tournamentFilepath, 'a') as file:
            csvWriter = csv.writer(file)
            try:
                csvWriter.writerow( tournament.toCSVList())
            except:
                return None
        return tournament    

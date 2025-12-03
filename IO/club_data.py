#Þröstur
import csv
from Models.club import Club

class ClubData:
    def __init__(self):
        self._filepath: str = "\Data\club.csv"
    

    def get_all_club_data(self) -> list[list[str]]:
        clubs: list[list] = []
        with open(self._filepath, "+r", encoding = "utf-8") as file:
            csvReader = csv.reader(file)
            next(csvReader)
            for line in csvReader:
                id: str = line[0]
                name: str = line[1]
                hometown: str = line[2]
                logo: str = line[3]
                all_club_colors: str = line[4]
                country: str = line[5]
                points: int = int(line[6])
                all_teams: str = line[7]
                
                # Tek ; úr strengnum og bý til lista af club colors
                club_colors: list = all_club_colors.split(";")
                club_colors_list: list = []
                for color in club_colors:
                    club_colors_list.append(color)
                
                # Tek ; úr strengnum og bý til lista af liðum
                teams: list = all_teams.split(";")
                teams_list: list = []
                for team in teams:
                    teams_list.append(team)
                club: list = [
                    id,
                    name,
                    hometown,
                    logo,
                    club_colors_list,
                    country,
                    points,
                    teams_list
                ]
                    

    def store_club_data(self, club: Club) -> Club | None:
        with open(self._filepath, "a") as file:
            csvWriter = csv.writer(file)
            try:
                csvWriter.writerow(club.toCSVList())
            except:
                return None
        return club
    

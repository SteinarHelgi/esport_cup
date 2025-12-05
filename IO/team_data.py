# Þröstur
import csv
from Models.models import Team


class TeamData:
    def __init__(self):
        self.team_file_path: str = "Data/teams.csv"

    def get_all_team_data(self) -> list[Team]:
        teams: list[Team] = []
        with open(self.team_file_path, "+r", encoding="utf-8") as file:
            csvReader = csv.reader(file)
            next(csvReader)
            for line in csvReader:
                id: str = line[0]
                name: str = line[1]
                captain_id: str = line[2]
                social_media: str = line[3]
                logo: str = line[4]
                team = Team(id, name, captain_id, social_media, logo)
                teams.append(team)
            return teams

    def store_team_data(self, team: Team) -> Team | None:
        with open(self.team_file_path, "a") as file:
            csvWriter = csv.writer(file)
            try:
                csvWriter.writerow(team.toCSVList())
            except:
                return None
        return team
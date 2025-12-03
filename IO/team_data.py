# Þröstur
import csv
from Models.models import Team


class TeamData:
    def __init__(self):
        self.team_file_path = "Data/TeamData.csv"

    def get_all_team_data(self) -> list[Team]:
        teams = []
        with open(self.team_file_path, "+r", encoding="utf-8") as file:
            csvReader = csv.reader(file)
            next(csvReader)
            for line in csvReader:
                id = int(line[0])
                name = line[1]
                all_players_handle_raw = line[2]
                logo = line[3]
                captain_id = int(line[4])
                social = line[5]
                club_id = line[6]
                points = int(line[7])
                all_players_handle = all_players_handle_raw.split(";")

                team = Team(
                    id,
                    name,
                    all_players_handle,
                    captain_id,
                    social,
                    club_id,
                    points,
                )
                teams.append(team)
            return teams

    def store_team_data(self, team: Team) -> Team:
        with open(self.team_file_path, "a") as file:
            csvWriter = csv.writer(file)
            try:
                csvWriter.writerow(team.toCSVList())
            except:
                return None
        return team

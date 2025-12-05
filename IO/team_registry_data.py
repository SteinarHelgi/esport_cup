import csv
from Models.team_registry import TeamRegistry

class TeamRegistry:
    def __init__(self):
        self._filepath: str = "Data/team_registry.py"

    def get_all_team_registry(self) -> list[TeamRegistry]:
        team_registries: list[TeamRegistry] = []
        with open(self._filepath, "+r", encoding = "utf-8") as file:
            csvReader = csv.reader(file)
            next(csvReader)
            for line in csvReader:
                team_id: str = line[0]
                tournament_id: str = line[1]
                team_registry = TeamRegistry(team_id, tournament_id)
                team_registries.append(team_registry)
            return team_registries
        
    def store_team_registry(self, team_registry: TeamRegistry) -> TeamRegistry | None:
        with open(self._filepath, "a") as file:
            csvWriter = csv.writer(file)
            try:
                csvWriter.writerow(team_registry.toCSVList())
            except:
                return None
        return team_registry

import csv
from Models.team_registry import TeamRegistry


class TeamRegistryData:
    def __init__(self):
        self._filepath: str = "Data/team_registry.csv"

    def get_all_team_registry_data(self) -> list[TeamRegistry]:
        team_registries: list[TeamRegistry] = []
        with open(self._filepath, "+r", encoding="utf-8") as file:
            csvReader = csv.reader(file)
            next(csvReader)
            for line in csvReader:
                if line:
                    team_id: str = line[0]
                    tournament_id: str = line[1]
                    team_name: str = line[2]
                    tournament_name: str = line[3]
                    team_registry = TeamRegistry(
                        team_id, tournament_id, team_name, tournament_name
                    )
                    team_registries.append(team_registry)
            return team_registries

    def store_team_registry_data(
        self, team_registry: TeamRegistry
    ) -> TeamRegistry | None:
        with open(self._filepath, "a" , newline="" , encoding="utf-8") as file:
            csvWriter = csv.writer(file)
            try:
                csvWriter.writerow(team_registry.toCSVList())
            except (OSError, csv.Error):
                return None
        return team_registry


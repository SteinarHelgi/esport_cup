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
                if line:
                    id: str = line[0]
                    name: str = line[1]
                    captain_id: str = line[2]
                    social_media: str = line[3]
                    logo: str = line[4]
                    team = Team(name, captain_id, social_media, logo)
                    team.set_id(id)
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

    def modify_team_data(self, team: Team) -> None:
        temp_data: list[list[str]] = []
        target_id: str = team.id

        # Creates a temporary data file without the modified team
        try:
            with open(self.team_file_path, "r", newline="") as file:
                reader = csv.reader(file)

                # Read the header row first and append it to temporary data
                header = next(reader)
                temp_data.append(header)

                for line in reader:
                    if line:
                        if line[0] != target_id:
                            temp_data.append(line)

        except FileNotFoundError:
            exit()

        # Overwrite temporary datafile to csv file
        try:
            with open(
                self.team_file_path, "w", newline="", encoding="utf-8"
            ) as csvfile:
                # Create a writer object
                writer = csv.writer(csvfile)

                # Iterate through the list of strings
                for line in temp_data:
                    writer.writerow(line)
        except:
            return None

        # add modified team to player database
        self.store_team_data(team)

    def give_team_points(self, team_name: str, added_points: int) -> None:
        temp_data: list[list[str]] = []
        target: str = team_name

        # Creates a temporary data file without the modified player
        try:
            with open(self.team_file_path, "r", newline="") as file:
                reader = csv.reader(file)

                # Read the header row first
                header = next(reader, None)
                if header:
                    temp_data.append(header)  # Add header to the data we are keeping

                # Read the rest of the rows
                for line in reader:
                    if not line:
                        continue
                    
                    if line[1] != target:
                        temp_data.append(line)
                    else:
                        try:
                            current_points: int = int(line[5])
                        except (ValueError, IndexError):
                            current_points = 0
                        new_points = current_points + added_points
                        line[5] = str(new_points)

                        temp_data.append(line)

                        id: str = line[0]
                        name: str = line[1]
                        captain_id: str = line[2]
                        social_media: str = line[3]
                        logo: str = line[4]
                        team: Team = Team(name, captain_id, social_media, logo)
                        team.set_id(id)
                        team.set_points(new_points)

        except FileNotFoundError:
            return

        # Overwrites temporary datafile to csv file
        try:
            with open(self.team_file_path, "w", newline="", encoding="utf-8") as csvfile:
                # Create a writer object
                writer = csv.writer(csvfile)

                # Iterate through the list of strings
                for line in temp_data:
                    writer.writerow(line)
        except:
            return None
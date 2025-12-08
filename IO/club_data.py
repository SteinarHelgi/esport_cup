import csv
from Models.models import Club, Team


class ClubData:
    def __init__(self) -> None:
        self.club_file_path = "Data/club.csv"

    def get_all_club_data(self):
        clubs: list[Club] = []
        with open(self.club_file_path, "r", encoding="utf-8") as file:
            csv_reader = csv.reader(file)
            #Skip header
            next(csv_reader)
            for line in csv_reader:
                if line:
                    id = line[0]
                    name = line[1]
                    hometown = line[2]
                    logo = line[3]
                    club_colors = line[4]
                    country = line[5]
                    points = int(line[6])
                    teams = line[7]

                    club = Club(name, hometown, logo, club_colors, country, teams)
                    club.set_id(id)
                    club.set_points(points)
    
                    clubs.append(club)
        return clubs

    def store_club_data(self, club: Club) -> Club | None:
        with open(self.club_file_path, "a", encoding="utf-8") as file:
            csv_writer = csv.writer(file)
            try:
                csv_writer.writerow(club.toCSVList())
            except:
                return None
        return club
    
    def add_team_to_club(self, team: Team, club_id: str):
        team_name_to_add = team.name
        temp_data: list[Club] = []
        target_id: str = club_id

        # Creates a temporary data file without the modified player
        try:
            with open(self.club_file_path, "r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)

                # Read the header row first
                header = next(reader)
                temp_data.append(header)  # Add header to the data we are keeping

                # Read the rest of the rows
                for line in reader:
                    # Check the value in the first column (index 0)
                    if line:
                        if line[0] != target_id:
                            temp_data.append(line)
                        else:
                            last_bit = line[-1]
                            new_last_bit = last_bit + f";{team_name_to_add}"
                            line[-1] = new_last_bit
                            temp_data.append(line)

        except FileNotFoundError:
            exit()

        # Overwrites temporary datafile to csv file
        try:
            with open(self.club_file_path, "w", newline="", encoding="utf-8") as csvfile:
                # Create a writer object
                writer = csv.writer(csvfile)

                # Iterate through the list of strings
                for line in temp_data:
                    writer.writerow(line)
        except:
            return None

    def give_club_points(self, club_name: str, added_points: int) -> None:
        temp_data: list[Club] = []
        target: str = club_name

        # Creates a temporary data file without the modified player
        try:
            with open(self.club_file_path, "r", newline="", encoding = "utf-8") as file:
                reader = csv.reader(file)

                # Read the header row first
                header = next(reader)
                temp_data.append(header)  # Add header to the data we are keeping

                # Read the rest of the rows
                for line in reader:
                    # Check the value in the first column (index 0)
                    if line:
                        if line[1] != target:
                            temp_data.append(line)
                        else:
                            id: str = line[0]
                            name: str = line[1]
                            hometown: str = line[2]
                            logo: str = line[3]
                            club_colors: str = line[4]
                            country: str = line[5]
                            points: int = int(line[6])
                            teams: str = line[7]
                            club: Club = Club(name, hometown, logo, club_colors, country, teams)
                            club.set_id(id)
                            club.set_points(points + added_points)

        except FileNotFoundError:
            exit()

        # Overwrites temporary datafile to csv file
        try:
            with open(self.club_file_path, "w", newline="", encoding="utf-8") as csvfile:
                # Create a writer object
                writer = csv.writer(csvfile)

                # Iterate through the list of strings
                for line in temp_data:
                    writer.writerow(line)
        except:
            return None
        #add the modified player to the database
        self.store_club_data(club)
# Sigrún
import csv
from Models.models import Club


class ClubData:
    def __init__(self) -> None:
        self.club_file_path = "Data/club.csv"

    def get_all_club_data(self) -> list[Club]:
        """Les alla klúbba úr CSV skránni og skilar lista af Club hlutum."""
        clubs = []

        with open(self.club_file_path, "r+", encoding="utf-8") as file:
            csv_reader = csv.reader(file)
            # Sleppum header-línu ef hún er til staðar
            next(csv_reader, None)
            for line in csv_reader:
                id = line[0]
                name = line[1]
                hometown = line[2]
                logo = line[3]
                club_colors = line[4]
                country = line[5]
                teams = line[7].split(";")

                points = 0
                if line[6] != "":
                    try:
                        points = line[6]
                    except ValueError:
                        points = 0
                # þarf að tengja teams í APIDATA svo er bara tómur listi hér

                club = Club(
                    id, name, hometown, logo, club_colors, country, str(points), teams
                )
                clubs.append(club)

            return clubs

    def store_club_data(self, club: Club) -> Club | None:
        """Bætir nýjum kúbbi aftast í CSV skrána."""
        with open(self.club_file_path, "a", encoding="utf-8") as file:
            csv_writer = csv.writer(file)
            try:
                csv_writer.writerow(club.toCSVList())
            except:
                return None
        return club

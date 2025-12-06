import csv
from Models.player import Player


class PlayerData:
    def __init__(self):
        self._filepath: str = "Data/players.csv"

    def get_all_player_data(self) -> list[Player]:
        players: list[Player] = []
        with open(self._filepath, "+r", encoding="utf-8") as file:
            csvReader = csv.reader(file)
            next(csvReader)  # skip header line
            for line in csvReader:
                if line != []:
                    player_id: str = line[0]
                    name: str = line[1]
                    date_of_birth: str = line[2]
                    address: str = line[3]
                    phone: str = line[4]
                    email: str = line[5]
                    link: str = line[6]
                    handle: str = line[7]
                    team_name: str = line[8]

                    player: Player = Player(
                        name,
                        date_of_birth,
                        address,
                        phone,
                        email,
                        link,
                        handle,
                        team_name,
                    )
                    player.set_id(player_id)
                    players.append(player)
            return players

    def store_player_data(self, player: Player) -> Player | None:
        with open(self._filepath, "a", newline="", encoding="utf=8") as file:
            csvWriter = csv.writer(file)
            try:
                csvWriter.writerow(player.toCSVList())
            except:
                return None
        return player

    def modify_player_data(self, player: Player) -> None:
        temp_data = []
        target_id = player.id

        # Creates a temporary data file
        try:
            with open(self._filepath, "r", newline="") as file:
                reader = csv.reader(file)

                # Read the header row first
                header = next(reader)
                temp_data.append(header)  # Add header to the data we are keeping

                # Read the rest of the rows
                for line in reader:
                    # Check the value in the first column (index 0)
                    if line[0] != target_id:
                        temp_data.append(line)

        except FileNotFoundError:
            exit()

        # Overwrites temporary datafile to csv file
        try:
            with open(self._filepath, "w", newline="", encoding="utf-8") as csvfile:
                # Create a writer object
                writer = csv.writer(csvfile)

                # Iterate through the list of strings
                for line in temp_data:
                    writer.writerow(line)
        except:
            return None

        self.store_player_data(player)

    def delete_player_data(self, player_id: str) -> None:
        target_id = player_id

        # Creates a temporary data file
        temp_data = []

        try:
            with open(self._filepath, "r", newline="") as file:
                reader = csv.reader(file)

                # Read the header row first
                header = next(reader)
                temp_data.append(header)  # Add header to the data we are keeping

                # Read the rest of the rows
                for line in reader:
                    # Check the value in the first column (index 0)
                    if line[0] != target_id:
                        temp_data.append(line)

        except FileNotFoundError:
            exit()

        # Overwrites temporary datafile to csv file
        try:
            with open(self._filepath, "w", newline="", encoding="utf-8") as csvfile:
                # Create a writer object
                writer = csv.writer(csvfile)

                # Iterate through the list of strings
                for line in temp_data:
                    writer.writerow(line)
        except:
            return None

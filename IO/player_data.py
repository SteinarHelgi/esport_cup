import csv
from datetime import datetime
from Models.player import Player


class PlayerData:
    def __init__(self):
        self._filepath: str = "Data/players.csv"


    def get_all_player_data(self) -> list[Player]:
        players: list[Player] = []
        with open(self._filepath, "+r", encoding="utf-8") as file:
            csvReader = csv.reader(file)
            next(csvReader) #skip header line
            for line in csvReader:
                player_id: str = line[0]
                name: str = line[1]
                date_of_birth: datetime = datetime.fromisoformat(line[2])
                address: str = line[3]
                phone: str = line[4]
                email: str = line[5]
                link: str = line[6]
                handle: str = line[7]
                team_name: str = line[8]

                player: Player = Player(
                    player_id,
                    name,
                    date_of_birth,
                    address,
                    phone,
                    email,
                    link,
                    handle,
                    team_name,
                )
                players.append(player)
            return players

    def store_player_data(self, player: Player) -> Player | None:
        with open(self._filepath, "a") as file:
            csvWriter = csv.writer(file)
            try:
                csvWriter.writerow(player.toCSVList())
            except:
                return None
        return player
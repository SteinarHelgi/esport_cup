from datetime import datetime
import csv

from Models.player import Player

# player_id,name,date_of_birth,address,phone,email,link,handle,team_name


class PlayerData:
    def __init__(self) -> None:
        self._filepath = "Data/players.csv"

    def get_all_player_data(self) -> list[Player]:
        players = []
        with open(self._filepath, "+r", encoding="utf-8") as file:
            csvReader = csv.reader(file)
            next(csvReader)
            for line in csvReader:
                player_id = line[0]
                name = line[1]
                date_of_birth = datetime.fromisoformat(line[2])
                address = line[3]
                phone = line[4]
                email = line[5]
                link = line[6]
                handle = line[7]
                team_name = line[8]

                player = Player(
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

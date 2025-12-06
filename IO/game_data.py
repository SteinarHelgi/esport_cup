import csv
from Models.models import Game

class GameData:
    def __init__(self) -> None:
        self.game_file_path = "Data/Games.csv"

    def get_all_game_data(self) -> list[Game]:
        """Les alla leiki úr CSV skránni og skilar lista af Game hlutum."""
        games = []
        with open(self.game_file_path, "r+") as file:
            csv_reader = csv.reader(file)
            # sleppum header-línu ef hún er til staðar
            next(csv_reader, None)
            for line in csv_reader:
                game_id = line[0]
                name = line[1]
                duration = line[2]

                game = Game(game_id, name, duration)
                games.append(game)
        return games

    def store_game_data(self, game: Game) -> Game | None:
        """Bætir nýjum leik aftast í CSV skrána."""
        with open(self.game_file_path, "a") as file:
            csv_writer = csv.writer(file)
            try:
                csv_writer.writerow(game.toCSVList())
            except:
                return None
        return game
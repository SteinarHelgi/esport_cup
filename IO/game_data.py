import csv
from Models.models import Game

class GameData:
    def __init__(self) -> None:
        self.game_file_path = "Data/Games.csv"

    def get_all_game_data(self) -> list[Game]:
        """Reads all games from the CSV file and returns a list of Game objects."""

        games: list[Game] = []

        # Open the file in read mode
        with open(self.game_file_path, "r+") as file:
            csv_reader = csv.reader(file)

            # Skip header row if present
            next(csv_reader, None)

            # Read each remaining line and create Game ojects
            for line in csv_reader:
                if not line:
                    continue  # Skip empty lines if any

                game_id = line[0]
                name = line[1]
                duration = line[2]

                game = Game(game_id, name, duration)
                games.append(game)

        return games

    def store_game_data(self, game: Game) -> Game | None:
        """Appends a new game to the CSV file. Returns the game if successful, otherwise None."""
        with open(self.game_file_path, "a") as file:
            csv_writer = csv.writer(file)
            try:
                csv_writer.writerow(game.toCSVList())
            except:
                return None
        return game
# Þröstur
import csv
from Models.models import Game


class GameData:
    def __init__(self):
        self._filepath: str = "Data/Game.csv"


    def get_all_game_data(self) -> list[Game]:
        games: list[Game] = []
        with open(self._filepath, "+r", encoding = "utf-8") as file:
            csvReader = csv.reader(file)
            next(csvReader)
            for line in csvReader:
                id: str = line[0]
                name: str = line[1]
                duration: int = int(line[2])
            game: Game = Game(id, name, duration)
            games.append(game)
        return games
    
    def store_game_data(self, game) -> Game | None:
        with open(self._filepath, "a") as file:
            csvWriter = csv.writer(file)
            try:
                csvWriter.csvwriterow(game.toCSVList())
            except:
                return None
        return game
    
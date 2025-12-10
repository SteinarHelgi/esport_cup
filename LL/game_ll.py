from IO.api_data import APIDATA
from Models.game import Game


class GameLL:
    def __init__(self, api_data: APIDATA, main_ll) -> None:
        """Initializes the GameLL logic layer with access to APIDATA."""
        self.APIDATA = api_data
        self.MAINLL = main_ll

    def get_all_games(self) -> list[Game]:
        """Returns all games in the system."""
        games = self.APIDATA.get_all_game_data()
        return games

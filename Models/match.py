import datetime as dt
from Models.models import Game


class Match:
    def __init__(
        self,
        match_id: str,
        date_time: dt.datetime,
        team_1_id: str,
        team_2_id: str,
        server_id: str,
        game_id: str,
    ):
        self.match_id = match_id
        self.date_time = date_time
        self.team_1_id = team_1_id
        self.team_2_id = team_2_id
        self.server_id = server_id
        self.game_id = game_id

    def toCSVList(self) -> list:
        return [
            self.match_id,
            self.date_time,
            self.team_1_id,
            self.team_2_id,
            self.server_id,
            self.game_id,
        ]


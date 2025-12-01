import datetime as dt

from game import Game

class Match:
    def __init__(self, team_id: int, date_time: dt, team_1_id: int, team_2_id: int, server_id: int, game: Game):
        self.team_id = team_id
        self.date_time = date_time
        self.team_1 = team_1_id
        self.team_2 = team_2_id
        self.server_id = server_id
        self.game = game
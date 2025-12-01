from match import Match
from tournament import Tournament

class Schedule:
    def __init__(self, schedule_id: int, matches: list[Match], tournament: Tournament):
        self.id = schedule_id
        self.matches = matches
        self.tournament = tournament
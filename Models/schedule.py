from Models.models import Match, Tournament


class Schedule:
    def __init__(self, schedule_id: int, matches: list[Match], tournament_id: str):
        self.id = schedule_id
        self.matches = matches
        self.tournament_id = tournament_id


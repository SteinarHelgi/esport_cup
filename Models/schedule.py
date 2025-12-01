class Match:
    def __init__(self):
        pass

class Tournament:
    def __init__(self):
        pass

class Schedule:
    def __init__(self, schedule_id: int, matches: list[Match], tournament: Tournament):
        self.id = schedule_id
        self.matches = matches
        self.tournament = tournament
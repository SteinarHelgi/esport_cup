class Match:
    def __init__(
        self,
        tournament_id: str,
        round: str,
        team_a_name: str,
        team_b_name: str,
        match_date: str,
        match_time: str,
        server_id: str,
        
    ):
        self.match_id = ""
        self.tournament_id = tournament_id
        self.round = round
        self.match_number = ""
        self.team_a_name = team_a_name
        self.team_b_name = team_b_name
        self.match_date = match_date
        self.match_time = match_time
        self.server_id = server_id
        self.score_a = 0
        self.score_b = 0
        self.winner_team_name = ""
        self.completed = False
        self.rounds: list[str] = ["R16", "QF", "SF", "Final"]

    def toCSVList(self) -> list:
        return [
            self.match_id,
            self.tournament_id,
            self.round,
            self.match_number,
            self.team_a_name,
            self.team_b_name,
            self.match_date,
            self.match_time,
            self.server_id,
            self.score_a,
            self.score_b,
            self.winner_team_name,
            self.completed,
        ]

    def __str__(self) -> str:
        return f"{self.team_a_name} vs {self.team_b_name} {self.match_date} at {self.match_time}"

    def set_id(self, id):
        self.match_id = id

    def set_match_number(self, id):
        self.match_number = id

    def set_score(self, score_a, score_b):
        self.score_a = score_a
        self.score_b = score_b

    def set_winner(self, winner_team):
        self.winner_team_name = winner_team
        self.completed = True
    
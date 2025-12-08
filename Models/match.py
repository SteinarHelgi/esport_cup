class Match:
    def __init__(
        self,
        tournament_id: str,
        round: str,
        team_a_name: str,
        team_b_name: str,
        match_date: str,
        match_time: str,
    ):
        self.match_id = ""
        self.tournament_id = tournament_id
        self.round = round
        self.match_number = ""
        self.team_a_name = team_a_name
        self.team_b_name = team_b_name
        self.match_date = match_date
        self.match_time = match_time
        self.server_id = ""
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
        w_team = 26
        w_date = 12
        w_time = 12
        w_round = 8
        w_vs = 4
        w_completed = 10

        return (
            f"{self.team_a_name:<{w_team}}"
            f"{'vs':^{w_vs}}"
            f"{self.team_b_name:>{w_team}}"
            f"{self.match_date:^{w_date}}"
            f"{self.match_time:^{w_time}}"
            f"{self.round:>{w_round}}"
            f"{str(self.completed):>{w_completed}}"
            f"{self.winner_team_name:>{w_team}}"
        )

    def set_id(self, id):
        self.match_id = id

    def set_match_number(self, id):
        self.match_number = id

    def set_score(self, score_a, score_b):
        self.score_a = score_a
        self.score_b = score_b

    def set_winner(self, winner_team, completed):
        self.winner_team_name = winner_team
        self.completed = completed

    def set_server_id(self, server_id):
        self.server_id = server_id

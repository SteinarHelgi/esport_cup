# match_id,tournament_id,round,match_number,team_a_name,team_b_name,match_date,match_time,server_id,score_a,score_b,winner_team_name,completed


class Match:
    def __init__(
        self,
        tournament_id: str,
        round: str,
        team_1_name: str,
        team_2_name: str,
        match_date: str,
        match_time: str,
    ):
        self.tournament_id = tournament_id
        self.round = round
        self.team_1_name = team_1_name
        self.team_2_name = team_2_name
        self.match_date = match_date
        self.match_time = match_time
        self.server_id = ""
        self.winner_team = ""
        self.completed = False

    def toCSVList(self) -> list:
        return [
            self.match_id,
            self.tournament_id,
            self.round,
            self.team_1_name,
            self.team_2_name,
            self.match_date,
            self.match_time,
            self.server_id,
            self.winner_team,
            self.completed,
        ]

    def __str__(self) -> str:
        return f"{self.team_1_name} vs {self.team_2_name} {self.match_date} at {self.match_time}"

    def set_id(self, id):
        self.match_id = id

    def set_winner(self, winner_team):
        self.winner_team = winner_team
        self.completed = True

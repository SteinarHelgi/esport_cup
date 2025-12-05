# match_id,tournament_id,round,match_number,team_a_name,team_b_name,match_date,match_time,server_id,score_a,score_b,winner_team_name,completed


class Match:
    def __init__(
        self,
        tournament_id: str,
        round: str,
        team_1_id: str,
        team_2_id: str,
        match_date: str,
        match_time: str,
        server_id: str,
        game_name: str,
    ):
        self.tournament_id = tournament_id
        self.round = round
        self.team_1_id = team_1_id
        self.team_2_id = team_2_id
        self.match_date = match_date
        self.match_time = match_time
        self.server_id = server_id
        self.winner_team = ""
        self.game_name = game_name
        self.completed = False

    def toCSVList(self) -> list:
        return [
            self.match_id,
            self.tournament_id,
            self.round,
            self.team_1_id,
            self.team_2_id,
            self.match_date,
            self.match_time,
            self.server_id,
            self.winner_team,
            self.game_name,
            self.completed,
        ]

    def set_id(self, id):
        self.match_id = id

    def set_winner(self, winner_team):
        self.winner_team = winner_team
        self.completed = True


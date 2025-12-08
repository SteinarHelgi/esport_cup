class EliminationStat:
    def __init__(
            self,
            team_name: str
    ) -> None:
            self.team_name = team_name
            self.games_played: int = 0
            self.won: int = 0
            self.lost: int = 0
            self.score_for: int = 0
            self.score_against: int = 0
            self.difference: int = 0
            self.winning_ratio: float = 0
            self.points: int = 0

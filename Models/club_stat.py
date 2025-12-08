class ClubStat:
    def __init__(
            self,
            club_name: str
    ) -> None:
            self.club_name = club_name
            self.games_played: int = 0
            self.won: int = 0
            self.lost: int = 0
            self.winning_ratio: float = 0
            self.points: int = 0

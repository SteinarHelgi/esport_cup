class PlayerStat:
    def __init__(
            self,
            player_handle: str
    ) -> None:
            self.player_handle = player_handle
            self.points: int = 0
            self.games_played: int = 0
            self.won: int = 0
            self.lost: int = 0
            self.winning_ratio: float = 0
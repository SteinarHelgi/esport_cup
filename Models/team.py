class Captain:
    def __init__(self):
        return


class Club:
    def __init__(self) -> None:
        pass


class Player:
    def __init__(self) -> None:
        pass


class Team:
    def __init__(
        self,
        id: int,
        name: str,
        players: list[Player],
        captain: Captain,
        social_media: str,
        club: Club,
        points: int,
    ) -> None:
        self.id = id
        self.name = name
        self.players = players
        self.captain = captain
        self.social_media = social_media
        self.club = club
        self.points = points

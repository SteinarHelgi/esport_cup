class Team:
    def __init__(
        self,
        id: int,
        name: str,
        list_of_players_id: list[str],
        captain_id: str,
        social_media: str,
        club: str,
        points: int,
    ) -> None:
        self.id = id
        self.name = name
        self.players = list_of_players_id
        self.captain_id = captain_id
        self.social_media = social_media
        self.club = club
        self.points = points

class Team:
    def __init__(
        self,
        name: str,
        captain_handle: str,
        social_media: str | None,
        logo: str,
    ) -> None:
        self.id: str = ""
        self.name: str = name
        self.captain_handle: str = captain_handle
        self.social_media: str | None = social_media
        self.logo: str = logo
        self.players: list[str] = []
        self.points: int = 0

    def __str__(self) -> str:
        return f"Name: {self.name}, Players: {self.players} Social Media: {self.social_media} Logo: {self.logo}"

    def toCSVList(self):
        ret = []
        ret.append(self.id)
        ret.append(self.name)
        ret.append(self.captain_handle)
        ret.append(self.social_media)
        ret.append(self.logo)
        ret.append(self.points)
        return ret

    def add_player(self, player_handle: str):
        self.players.append(player_handle)

    def set_id(self, id: str):
        self.id = id

    def set_points(self, points: int):
        self.points = points
class Team:
    def __init__(
        self,
        name: str,
        captain_id: str,
        social_media: str | None,
        logo: str,
    ) -> None:
        self.id = ""
        self.name = name
        self.captain_id = captain_id
        self.social_media = social_media
        self.logo = logo
        self.players = []
        self.points = 0

    def __str__(self) -> str:
        return f"Name: {self.name}, Players: {self.players}"

    def toCSVList(self):
        ret = []
        ret.append(self.id)
        ret.append(self.name)
        ret.append(self.captain_id)
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
class Team:
    def __init__(
        self,
        id: str = "2",
        name: str = "hi",
        captain_id: str = "hello",
        social_media: str | None = "hi",
        logo: str = "ASSCHI",
    ) -> None:
        self.id = id
        self.name = name
        self.captain_id = captain_id
        self.social_media = social_media
        self.logo = logo
        self.players = []

    def __str__(self) -> str:
        return f"Name: {self.name}, Players: {self.players}"

    def toCSVList(self):
        ret = []
        ret.append(self.id)
        ret.append(self.name)
        ret.append(self.captain_id)
        ret.append(self.social_media)
        ret.append(self.logo)
        return ret

    def add_player(self, player_handle: str):
        self.players.append(player_handle)

    def set_id(self, id: str):
        self.id = id
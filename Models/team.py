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

    def toCSVList(self):
        ret = []
        ret.append(self.id)
        ret.append(self.name)
        ret.append(self.captain_id)
        ret.append(self.social_media)
        ret.append(self.logo)
        return ret

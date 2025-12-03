class Team:
    def __init__(
        self,
        id: int,
        name: str,
        players: list[str],
        captain_id: str,
        social_media: str,
        club: str,
        points: int,
    ) -> None:
        self.id = id
        self.name = name
        self.players = players
        self.captain_id = captain_id
        self.social_media = social_media
        self.club = club
        self.points = points

    def toCSVList(self):
        ret = []
        players_string = ""
        ret.append(self.id)
        ret.append(self.name)
        for player in self.players:
            players_string += player
            players_string += ";"
        ret.append(players_string[:-1])
        ret.append(self.captain_id)
        ret.append(self.social_media)
        ret.append(self.club)
        ret.append(self.points)
        return ret


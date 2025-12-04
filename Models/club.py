from Models.models import Team


class Club:
    def __init__(
        self,
        id: str,
        name: str,
        hometown: str,
        logo: str,
        club_colors: str,
        country: str,
        points: str,
        teams: list[str],
    ) -> None:
        self.id = id
        self.name = name
        self.hometown = hometown
        self.logo = logo
        self.club_colors = club_colors
        self.country = country
        self.points = points
        self.teams = teams

    def toCSVList(self):
        ret = []
        ret.append(self.id)
        ret.append(self.name)
        ret.append(self.hometown)
        ret.append(self.logo)
        ret.append(self.club_colors)
        ret.append(self.country)
        ret.append(self.points)
        ret.append(self.teams)
        return ret

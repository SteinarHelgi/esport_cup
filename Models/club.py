from Models.models import Team


class Club:
    def __init__(
        self,
        name: str,
        hometown: str,
        logo: str,
        club_colors: str,
        country: str,
        teams: list[str],
    ) -> None:
        self.id = ""
        self.name = name
        self.hometown = hometown
        self.logo = logo
        self.club_colors = club_colors
        self.country = country
        self.points = 0
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

    def __str__(self) -> str:
        return f"name: {self.name} {self.teams}"
    
    def set_id(self, id: str):
        self.id = id

    def set_points(self, points: int):
        self.points = points

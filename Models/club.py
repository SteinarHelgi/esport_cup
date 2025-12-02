from Models.models import Team


class Club:
    def __init__(
        self,
        id: int,
        name: str,
        hometown: str,
        logo: str,
        club_colors: str,
        country: str,
        points: int,
        teams: list[Team],
    ) -> None:
        self.id = id
        self.name = name
        self.hometown = hometown
        self.logo = logo
        self.club_colors = club_colors
        self.country = country
        self.points = points
        self.teams = teams

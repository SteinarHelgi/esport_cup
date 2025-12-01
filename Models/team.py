from team_captain import TeamCaptain
from club import Club
from player import Player

class Team:
    def __init__(
        self,
        id: int,
        name: str,
        players: list[Player],
        captain: TeamCaptain,
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

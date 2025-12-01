import datetime as dt
from team import Team

class Player:
    def __init__(self, player_id: int, name: str, address: str, phone_number: int, email: str, social_media: str, team: Team, handle: str, points: int, date_of_birth: dt):
        self.player_id = player_id
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.social_media = social_media
        self.team = team
        self.handle = handle
        self.points = points
        self.date_of_birth = date_of_birth
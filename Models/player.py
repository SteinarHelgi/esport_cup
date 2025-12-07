import datetime as dt
from Models.models import Team

# player_id,name,date_of_birth,address,phone,email,link,handle,team_name


class Player:
    def __init__(
        self,
        name: str,
        date_of_birth: str,
        address: str,
        phone_number: str,
        email: str,
        social_media: str,
        handle: str,
        team_name: str,
    ):
        self.id = ""
        self.name = name
        self.date_of_birth = date_of_birth
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.social_media = social_media
        self.handle = handle
        self.team_name = team_name
        self.points = 0
        
    def get_team_name(self):
        return self.team_name

    def toCSVList(self):
        ret: list[str] = []
        ret.append(self.id)
        ret.append(self.name)
        ret.append(self.date_of_birth)
        ret.append(self.address)
        ret.append(self.phone_number)
        ret.append(self.email)
        ret.append(self.social_media)
        ret.append(self.handle)
        ret.append(self.team_name)
        ret.append(self.points)
        return ret

    def set_id(self, id: str):
        self.id = id

    def set_points(self, points: int):
        self.points = points
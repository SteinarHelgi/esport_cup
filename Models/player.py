import datetime as dt
from Models.models import Team

# player_id,name,date_of_birth,address,phone,email,link,handle,team_name


class Player:
    def __init__(
        self,
        player_id: str,
        name: str,
        date_of_birth: dt.datetime,
        address: str,
        phone_number: str,
        email: str,
        social_media: str,
        handle: str,
        team_name: str,
    ):
        self.player_id = player_id
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email
        self.social_media = social_media
        self.team_name = team_name
        self.handle = handle
        self.date_of_birth = date_of_birth

    def get_team_name(self):
        return self.team
    
    def toCSVList(self):
        ret: list[str] = []
        ret.append(self.player_id)
        ret.append(self.name)
        ret.append(self.address)
        ret.append(self.phone_number)
        ret.append(self.email)
        ret.append(self.social_media)
        ret.append(self.team_name)
        ret.append(self.handle)
        ret.append(self.date_of_birth)
        return ret


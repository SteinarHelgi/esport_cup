import datetime as datetime

# player_id,name,date_of_birth,address,phone,email,link,handle,team_name


class Player:
    w_player_name = 25
    w_player_handle = 20
    w_counter = 3
    w_club = 15

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

    # print header

    def print_header(self):
        print(
            f"{'ID':<{Player.w_counter}} {'PLAYER NAME':<{Player.w_player_name}} {'PLAYER HANDLE':<{Player.w_player_handle}}"
        )

    def format_row(self, index: int):
        print(
            f"{str(index) + '.':<{Player.w_counter}}"
            f"{self.name:<{Player.w_player_name}}"
            f"{self.handle:<{Player.w_player_handle}}"
        )

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
        ret.append(str(self.points))
        return ret

    def set_id(self, id: str):
        self.id = id

    def set_points(self, points: int):
        self.points = points


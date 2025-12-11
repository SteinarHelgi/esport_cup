class Team:
    w_name = 32
    w_captain = 32
    w_counter = 14
    w_social_media = 20
    w_logo = 20
    w_name_header = 20
    w_social_header = 15
    w_logo_header = 15
    w_captain_header = 15
    w_club = 15
    w_all_header = w_name_header + w_captain_header + w_social_header + w_logo_header

    def __init__(
        self,
        name: str,
        captain_handle: str,
        social_media: str | None,
        logo: str,
    ) -> None:
        self.id: str = ""
        self.name: str = name
        self.captain_handle: str = captain_handle
        self.social_media: str | None = social_media
        self.logo: str = logo
        self.players: list[str] = []
        self.points: int = 0
        self.club: str = "No club"

    def __str__(self) -> str:
        return f"{self.club:<{Team.w_club}} | {self.name:^{Team.w_name}} | {self.social_media:^{Team.w_social_media}} |  {self.logo:^{Team.w_logo}} |  {self.captain_handle:^{Team.w_captain}} |\n"

    def my_team_header(self):
        mainstr = f"{self.club:^{Team.w_club}} | {self.name:^{Team.w_name_header}} | {self.social_media:^{Team.w_social_header}} |  {self.logo:^{Team.w_logo_header}} |  {self.captain_handle:^{Team.w_captain_header}} |\n"
        return f"{'-' * len(mainstr)}\n{mainstr}{'-' * len(mainstr)}"

    def _print_header(self) -> None:
        # print header
        print(
            f"{'Id':<{Team.w_counter}}{'TEAM NAME':<{Team.w_name}}{'TEAM CAPTAIN':>{Team.w_captain}}\n"
        )

    def format_row(self, index: int):
        print(
            f"{str(index) + '.':<{Team.w_counter}}"
            f"{self.name:<{Team.w_name}}"
            f"{self.captain_handle:>{Team.w_captain}}"
        )

    def _print_divider_line(self):
        print("-" * (Team.w_name + Team.w_captain + Team.w_counter))

    def toCSVList(self):
        ret = []
        ret.append(self.id)
        ret.append(self.name)
        ret.append(self.captain_handle)
        ret.append(self.social_media)
        ret.append(self.logo)
        ret.append(self.points)
        return ret

    def add_player(self, player_handle: str):
        self.players.append(player_handle)

    def set_id(self, id: str):
        self.id = id

    def set_points(self, points: int):
        self.points = points

    def set_club(self, club: str):
        self.club = club

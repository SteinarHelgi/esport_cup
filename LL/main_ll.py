from IO.api_data import APIDATA
from LL.club_ll import ClubLL
from LL.team_ll import TeamLL
from LL.tournament_ll import TouranamentLL


class MainLL:
    def __init__(self, api_data: APIDATA) -> None:
        self.APIDATA = api_data
        self.tournament_ll = TouranamentLL(self.APIDATA, self)
        self.team_ll = TeamLL(self.APIDATA, self)
        self.club_ll = ClubLL(self.APIDATA, self)

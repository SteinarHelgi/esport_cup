from IO.api_data import APIDATA
from LL.user_ll import UserLL


class APILL:
    def __init__(self) -> None:
        self.api_data = APIDATA()
        self.userLL = UserLL(self.api_data)

    def get_all_teams(self):
        return self.userLL.get_all_teams()

    def get_all_tournaments(self):
        return self.userLL.get_all_tournaments()

from IO.api_data import APIDATA
from LL.team_captain_ll import TeamCaptainLL
from LL.user_ll import UserLL


class APILL:
    def __init__(self) -> None:
        self.api_data = APIDATA()
        self.userLL = UserLL(self.api_data)
        self.team_captain_ll = TeamCaptainLL(self.api_data)

    def get_all_teams(self):
        return self.userLL.get_all_teams()

    def get_all_tournaments(self):
        return self.userLL.get_all_tournaments()

    def get_ongoing_tournaments(self, today):
        return self.userLL.get_ongoing_tournament(today)

    def get_past_tournaments(self, today):
        return self.userLL.get_past_tournament(today)

    def get_upcoming_tournaments(self, today):
        return self.userLL.get_upcoming_tournament(today)

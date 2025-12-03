from IO.api_data import APIDATA
from LL.team_captain_ll import TeamCaptainLL
from LL.user_ll import UserLL
from Models.models import Tournament
from Models.player import Player
from Models.team import Team


class APILL:
    def __init__(self) -> None:
        self.api_data = APIDATA()
        self.userLL = UserLL(self.api_data)
        self.team_captain_ll = TeamCaptainLL(self.api_data)

    def get_all_teams(self) -> list[Team]:
        return self.userLL.get_all_teams()

    def get_all_tournaments(self) -> list[Tournament]:
        return self.api_data.get_tournament_data()

    def get_ongoing_tournaments(self, today) -> list[Tournament]:
        return self.userLL.get_ongoing_tournament(today)

    def get_past_tournaments(self, today) -> list[Tournament]:
        return self.userLL.get_past_tournament(today)

    def get_upcoming_tournaments(self, today) -> list[Tournament]:
        return self.userLL.get_upcoming_tournament(today)

    def get_players_in_team(self, team: str) -> list[Player]:
        return self.team_captain_ll.get_players_in_team(team)

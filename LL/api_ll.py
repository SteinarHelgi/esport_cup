from datetime import datetime
from IO.api_data import APIDATA
from LL.team_captain_ll import TeamCaptainLL
from LL.user_ll import UserLL
from LL.organiser_ll import OrganiserLL
from Models.models import Tournament, Player, Team, Match, ContactPerson


class APILL:
    def __init__(self) -> None:
        self.api_data = APIDATA()
        self.userLL = UserLL(self.api_data)
        self.team_captain_ll = TeamCaptainLL(self.api_data)
        self.organiser_ll = OrganiserLL(self.api_data)

    def get_all_teams(self) -> list[Team]:
        return self.userLL.get_all_teams()

    def get_players_in_team(self, team: str) -> list[Player]:
        return self.team_captain_ll.get_players_in_team(team)

    def get_all_tournaments(self) -> list[Tournament]:
        return self.api_data.get_all_tournament_data()

    def get_ongoing_tournaments(self, today) -> list[Tournament]:
        return self.userLL.get_ongoing_tournament(today)

    def get_past_tournaments(self, today) -> list[Tournament]:
        return self.userLL.get_past_tournament(today)

    def get_upcoming_tournaments(self, today) -> list[Tournament]:
        return self.userLL.get_upcoming_tournament(today)

    def get_team_by_captain_id(self, id) -> Team | None:
        return self.team_captain_ll.get_team_by_captain_id(id)

    def get_team_by_name(self, name) -> Team | None:
        return self.team_captain_ll.get_team_by_name(name)

    def create_tournament(self, tournament: Tournament) -> Tournament | None:
        return self.organiser_ll.create_tournament(tournament)

    def create_match(self) -> Match | None:
        return self.organiser_ll.create_match(self)

    def create_contact_person(self) -> ContactPerson | None:
        return self.organiser_ll.create_contact_person(self)

    def get_player_by_name(self) -> Player | None:
        return self.team_captain_ll.get_player_by_name(self)
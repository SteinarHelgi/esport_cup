from datetime import datetime
from IO.api_data import APIDATA
from LL.team_captain_ll import TeamCaptainLL
from LL.user_ll import UserLL
from LL.organiser_ll import OrganiserLL
from Models.models import (
    Tournament,
    Player,
    Team,
    Match,
    ContactPerson,
    TeamRegistry,
    TeamCaptain,
)
from Models.club import Club
# from Models.club_stat import ClubStat
# from Models.player_stat import PlayerStat


class APILL:
    def __init__(self) -> None:
        self.api_data = APIDATA()
        self.userLL = UserLL(self.api_data)
        self.team_captain_ll = TeamCaptainLL(self.api_data)
        self.organiser_ll = OrganiserLL(self.api_data)

    def get_all_teams(self) -> list[Team]:
        return self.userLL.get_all_teams()

    def get_all_tournaments(self) -> list[Tournament]:
        return self.api_data.get_all_tournament_data()

    def get_all_players(self) -> list:
        return self.userLL.get_all_players()

    def get_ongoing_tournaments(self) -> list[Tournament]:
        return self.userLL.get_ongoing_tournament()

    def get_past_tournaments(self) -> list[Tournament]:
        return self.userLL.get_past_tournament()

    def get_upcoming_tournaments(self) -> list[Tournament]:
        return self.userLL.get_upcoming_tournament()

    def create_player(self, player: Player) -> Player | None:
        return self.team_captain_ll.create_player(player)

    def modify_player(self, player: Player):
        return self.team_captain_ll.modify_player(player)

    def delete_player(self, player_id: str):
        return self.team_captain_ll.delete_player(player_id)

    def create_new_team(self, team: Team) -> Team | None:
        return self.team_captain_ll.create_new_team(team)

    def add_team_to_club(self, team: Team, club_id: str):
        return self.team_captain_ll.add_team_to_club(team, club_id)

    def get_all_club_data(self) -> list[Club]:
        return self.team_captain_ll.get_all_club_data()

    def get_all_teams_in_a_club(self, club_id) -> list[Team]:
        return self.team_captain_ll.get_all_teams_in_a_club(club_id)

    def modify_team_data(self, team: Team):
        return self.team_captain_ll.modify_team_data(team)

    def register_team_to_tournament(self, team: Team, tournament: Tournament):
        return self.team_captain_ll.register_team_to_tournament(team, tournament)

    def get_team_by_name(self, name) -> Team | None:
        return self.team_captain_ll.get_team_by_name(name)

    def get_players_in_team(self, team: str) -> list[Player]:
        return self.team_captain_ll.get_players_in_team(team)

    def get_player_by_name(self, player_name: str) -> Player | None:
        return self.team_captain_ll.get_player_by_name(player_name)

    def get_my_tournaments(self, team: Team) -> list[Tournament]:
        return self.team_captain_ll.get_my_tournaments(team)

    def get_tournament_by_id(self, tournament_id: str) -> Tournament | None:
        return self.team_captain_ll.get_tournament_by_id(tournament_id)

    def get_team_by_captain_id(self, handle) -> Team | None:
        return self.team_captain_ll.get_team_by_captain_handle(handle)

    # def get_all_club_stat(self) -> list[ClubStat]:
    #     return self.userLL.get_all_club_stat()

    def get_all_tournaments_for_captain(self, captain: TeamCaptain) -> list[Tournament]:
        return self.team_captain_ll.get_all_tournaments_for_captain(captain)

    def get_all_open_tournaments_for_captain(
        self, captain: TeamCaptain
    ) -> list[Tournament]:
        return self.team_captain_ll.get_all_open_tournaments_for_captain(captain)

    def create_tournament(self, tournament: Tournament) -> Tournament | None:
        return self.organiser_ll.create_tournament(tournament)

    def delete_tournament(self, tournament_id: str):
        return self.organiser_ll.delete_tournament(tournament_id)

    def create_match(self, match: Match) -> Match | None:
        return self.organiser_ll.create_match(match)

    def create_contact_person(
        self, contact_person: ContactPerson
    ) -> ContactPerson | None:
        return self.organiser_ll.create_contact_person(contact_person)

    def get_all_teams_on_tournament(self, target_tournament_id: str) -> list[Team]:
        return self.organiser_ll.get_all_teams_on_tournament(target_tournament_id)

    def register_match_result(
        self, match_id: str, home_score: int, away_score: int, completed: str
    ):
        return self.organiser_ll.register_match_result(
            match_id, home_score, away_score, completed
        )

    def get_tournament_by_name(self, tournament_name) -> Tournament | None:
        return self.organiser_ll.get_tournament_by_name(tournament_name)

    def get_contact_person_by_id(self, id: str) -> ContactPerson | None:
        return self.organiser_ll.get_contact_person_by_id(id)

    def get_contact_person(self, tournament_id: str) -> ContactPerson | None:
        return self.organiser_ll.get_contact_person(tournament_id)

    def give_player_points(self, handle: str, points: int):
        return self.organiser_ll.give_player_points(handle, points)

    def give_team_points(self, team_name: str, points: int):
        return self.organiser_ll.give_team_points(team_name, points)

    def give_club_points(self, club_name: str, points: int):
        return self.organiser_ll.give_club_points(club_name, points)

    # def show_player_stats_bar_chart(self):
    #     return self.userLL.show_player_stats_bar_chart()
    #
    # def get_elimination_stats(self, tournament_id):
    #     return self.userLL.get_elimination_stats(tournament_id)
    #
    # def get_all_player_stat(self, tournament_id) -> list[PlayerStat]:
    #     return self.userLL.get_all_player_stat(tournament_id)
    #
    # def get_player_stat(self, player_handle, tournament_id) -> PlayerStat | None:
    #     return self.userLL.get_player_stat(player_handle, tournament_id)


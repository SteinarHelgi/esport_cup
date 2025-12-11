from datetime import datetime
from IO.api_data import APIDATA
from Models.game import Game
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
from LL.main_ll import MainLL


class APILL:
    def __init__(self) -> None:
        self.APIDATA = APIDATA()
        self.main_ll = MainLL(self.APIDATA)

    def get_all_teams(self) -> list[Team]:
        return self.main_ll.team_ll.get_all_teams()

    def get_all_tournaments(self) -> list[Tournament]:
        return self.main_ll.tournament_ll.get_all_tournaments()

    def get_all_players(self) -> list:
        return self.main_ll.team_ll.get_all_players()

    def get_ongoing_tournaments(self) -> list[Tournament]:
        return self.main_ll.tournament_ll.get_ongoing_tournament()

    def get_past_tournaments(self) -> list[Tournament]:
        return self.main_ll.tournament_ll.get_past_tournament()

    def get_upcoming_tournaments(self) -> list[Tournament]:
        return self.main_ll.tournament_ll.get_upcoming_tournament()

    def create_player(self, player: Player) -> Player | None:
        return self.main_ll.team_ll.create_player(player)

    def modify_player(self, player: Player):
        return self.main_ll.team_ll.modify_player(player)

    def delete_player(self, player_id: str):
        return self.main_ll.team_ll.delete_player(player_id)

    def create_new_team(self, team: Team) -> Team | None:
        return self.main_ll.team_ll.create_new_team(team)

    def add_team_to_club(self, team: Team, club_id: str):
        return self.main_ll.club_ll.add_team_to_club(team, club_id)

    def get_all_club_data(self) -> list[Club]:
        return self.main_ll.club_ll.get_all_club_data()

    def get_all_teams_in_a_club(self, club_id) -> list[Team]:
        return self.main_ll.club_ll.get_all_teams_in_a_club(club_id)

    def modify_team_data(self, team: Team) -> Team | None:
        return self.main_ll.team_ll.modify_team_data(team)

    def register_team_to_tournament(self, team: Team, tournament: Tournament):
        return self.main_ll.team_ll.register_team_to_tournament(team, tournament)

    def get_team_by_name(self, name) -> Team | None:
        return self.main_ll.team_ll.get_team_by_name(name)

    def get_team_by_id(self, id) -> Team | None:
        return self.main_ll.team_ll.get_team_by_id(id)

    def get_players_in_team(self, team: str) -> list[Player]:
        return self.main_ll.team_ll.get_players_in_team(team)

    def get_player_by_name(self, player_name: str) -> Player | None:
        return self.main_ll.team_ll.get_player_by_name(player_name)

    def get_my_tournaments(self, team: Team) -> list[Tournament]:
        return self.main_ll.team_ll.get_my_tournaments(team)

    def get_tournament_by_id(self, tournament_id: str) -> Tournament | None:
        return self.main_ll.tournament_ll.get_tournament_by_id(tournament_id)

    def get_all_matches_by_type(
        self, tournament: Tournament, type_of_round: str
    ) -> list[Match]:
        return self.main_ll.tournament_ll.get_all_matches_by_type(
            tournament, type_of_round
        )

    def get_teams_not_in_round(self, tournament: Tournament):
        return self.main_ll.tournament_ll.get_teams_not_in_round(tournament)

    def get_team_by_captain_handle(self, handle) -> Team | None:
        return self.main_ll.team_ll.get_team_by_captain_handle(handle)

    # def get_all_club_stat(self) -> list[ClubStat]:
    #     return self.userLL.get_all_club_stat()

    def get_all_tournaments_for_team(self, team: Team) -> list[Tournament]:
        return self.main_ll.tournament_ll.get_all_tournaments_for_team(team)

    def get_teams_in_tournament(self, tournament: Tournament) -> list[Team]:
        return self.main_ll.tournament_ll.get_teams_in_tournament(tournament)

    def get_all_open_tournaments_for_captain(
        self, captain: TeamCaptain
    ) -> list[Tournament]:
        return self.main_ll.tournament_ll.get_all_open_tournaments_for_captain(captain)

    def create_tournament(self, tournament: Tournament) -> Tournament | None:
        return self.main_ll.tournament_ll.create_tournament(tournament)

    def delete_tournament(self, tournament_id: str):
        return self.main_ll.tournament_ll.delete_tournament(tournament_id)

    def create_match(self, match: Match) -> Match | None:
        return self.main_ll.tournament_ll.create_match(match)

    def create_contact_person(
        self, contact_person: ContactPerson
    ) -> ContactPerson | None:
        return self.main_ll.tournament_ll.create_contact_person(contact_person)

    def get_all_teams_on_tournament(self, target_tournament_id: str) -> list[Team]:
        return self.main_ll.tournament_ll.get_all_teams_on_tournament(
            target_tournament_id
        )

    def register_match_result(self, match_id: str, winner_name: str, completed: str):
        """Registering match results"""
        return self.main_ll.tournament_ll.register_match_result(
            match_id, winner_name, completed
        )

    def get_tournament_by_name(self, tournament_name) -> Tournament | None:
        return self.main_ll.tournament_ll.get_tournament_by_name(tournament_name)

    def get_contact_person_by_id(self, id: str) -> ContactPerson | None:
        return self.main_ll.tournament_ll.get_contact_person_by_id(id)

    def get_contact_person(self, tournament_id: str) -> ContactPerson | None:
        return self.main_ll.tournament_ll.get_contact_person(tournament_id)

    def give_team_points(self, team_name: str, points: int):
        return self.main_ll.tournament_ll.give_team_points(team_name, points)

    def get_all_games(self) -> list[Game]:
        return self.main_ll.game_ll.get_all_games()

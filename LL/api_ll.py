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

from LL.validators_ll import (
    Errors,
    validate_player_name,
    validate_date_of_birth,
    validate_address,
    validate_phone_number,
    validate_player_email,
    validate_player_handle,
    validate_social_media,
    validate_team_captain,
    validate_team_name,
    validation_team_handle,
    validate_team_logo,
    validate_team_points,
    validate_tournament_name,
    validate_tournament_start_date,
    validate_tournament_end_date,
    validate_tournament_servers,
    validate_tournament_venue,
    validate_tournament_game,
    validate_players_in_teams,
    validate_match_round,
    validate_match_creation,
    validate_match_date,
    validate_match_time,
    validate_game_name,
    validate_club_name,
    validate_club_hometown,
    validate_club_color,
    validate_club_country
)

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



       #-------------------VALIDATION--------------------------
    
    def validate_player_name(self, name: str) -> Errors:
        return validate_player_name(name)

    def validate_date_of_birth(self,date_of_birth: str) -> Errors:
        return validate_date_of_birth(date_of_birth)

    def validate_address(self,address: str) -> Errors:
        return validate_address(address)
    
    def validate_phone_number(self,phone_number) -> Errors:
        return validate_phone_number(phone_number)
    
    def validate_player_email(self,player_email) -> Errors:
        return validate_player_email(player_email)

    def validate_player_handle(self, player_handle) -> Errors:
        return validate_player_handle(player_handle, self.APIDATA)

    def validate_social_media(self, social_media) -> Errors:
        return validate_social_media(social_media)   

# -----------TEAM CAPTAIN VALIDATION-------------

    def validate_team_captain(self, handle: str) -> Errors:
        return validate_team_captain(handle, self.APIDATA)

# -------------TEAM VALIDATION---------------

    def validate_team_name(self,name: str) -> Errors:
        return validate_team_name(name, self.APIDATA)

    def validation_team_handle(self,handle: str) -> Errors:
        return validation_team_handle(handle, self.APIDATA)

    def validate_team_logo(self,logo: str) -> Errors:
        return validate_team_logo(logo)

    def validate_team_points(self,points: str) -> Errors:
        return validate_team_points(points)

# -------------TOURNAMENT VALIDATION--------------

    def validate_tournament_name(self, name) -> Errors:
        return validate_tournament_name(name)

    def validate_tournament_start_date(self, start_date) -> Errors:
        return validate_tournament_start_date(start_date)

    def validate_tournament_end_date(self, start_date, end_date) -> Errors:
        return validate_tournament_end_date(start_date, end_date)

    def validate_players_in_teams(self, players_in_team) -> Errors:
        return validate_players_in_teams(players_in_team)

    def validate_tournament_servers(self, servers) -> Errors:
        return validate_tournament_servers(servers)

    def validate_tournament_venue(self, venue) -> Errors:
        return validate_tournament_venue(venue)

    def validate_tournament_game(self, user_input_game, games) -> Errors:
        return validate_tournament_game(user_input_game, games)

# ----------------MATCH VALIDATION--------------------

    def validate_match_round(self, round_name: str, matches_in_round: list) -> Errors:
        return validate_match_round(round_name, matches_in_round)

    def validate_match_creation(self, match: Match, tournament: Tournament) -> Errors:
        return validate_match_creation(match, tournament, self.APIDATA )

    def validate_match_date(self, date_input: str, tournament_start_date: datetime, tournament_end_date: datetime) -> Errors:
        return validate_match_date(date_input, tournament_start_date, tournament_end_date)

    def validate_match_time(self, time_input: str) -> Errors:
        return validate_match_time(time_input)

# -----------------GAME VALIDATION--------------------
    def validate_game_name(self, game_name: str) -> Errors:
        return validate_game_name(game_name, self.APIDATA)

# -----------------CLUB VALIDATION--------------------

    def validate_club_name(self, name: str) -> Errors:
        return validate_club_name(name)

    def validate_club_hometown(self, hometown: str) -> Errors:
        return validate_club_hometown(hometown)

    def validate_club_color(self, color: str) -> Errors:
        return validate_club_color(color)

    def validate_club_country(self, country: str) -> Errors:
        return validate_club_country(country)
from datetime import datetime
from IO.api_data import APIDATA
from LL.main_ll import MainLL
from Models.models import (
    Game,
    Tournament,
    Player,
    Team,
    Match,
    ContactPerson,
    TeamCaptain,
    Club
)

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
    validate_club_country,
    validate_unwanted_characters
)

class APILL:
    def __init__(self) -> None:
        self.APIDATA = APIDATA()
        self.main_ll = MainLL(self.APIDATA)

    def get_all_teams(self) -> list[Team]:
        """Returns a list of all teams in the system."""
        return self.main_ll.team_ll.get_all_teams()

    def get_all_tournaments(self) -> list[Tournament]:
        """Returns a list of all tournaments in the system."""
        return self.main_ll.tournament_ll.get_all_tournaments()

    def get_all_players(self) -> list:
        """Returns a list of all players in the system."""
        return self.main_ll.team_ll.get_all_players()

    def get_ongoing_tournaments(self) -> list[Tournament]:
        """Returns tournaments that are currently in progress."""
        return self.main_ll.tournament_ll.get_ongoing_tournament()

    def get_past_tournaments(self) -> list[Tournament]:
        """Returns tournaments that have already finished."""
        return self.main_ll.tournament_ll.get_past_tournament()

    def get_upcoming_tournaments(self) -> list[Tournament]:
        """Returns tournaments that start in the future."""
        return self.main_ll.tournament_ll.get_upcoming_tournament()

    def create_player(self, player: Player) -> Player | None:
        """Creates a new player through the logic layer and returns the stored player."""
        return self.main_ll.team_ll.create_player(player)

    def modify_player(self, player: Player):
        """Updates an existing player's data."""
        return self.main_ll.team_ll.modify_player(player)

    def delete_player(self, player_id: str):
        """Deletes a player with the given ID."""
        return self.main_ll.team_ll.delete_player(player_id)

    def create_new_team(self, team: Team) -> Team | None:
        """Creates a new team through the logic layer and returns the stored team."""
        return self.main_ll.team_ll.create_new_team(team)

    def add_team_to_club(self, team: Team, club: Club):
        """Adds a team to a club with the given club ID."""
        return self.main_ll.club_ll.add_team_to_club(team, club)

    def get_all_club_data(self) -> list[Club]:
        """Returns a list of all clubs in the system."""
        return self.main_ll.club_ll.get_all_club_data()

    def get_all_teams_in_a_club(self, club_id) -> list[Team]:
        """Returns all teams that belong to a given club."""
        return self.main_ll.club_ll.get_all_teams_in_a_club(club_id)

    def modify_team_data(self, team: Team) -> Team | None:
        """Updates an existing team's data."""
        return self.main_ll.team_ll.modify_team_data(team)

    def register_team_to_tournament(self, team: Team, tournament: Tournament):
        """Registers a team into a given tournament."""
        return self.main_ll.team_ll.register_team_to_tournament(team, tournament)

    def get_team_by_name(self, name) -> Team | None:
        """Returns a team by its name, or None if not found."""
        return self.main_ll.team_ll.get_team_by_name(name)

    def get_team_by_id(self, id) -> Team | None:
        """Returns a team by its ID, or None if not found."""
        return self.main_ll.team_ll.get_team_by_id(id)

    def get_players_in_team(self, team: str) -> list[Player]:
        """Returns all players that belong to a team with the given name."""
        return self.main_ll.team_ll.get_players_in_team(team)

    def get_player_by_name(self, player_name: str) -> Player | None:
        """Returns a player by name, or None if not found."""
        return self.main_ll.team_ll.get_player_by_name(player_name)

    def get_my_tournaments(self, team: Team) -> list[Tournament]:
        """Returns all tournaments a given team is registered for."""
        return self.main_ll.team_ll.get_my_tournaments(team)

    def get_tournament_by_id(self, tournament_id: str) -> Tournament | None:
        """Returns a tournament by its ID, or None if not found."""
        return self.main_ll.tournament_ll.get_tournament_by_id(tournament_id)

    def get_all_matches_by_type(
        self, tournament: Tournament, type_of_round: str
    ) -> list[Match]:
        """Returns all matches in a specific round type for a given tournament."""
        return self.main_ll.tournament_ll.get_all_matches_by_type(
            tournament, type_of_round
        )

    def get_teams_not_in_round(self, tournament: Tournament):
        """Returns teams in a tournament that are not yet assigned to the given round."""
        return self.main_ll.tournament_ll.get_teams_not_in_round(tournament)

    def get_team_by_captain_handle(self, handle) -> Team | None:
        """Returns the team whose captain has the given handle, or None if not found."""
        return self.main_ll.team_ll.get_team_by_captain_handle(handle)

    # def get_all_club_stat(self) -> list[ClubStat]:
    #     return self.userLL.get_all_club_stat()

    def get_all_tournaments_for_team(self, team: Team) -> list[Tournament]:
        """Returns all tournaments a given team is (or was) participating in."""
        return self.main_ll.tournament_ll.get_all_tournaments_for_team(team)

    def get_teams_in_tournament(self, tournament: Tournament) -> list[Team]:
        """Returns all teams that are registered in a given tournament."""
        return self.main_ll.tournament_ll.get_teams_in_tournament(tournament)

    def get_all_open_tournaments_for_captain(
        self, captain: TeamCaptain
    ) -> list[Tournament]:
        """Returns tournaments that the captain's team can still register for."""
        return self.main_ll.tournament_ll.get_all_open_tournaments_for_captain(captain)

    def create_tournament(self, tournament: Tournament) -> Tournament | None:
        """Creates a new tournament through the logic layer and returns the stored tournament."""
        return self.main_ll.tournament_ll.create_tournament(tournament)

    def delete_tournament(self, tournament_id: str):
        """Deletes a tournament with the given ID."""
        return self.main_ll.tournament_ll.delete_tournament(tournament_id)

    def create_match(self, match: Match) -> Match | None:
        """Creates a new match through the logic layer and returns the stored match."""
        return self.main_ll.tournament_ll.create_match(match)

    def create_contact_person(
        self, contact_person: ContactPerson
    ) -> ContactPerson | None:
        """Creates a new contact person and stores it through the logic layer."""
        return self.main_ll.tournament_ll.create_contact_person(contact_person)

    def get_all_teams_on_tournament(self, target_tournament_id: str) -> list[Team]:
        """Returns all teams registered for a tournament with the given ID."""
        return self.main_ll.tournament_ll.get_all_teams_on_tournament(
            target_tournament_id
        )

    def register_match_result(self, match_id: str, winner_name: str, completed: str):
        """Registers the result of a match (winner and completion status)."""
        return self.main_ll.tournament_ll.register_match_result(
            match_id, winner_name, completed
        )

    def get_tournament_by_name(self, tournament_name) -> Tournament | None:
        """Returns a tournament by its name, or None if not found."""
        return self.main_ll.tournament_ll.get_tournament_by_name(tournament_name)

    def get_contact_person_by_id(self, id: str) -> ContactPerson | None:
        """Returns a contact person by ID, or None if not found."""
        return self.main_ll.tournament_ll.get_contact_person_by_id(id)

    def get_contact_person(self, tournament_id: str) -> ContactPerson | None:
        """Returns the contact person associated with a given tournament."""
        return self.main_ll.tournament_ll.get_contact_person(tournament_id)

    def give_team_points(self, team_name: str, points: int):
        """Adds points to a team with the given name."""
        return self.main_ll.tournament_ll.give_team_points(team_name, points)

    def get_all_games(self) -> list[Game]:
        """Returns a list of all games available in the system."""
        return self.main_ll.game_ll.get_all_games()

    # ---------- PLAYER VALIDATION ----------
    def validate_player_name(self, name: str) -> Errors:
        return validate_player_name(name)

    def validate_date_of_birth(self, date_of_birth: str) -> Errors:
        return validate_date_of_birth(date_of_birth)

    def validate_address(self, address: str) -> Errors:
        return validate_address(address)

    def validate_phone_number(self, phone_number: str) -> Errors:
        return validate_phone_number(phone_number)

    def validate_player_email(self, player_email: str) -> Errors:
        return validate_player_email(player_email)

    def validate_player_handle(self, player_handle: str) -> Errors:
        return validate_player_handle(player_handle, self.APIDATA)

    def validate_social_media(self, social_media: str) -> Errors:
        return validate_social_media(social_media)

    # ---------- TEAM CAPTAIN VALIDATION ----------

    def validate_team_captain(self, handle: str) -> Errors:
        return validate_team_captain(handle, self.APIDATA)

    # ---------- TEAM VALIDATION ----------

    def validate_team_name(self, name: str) -> Errors:
        return validate_team_name(name, self.APIDATA)

    def validation_team_handle(self, handle: str) -> Errors:
        return validation_team_handle(handle, self.APIDATA)

    def validate_team_logo(self, logo: str) -> Errors:
        return validate_team_logo(logo)

    def validate_team_points(self, points: str) -> Errors:
        return validate_team_points(points)

    # ---------- TOURNAMENT VALIDATION ----------

    def validate_tournament_name(self, name: str) -> Errors:
        return validate_tournament_name(name)

    def validate_tournament_start_date(self, start_date: str) -> Errors:
        return validate_tournament_start_date(start_date)

    def validate_tournament_end_date(self, start_date: str, end_date: str) -> Errors:
        return validate_tournament_end_date(start_date, end_date)

    def validate_players_in_teams(self, players_in_team: list[Player]) -> Errors:
        return validate_players_in_teams(players_in_team)

    def validate_tournament_servers(self, servers: str) -> Errors:
        return validate_tournament_servers(servers)

    def validate_tournament_venue(self, venue: str) -> Errors:
        return validate_tournament_venue(venue)

    def validate_tournament_game(
        self, user_input_game: str, games: list[Game]
    ) -> Errors:
        return validate_tournament_game(user_input_game, games)

    # ----------------MATCH VALIDATION--------------------

    def validate_match_round(self, round_name: str, matches_in_round: list) -> Errors:
        return validate_match_round(round_name, matches_in_round)

    def validate_match_creation(self, match: Match, tournament: Tournament) -> Errors:
        return validate_match_creation(match, tournament, self.APIDATA)

    def validate_match_date(
        self,
        date_input: str,
        tournament_start_date: datetime,
        tournament_end_date: datetime,
    ) -> Errors:
        return validate_match_date(
            date_input, tournament_start_date, tournament_end_date
        )

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
    
    def validate_unwanted_characters(self,input: str) -> Errors:
        return validate_unwanted_characters(self)


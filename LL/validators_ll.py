from Models.models import Player, TeamCaptain, Team, Match, Tournament
from datetime import datetime, date
from IO.api_data import APIDATA
from enum import Enum, auto


class Errors(Enum):
    EMPTY = auto()
    NAME_INCLUDE_NUMBERS = auto()
    HANDLE_EXIST = auto()
    TEAM_NAME_TOO_LONG = auto()
    LOGO_EMPTY = auto()
    POINTS_NEGATIVE = auto()
    DATE_NOT_VALID = auto()
    DATE_TOO_OLD = auto()
    ADDRESS_ONLY_NUMBERS = auto()
    NUMBER_HAS_CHARACTERS = auto()
    NUMBER_NOT_CORRECT_LENGTH = auto()
    EMAIL_NOT_CONTAINING_AT = auto()
    HANDLE_CONTAINS_SPACE = auto()
    TOURNAMENT_NAME_LENGTH = auto()
    TOURNAMENT_NAME_LENGTH_TOO_LONG = auto()
    END_DATE_BEFORE_START = auto()
    DATE_FORMAT_NOT_VALID = auto()
    START_DATE_BEFORE_TODAY = auto()
    SERVER_LESS_THAN_0 = auto()
    SERVER_NOT_NUMBER = auto()
    NOT_Y_OR_N = auto()
    VENUE_INCLUDE_NUMBERS = auto()
    GAME_NOT_VALID = auto()
    ROUND_NOT_VALID = auto()
    TOO_MANY_GAMES_IN_ROUND = auto()
    CLUB_INCLUDE_NUMBERS = auto()
    HOMETOWN_CONTAINS_NUMBER = auto()
    INVALID_COLOR = auto()
    COLOR_HAS_NUMBER = auto()
    CLUB_COUNTRY_HAS_NUMBER = auto()
    TOO_MANY_PLAYERS = auto()
    SAME_HANDLE = auto()
    TEAM_CAPTAIN_NOT_EXISTS = auto()
    PLAYERS_NOT_ENOUGH = auto()
    PLAYERS_TOO_MANY = auto()
    DATE_NOT_IN_TOURNAMENT_DATE = auto()
    TIME_NOT_IN_TIMESLOT = auto()
    TEAM_A_ALREADY_IN_SLOT = auto()
    TEAM_B_ALREADY_IN_SLOT = auto()
    TEAM_A_ALREADY_IN_ROUND = auto()
    TEAM_B_ALREADY_IN_ROUND = auto()
    INVALID_SERVER_COUNT = auto()
    TIMESLOT_FULL = auto()
    TEAM_A_LOST_LAST_ROUND = auto()
    TEAM_B_LOST_LAST_ROUND = auto()
    TEAM_NAME_TAKEN = auto()
    OK = auto()


class ValidationError(Exception):
    pass


def validate_player_name(player_name: str) -> Errors:
    valid_name = player_name.strip()
    if valid_name == "":
        return Errors.EMPTY
    if any(char.isdigit() for char in valid_name):
        return Errors.NAME_INCLUDE_NUMBERS
    return Errors.OK


def validate_date_of_birth(date_of_birth):
    valid_dob = date_of_birth.strip()

    if valid_dob == "":
        return Errors.EMPTY
    try:
        dob = datetime.strptime(valid_dob, "%Y-%m-%d")
        if dob.year < 1900:
            return Errors.DATE_TOO_OLD
        return Errors.OK
    except ValueError:
        return Errors.DATE_NOT_VALID


def validate_address(address):
    valid_address = address.strip()

    if valid_address == "":
        return Errors.EMPTY

    if valid_address.replace(" ", "").isdigit():
        return Errors.ADDRESS_ONLY_NUMBERS
    return Errors.OK


def validate_phone_number(phone_number):
    number = phone_number.strip()

    if number == "":
        return Errors.EMPTY

    if not number.isdigit():
        return Errors.NUMBER_HAS_CHARACTERS

    if len(number) != 7:
        return Errors.NUMBER_NOT_CORRECT_LENGTH
    return Errors.OK


def validate_player_email(player_email):
    email = player_email.strip()

    if email == "":
        return Errors.EMPTY

    if email.count("@") != 1:
        return Errors.EMAIL_NOT_CONTAINING_AT
    return Errors.OK


def validate_player_handle(player_handle, api_data: APIDATA):
    handle = player_handle.strip()

    if handle == "":
        return Errors.EMPTY

    if " " in handle:
        return Errors.HANDLE_CONTAINS_SPACE

    current_players = api_data.get_all_player_data()

    for p in current_players:
        if p.handle == handle:
            Errors.SAME_HANDLE

    return Errors.OK


def validate_social_media(social_media):
    socials = social_media.strip()
    if socials == "":
        return Errors.EMPTY
    if socials == " ":
        return Errors.HANDLE_CONTAINS_SPACE
    return Errors.OK


# -----------TEAM CAPTAIN VALIDATION-------------


def validate_team_captain(handle: str, api_data: APIDATA) -> Errors:
    # Handle
    if not handle or not handle.strip():
        return Errors.EMPTY

    current_players = api_data.get_all_player_data()

    if any(p.handle == handle for p in current_players):
        return Errors.HANDLE_EXIST

    return Errors.OK


# -------------TEAM VALIDATION---------------

MAX_PLAYERS = 5


def validate_team_name(name: str, api_data: APIDATA) -> Errors:
    # Name
    if not name or name.strip() == "":
        return Errors.EMPTY

    if len(name) > 40:
        return Errors.TEAM_NAME_TOO_LONG

    # Max 5 players in a team
    current_players = api_data.get_all_player_data()

    players_in_team = [p for p in current_players if p.team_name == name]
    if len(players_in_team) >= MAX_PLAYERS:
        Errors.TOO_MANY_PLAYERS

    current_teams = api_data.get_all_team_data()

    for t in current_teams:
        if t.name == name:
            return Errors.TEAM_NAME_TAKEN

    return Errors.OK


def validation_team_handle(handle: str, api_data: APIDATA) -> Errors:
    # Captain handle

    if not handle or handle.strip() == "":
        return Errors.EMPTY

    current_players = api_data.get_all_player_data()

    if not any(p.handle == handle for p in current_players):
        return Errors.TEAM_CAPTAIN_NOT_EXISTS

    return Errors.OK


def validate_team_logo(logo: str) -> Errors:
    # Logo
    if not logo or logo.strip() == "":
        return Errors.EMPTY
    return Errors.OK


def validate_team_points(points: str) -> Errors:
    # Points
    if points == "":
        return Errors.EMPTY
    elif int(points) < 0:
        return Errors.POINTS_NEGATIVE

    return Errors.OK


# -------------TOURNAMENT VALIDATION--------------


def validate_tournament_name(name) -> Errors:
    if len(name.strip()) < 2:
        return Errors.TOURNAMENT_NAME_LENGTH
    if len(name) >= 40:
        return Errors.TOURNAMENT_NAME_LENGTH_TOO_LONG
    return Errors.OK


def validate_tournament_start_date(start_date) -> Errors:
    # Verður að vera rétt format
    # Start date verður að vera eftir daginn í dag
    try:
        start_date_iso = date.fromisoformat(start_date)
    except ValueError:
        return Errors.DATE_FORMAT_NOT_VALID
    if start_date_iso <= date.today():
        return Errors.START_DATE_BEFORE_TODAY
    return Errors.OK


def validate_tournament_end_date(start_date, end_date) -> Errors:
    # Verður að vera rétt format.
    # Verður að byrja eftir start date
    try:
        end_date_iso = date.fromisoformat(end_date)
    except ValueError:
        return Errors.DATE_FORMAT_NOT_VALID

    if end_date_iso < date.fromisoformat(start_date):
        return Errors.END_DATE_BEFORE_START
    return Errors.OK


def validate_players_in_teams(players_in_team) -> Errors:
    MIN_PLAYERS_PER_TEAM = 3
    MAX_PLAYERS_PER_TEAM = 5

    num_players = len(players_in_team)
    if num_players < MIN_PLAYERS_PER_TEAM:
        return Errors.PLAYERS_NOT_ENOUGH
    elif num_players > MAX_PLAYERS_PER_TEAM:
        return Errors.PLAYERS_TOO_MANY
    return Errors.OK


def validate_tournament_servers(servers) -> Errors:
    if not servers.isdigit():
        return Errors.SERVER_NOT_NUMBER
    if int(servers) < 1:
        return Errors.SERVER_LESS_THAN_0
    return Errors.OK


def validate_tournament_venue(venue) -> Errors:
    if venue.isdigit():
        return Errors.VENUE_INCLUDE_NUMBERS
    return Errors.OK





def validate_tournament_game(user_input_game, games) -> Errors:
    for game in games:
        if game.name == user_input_game:
            return Errors.OK
    return Errors.GAME_NOT_VALID


# ----------------MATCH VALIDATION--------------------


def validate_match_round(round_name: str, matches_in_round: list) -> Errors:
    expected_matches_by_round = {
        "R16": 8,
        "QF": 4,
        "SF": 2,
        "Final": 1,
    }

    if round_name not in expected_matches_by_round:
        return Errors.ROUND_NOT_VALID

    expected = expected_matches_by_round[round_name]
    actual = len(matches_in_round)

    if actual != expected:
        return Errors.TOO_MANY_GAMES_IN_ROUND
    return Errors.OK


def validate_match_creation(
    match: Match, tournament: Tournament, api_data: APIDATA
) -> Errors:
    team_a = match.team_a_name
    team_b = match.team_b_name
    date_str = match.match_date
    time_str = match.match_time
    round_name = match.round
    tournament_id = str(match.tournament_id)

    try:
        servers = int(tournament.no_servers)
        if servers < 1:
            return Errors.INVALID_SERVER_COUNT
    except ValueError:
        return Errors.INVALID_SERVER_COUNT

    all_matches = api_data.get_all_match_data()
    matches_in_tournament = [
        m for m in all_matches if str(m.tournament_id) == tournament_id
    ]

    # Same team already playing (date+time)
    for m in matches_in_tournament:
        if m.match_date == date_str and m.match_time == time_str:
            teams_in_match = (m.team_a_name, m.team_b_name)
            if team_a in teams_in_match:
                return Errors.TEAM_A_ALREADY_IN_SLOT

            if team_b in teams_in_match:
                return Errors.TEAM_B_ALREADY_IN_SLOT

    # Team already in the round for the tournament
    for m in matches_in_tournament:
        if m.round == round_name:
            teams_in_match = (m.team_a_name, m.team_b_name)
            if team_a in teams_in_match:
                return Errors.TEAM_A_ALREADY_IN_ROUND
            if team_b in teams_in_match:
                return Errors.TEAM_B_ALREADY_IN_ROUND

    # time slot availability vs server availability
    matches_in_same_slot = [
        m
        for m in matches_in_tournament
        if m.match_date == date_str and m.match_time == time_str
    ]
    if len(matches_in_same_slot) >= servers:
        return Errors.TIMESLOT_FULL

    # Only winners advance
    round_order = ["R16", "QF", "SF", "Final"]
    if round_name in round_order:
        idx = round_order.index(round_name)
        if idx > 0:
            prev_round = round_order[idx - 1]
            prev_round_matches = [
                m for m in matches_in_tournament if m.round == prev_round
            ]
            winners = {
                m.winner_team_name
                for m in prev_round_matches
                if m.winner_team_name != ""
            }
            if team_a not in winners:
                return Errors.TEAM_A_LOST_LAST_ROUND
            if team_b not in winners:
                return Errors.TEAM_B_LOST_LAST_ROUND
    return Errors.OK


def validate_match_date(
    date_input: str, tournament_start_date: datetime, tournament_end_date: datetime
) -> Errors:
    try:
        date_input_iso = datetime.fromisoformat(date_input)
    except ValueError:
        return Errors.DATE_FORMAT_NOT_VALID
    if tournament_start_date > date_input_iso < tournament_end_date:
        return Errors.DATE_NOT_IN_TOURNAMENT_DATE
    return Errors.OK


def validate_match_time(time_input: str):
    time_slots = ["08:00", "10:00", "12:00", "14:00", "16:00", "18:00", "20:00"]
    if time_input not in time_slots:
        return Errors.TIME_NOT_IN_TIMESLOT
    return Errors.OK


# -----------------GAME VALIDATION--------------------
def validate_game_name(game_name: str, api_data: APIDATA) -> Errors:
    valid_game = game_name.strip()

    if valid_game == "":
        return Errors.EMPTY

    available_games = api_data.get_all_game_data()

    game_names = [g.name for g in available_games]

    if valid_game not in game_names:
        Errors.GAME_NOT_VALID
    return Errors.OK


# -----------------CLUB VALIDATION--------------------


def validate_club_name(name: str) -> Errors:
    if not name or name.strip() == "":
        return Errors.OK
    if any(char.isdigit() for char in name):
        return Errors.CLUB_INCLUDE_NUMBERS

    return Errors.OK


def validate_club_hometown(hometown: str) -> Errors:
    if not hometown or hometown.strip() == "":
        raise ValueError("You must enter a club hometown")
        return Errors.Hom
    if any(char.isdigit() for char in hometown):
        return Errors.HOMETOWN_CONTAINS_NUMBER

    return Errors.OK


def validate_club_color(color: str) -> Errors:
    if not color or color.strip() == "":
        return Errors.OK
    if any(char.isdigit() for char in color):
        return Errors.COLOR_HAS_NUMBER

    allowed_colors = [
        "Red",
        "Blue",
        "Green",
        "Yellow",
        "Black",
        "White",
        "Purple",
        "Orange",
        "Pink",
        "Gray",
        "Brown",
    ]

    club_color = color.strip().lower()

    if club_color not in allowed_colors:
        return Errors.INVALID_COLOR

    return Errors.OK


def validate_club_country(country: str) -> Errors:
    if not country or country.strip() == "":
        return Errors.EMPTY
    if any(char.isdigit() for char in country):
        return Errors.CLUB_COUNTRY_HAS_NUMBER
    return Errors.OK

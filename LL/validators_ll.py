from Models.models import Player, TeamCaptain, Team
from datetime import datetime, date
from IO.api_data import APIDATA
from enum import Enum


class Errors(Enum):
    NAME_EMPTY = 404
    NAME_ONLY_NUMBERS = 403
    HANDLE_EMPTY = 2
    HANDLE_EXIST = 3
    TEAM_NAME_EMPTY = 4
    TEAM_NAME_TOO_LONG = 5
    LOGO_EMPTY = 6
    POINTS_EMPTY = 7
    POINTS_NEGATIVE = 8
    CLUB_NAME_EMPTY = 9
    CLUB_NAME_INVALID = 10
    HOMETOWN_EMPTY = 11
    HOMETOWN_INVALID = 12

    OK = 1





class ValidationError(Exception):
    pass


def validate_player_name(player_name: str) -> Errors:
    valid_name = player_name.strip()
    if valid_name == "":
        return Errors.NAME_EMPTY
    if any(char.isdigit() for char in valid_name):
        return Errors.NAME_ONLY_NUMBERS
    return Errors.OK


def validate_date_of_birth(date_of_birth):
    valid_dob = date_of_birth.strip()

    if valid_dob == "":
        raise ValueError("Date of birth cannot be empty")

    try:
        dob = datetime.strptime(valid_dob, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Date of birth must be in the format YYYY-MM--DD")

    if dob.year < 1900:
        raise ValueError("Please consult a doctor you might be dead, try again")
    return date_of_birth


def validate_address(address):
    valid_address = address.strip()

    if valid_address == "":
        raise ValueError("Address cannot be empty")

    if valid_address.replace(" ", "").isdigit():
        raise ValueError("Address cannot be only numbers")
    return address


def validate_phone_number(phone_number):
    number = phone_number.strip()

    if number == "":
        raise ValueError("Phone number cannot be empty")

    if not number.isdigit():
        raise ValueError("Phone number must contain numbers only")

    if len(number) != 7:
        raise ValueError("Phone number must be exactly 7 digits long")
    return phone_number


def validate_player_email(player_email):
    email = player_email.strip()

    if email == "":
        raise ValueError("Email cannot be empty")

    if email.count("@") != 1:
        raise ValueError("Email must contain exactly one '@'")

    if "." not in email:
        raise ValueError("Email must contain at least one '.'")
    return player_email


def validate_player_handle(player_handle):
    handle = player_handle.strip()

    if handle == "":
        raise ValueError("Hnadle cannot be empty")

    if " " in handle:
        raise ValueError("Handle cannot contain space")
    return player_handle


# -----------TEAM CAPTAIN VALIDATION-------------


def validate_team_captain(handle: str, api_data: APIDATA) -> Errors:
    # Handle
    if not handle or not handle.strip():
        return Errors.HANDLE_EMPTY

    current_players = api_data.get_all_player_data()

    if any(p.handle == handle for p in current_players):
       return Errors.HANDLE_EXIST

    return Errors.OK


# -------------TEAM VALIDATION---------------


def validate_team_name(name: str) -> Errors:
    # Name
    if not name or name.strip() == "":
        return Errors.TEAM_NAME_EMPTY

    if len(name) > 40:
        return Errors.TEAM_NAME_TOO_LONG

    return Errors.OK


def validation_team_handle(handle: str, api_data: APIDATA) -> Errors:
    # Captain handle

    if not handle or handle.strip() == "":
        raise ValueError("You must enter a team captain handle")

    current_players = api_data.get_all_player_data()

    if not any(p.handle == handle for p in current_players):
        raise ValueError("No team captain exists with that handle")

    return Errors.OK


def validate_team_logo(logo: str) -> Errors:
    # Logo
    if not logo or logo.strip() == "":
        return Errors.LOGO_EMPTY
    return Errors.OK


def validate_team_players(players: list[str]) -> None:
    pass


def validate_team_points(points: str) -> Errors:
    # Points
    if points is None:
        Errors.POINTS_EMPTY
    elif int(points) < 0:
        Errors.POINTS_NEGATIVE

    return Errors.OK


# -------------TOURNAMENT VALIDATION--------------

def validate_tournament_name(name) -> str | None:
    if len(name.strip()) < 2:
        raise ValidationError("Name of tournament be atleast 3 characters")
    if len(name) <= 40:
        return name
    else:
        raise ValidationError("Name cannot be longer than 40 characters")


def validate_tournament_start_date(start_date) -> str | None:
    # Verður að vera rétt format
    # Start date verður að vera eftir daginn í dag
    try:
        start_date_iso = date.fromisoformat(start_date)
    except ValueError:
        raise ValidationError("Not correct format")
    if start_date_iso <= date.today():
        raise ValidationError("Invalid start date")
    return start_date


def validate_tournament_end_date(start_date, end_date) -> str | None:
    # Verður að vera rétt format.
    # Verður að byrja eftir start date
    try:
        end_date_iso = date.fromisoformat(end_date)
    except ValueError:
        raise ValidationError("Not correct format")
    if end_date_iso < date.fromisoformat(start_date):
        raise ValidationError("Invalid end date")
    return end_date


def validate_tournament_servers(servers) -> str | None:
    if not servers.isdigit():
        raise ValidationError("Amount of servers must be a number")
    if int(servers) < 1:
        raise ValidationError("Amount of servers be greater than 0")
    return servers


def validate_tournament_venue(venue) -> str | None:
    if venue.isdigit():
        raise ValidationError("Invalid Venue name")
    return venue


def validate_tournament_double_elimination(double_elimination):
    if double_elimination.lower() == "y" or double_elimination.lower() == "n":
        return double_elimination
    else:
        raise ValidationError("Only Y or N")


def validate_tournament_game(user_input_game, games) -> str | None:
    for game in games:
        if game.name == user_input_game:
            return game
    raise ValidationError("Not a valid game")


# ----------------MATCH VALIDATION-------------------- 

def validate_match_round(round_name: str, matches_in_round: list) -> None:

    expected_matches_by_round = {
        "R16": 8,
        "QF": 4,
        "SF": 2,
        "Final": 1,
    }

    if round_name not in expected_matches_by_round:
        raise ValidationError(f"'{round_name}' is not a valid round.")

    expected = expected_matches_by_round[round_name]
    actual = len(matches_in_round)

    if actual != expected:
        raise ValidationError(
            f"Round '{round_name}' must have {expected} matches, "
            f"but got {actual}."
        )

# -----------------GAME VALIDATION--------------------

def validate_game_name(game_name: str, api_data: APIDATA) -> str | None:
    valid_game = game_name.strip()

    if valid_game == "":
        raise ValidationError("Game name cannot be empty")
    
    available_games = api_data.get_all_game_data()

    game_names = [g.name for g in available_games]

    if valid_game not in game_names:
        raise ValidationError(
            f"'{valid_game}' is not an available game. "
            f"Available gmaes are: {', '.join(game_names)}."
        )
    
    return valid_game

# -----------------CLUB VALIDATION--------------------

def validate_club_name(name:str) -> Errors:
    if not name or name.strip() == "":
        Errors.CLUB_NAME_EMPTY
    if any(char.isdigit() for char in name):
        Errors.CLUB_NAME_INVALID
    
    return Errors.OK

def validate_club_hometown(hometown:str) -> Errors:
    if not hometown or hometown.strip() == "":
        Errors.HOMETOWN_EMPTY
    if any(char.isdigit() for char in hometown):
        Errors.HOMETOWN_INVALID
 
    return Errors.OK

def validate_club_color(color:str) -> Errors:
    if not color or color.strip() == "":
        raise ValueError("You must enter a club color")
    if any(char.isdigit() for char in color):
        raise ValueError("Invalid color")
    
    allowed_colors = ["Red", "Blue", "Green", "Yellow", "Black", "White", "Purple", "Orange", "Pink", "Gray", "Brown"]
    
    club_color = color.strip().lower()

    if club_color not in allowed_colors:
        raise ValueError("Invalid club color. Allowed colors are: " + ", ".join(allowed_colors))
    
    return Errors.OK

def validate_club_country(country:str) -> Errors:
    if not country or country.strip() == "":
        raise ValueError("You must enter a club country")
    if any(char.isdigit() for char in country):
        raise ValueError("Invalid country")
    return Errors.OK
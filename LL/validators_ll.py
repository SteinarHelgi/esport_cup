from Models.models import Player, TeamCaptain, Team
from datetime import datetime, date
from IO.api_data import APIDATA


class ValidationError(Exception):
    pass


def validate_player_name(player_name: str) -> str:

    valid_name = player_name.strip()

    if valid_name == "":
        raise ValidationError("Name can not be empty.")

    if any(char.isdigit() for char in valid_name):
        raise ValidationError("Name can not include numbers")
    return valid_name


def validate_date_of_birth(date_of_birth) -> str | None:
    valid_dob = date_of_birth.strip()

    if valid_dob == "":
        raise ValidationError("Date of birth cannot be empty")

    try:
        dob = datetime.strptime(valid_dob, "%Y-%m-%d")
    except ValidationError:
        raise ValidationError("Date of birth must be in the format YYYY-MM--DD")

    if dob.year < 1900:
        raise ValidationError("Please consult a doctor you might be dead, try again")
    return date_of_birth


def validate_address(address) -> str | None:
    valid_address = address.strip()

    if valid_address == "":
        raise ValidationError("Address cannot be empty")

    if valid_address.replace(" ", "").isdigit():
        raise ValidationError("Address cannot be only numbers")
    return address


def validate_phone_number(phone_number) -> str | None:
    number = phone_number.strip()

    if number == "":
        raise ValidationError("Phone number cannot be empty")

    if not number.isdigit():
        raise ValidationError("Phone number must contain numbers only")

    if len(number) != 7:
        raise ValidationError("Phone number must be exactly 7 digits long")
    return phone_number


def validate_player_email(player_email) -> str | None:
    email = player_email.strip()

    if email == "":
        raise ValidationError("Email cannot be empty")

    if email.count("@") != 1:
        raise ValidationError("Email must contain exactly one '@'")

    if "." not in email:
        raise ValidationError("Email must contain at least one '.'")
    return player_email


def validate_player_handle(player_handle: str, api_data: APIDATA) -> str | None:
    handle = player_handle.strip()

    if handle == "":
        raise ValidationError("Hnadle cannot be empty")

    if " " in handle:
        raise ValidationError("Handle cannot contain space")
    
    current_players = api_data.get_all_player_data()
    for p in current_players:
        if p.handle == handle:
            raise ValidationError("Handle is already taken")
        
    return player_handle


# -----------TEAM CAPTAIN VALIDATION-------------


def validate_team_captain(handle: str, api_data: APIDATA) -> str | None:
    # Handle
    if not handle or not handle.strip():
        raise ValueError("Handle may not be empty")

    current_players = api_data.get_all_player_data()

    if any(p.handle == handle for p in current_players):
        raise ValueError("Handle already exists, please choose an unique handle")

    return handle


# -------------TEAM VALIDATION---------------


def validate_team_name(name: str) -> str | None:
    # Name
    if not name or name.strip() == "":
        raise ValueError("You must enter a team name")

    if len(name) > 40:
        raise ValueError("Team name can't be longer than 40 characters")

    return name


def validation_team_handle(handle: str, api_data: APIDATA) -> str | None:
    # Captain handle

    if not handle or handle.strip() == "":
        raise ValueError("You must enter a team captain handle")

    current_players = api_data.get_all_player_data()

    if not any(p.handle == handle for p in current_players):
        raise ValueError("No team captain exists with that handle")

    return handle


def validate_team_logo(logo: str) -> str | None:
    # Logo
    if not logo or logo.strip() == "":
        raise ValueError("Team logo may not be empty")
    return logo


def validate_team_players(players: list[str]) -> None:
    pass


def validate_team_points(points: str) -> str | None:
    # Points
    if points is None:
        raise ValueError("Points may not be empty")
    elif int(points) < 0:
        raise ValueError("Points may not be negative")

    return points


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

def validate_club_name(name:str) -> str | None:
    if not name or name.strip() == "":
        raise ValueError("You must enter a club name")
    if any(char.isdigit() for char in name):
        raise ValueError("Invalid club name")
    
    return name

def validate_club_hometown(hometown:str) -> str | None:
    if not hometown or hometown.strip() == "":
        raise ValueError("You must enter a club hometown")
    if any(char.isdigit() for char in hometown):
        raise ValueError("Invalid hometown")
 
    return hometown

def validate_club_color(color:str) -> str | None:
    if not color or color.strip() == "":
        raise ValueError("You must enter a club color")
    if any(char.isdigit() for char in color):
        raise ValueError("Invalid color")
    
    color_list = [c.strip().lower() for c in color.split(",") if c.strip()]

    if len(color_list) > 4:
        raise ValueError("You can only have four colors in club color")
    
    allowed_colors = ["Red", "Blue", "Green", "Yellow", "Black", "White", "Purple", "Orange", "Pink", "Gray", "Brown"]
    
    for color in color_list:
        if color not in allowed_colors:
            raise ValueError(f"Invalid club color: {color} Allowed colors are: "  ", ".join(allowed_colors))

    return ",".join([c.strip() for c in color.split(",") if c.strip()])
    
 
def validate_club_country(country:str) -> str | None:
    if not country or country.strip() == "":
        raise ValueError("You must enter a club country")
    if any(char.isdigit() for char in country):
        raise ValueError("Invalid country")
    return country

def validate_club_teams(teams:str) -> str | None:
    pass

def validate_club_logo(logo:str) -> str | None:
    if not logo or logo.strip() == "":
        raise ValueError("You must enter a club logo")
    return logo


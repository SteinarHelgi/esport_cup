from Models.models import Player, TeamCaptain, Team
from datetime import datetime, date
from IO.api_data import APIDATA

class ValidationError(Exception):
    pass

#----------PLAYER VALIDATION------------

def validate_player(player: Player) -> None:
    errors = []

    valid_name = player.name.strip()

    if valid_name == "":
        raise ValueError("Name can not be empty.")
    
    if any(char.isdigit() for char in valid_name):
        raise ValueError("Name can not include numbers")

def validate_date_of_birth(date_of_birth: str) -> None:

    valid_dob = date_of_birth.strip()

    if valid_dob == "":
        raise ValueError("Date of birth cannot be empty")
    
    try:
        dob = datetime.strptime(valid_dob, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Date of birth must be in the format YYYY-MM--DD")

    if dob.year < 1900:
        raise ValueError("Please consult a doctor you might be dead, try again")

def validate_address(address: str) -> None:

    valid_address = address.strip()

    if valid_address == "":
        raise ValueError("Address cannot be empty")
    
    if valid_address.replace(" ","").isdigit():
        raise ValueError("Address cannot be only numbers")

def validate_phone_number(phone_number: str) -> None:

    number = phone_number.strip()

    if number == "":
        raise ValueError("Phone number cannot be empty")

    if not number.isdigit():
        raise ValueError("Phone number must contain numbers only")
    
    if len(number) != 7:
        raise ValueError("Phone number must be exactly 7 digits long")
    
def validate_player_email(player_email: str) -> None:

    email = player_email.strip()

    if email == "":
        raise ValueError("Email cannot be empty")
    
    if email.count("@") != 1:
        raise ValueError("Email must contain exactly one '@'")
    
    if "." not in email:
        raise ValueError("Email must contain at least one '.'")

def validate_player_handle(player_handle: str) -> None:

    handle = player_handle.strip()

    if handle == "":
        raise ValueError("Hnadle cannot be empty")
    
    if " " in handle:
        raise ValueError("Handle cannot contain space")
    
#--------------TEAM VALIDATION---------------
"""
def validate_team_captain(team_captain: TeamCaptain) -> None:
    errors: list[str] = []
    # Team id
    if not team_captain.team_id:
        errors.append("Team id may not be empty")
    # Handle
    if not team_captain.handle or not team_captain.handle.strip():
        errors.append("Handle may not be empty")
"""


def validate_team_name(name: str) -> None:
    # Name
    if not name or name.strip() == "":
        raise ValueError("You must enter a team name")
    
    if len(name) > 40:
        raise ValueError("Team name can't be longer than 40 characters")

def validation_team_handle(handle:str, api_data:APIDATA) -> None:
    # Captain handle

    if not handle or handle.strip() == "":
        raise ValueError("You must enter a team captain handle")
    
    current_players = api_data.get_all_player_data()

    if not any(p.handle == handle for p in current_players):
        raise ValueError("No team captain exists with that handle")

def validate_team_logo(logo: str) -> None:
    # Logo
    if not logo or logo.strip() == "":
        raise ValueError("Team logo may not be empty")


def validate_team_players(players: list[str]) -> None:
    pass


def validate_team_points(points: int) -> None:
    # Points
    if points is None:
        raise ValueError("Points may not be empty") 
    elif points < 0:
        raise ValueError("Points may not be negative")


#-------------TOURNAMENT VALIDATION--------------

def validate_tournament_name(name):
    if len(name.strip()) < 2:
        raise ValidationError("Name of tournament be atleast 3 characters")
    if len(name) <= 40:
        return name
    else:
        raise ValidationError("Name cannot be longer than 40 characters")


def validate_tournament_start_date(start_date):
    # Verður að vera rétt format
    # Start date verður að vera eftir daginn í dag
    try:
        start_date_iso = date.fromisoformat(start_date)
    except ValueError:
        raise ValidationError("Not correct format")
    if start_date_iso <= date.today():
        raise ValidationError("Invalid start date")
    return start_date


def validate_tournament_end_date(start_date, end_date):
    # Verður að vera rétt format.
    # Verður að byrja eftir start date
    try:
        end_date_iso = date.fromisoformat(end_date)
    except ValueError:
        raise ValidationError("Not correct format")
    if end_date_iso < date.fromisoformat(start_date):
        raise ValidationError("Invalid end date")
    return end_date


def validate_tournament_servers(servers):
    if not servers.isdigit():
        raise ValidationError("Amount of servers must be a number")
    if int(servers) < 1:
        raise ValidationError("Amount of servers be greater than 0")
    return servers


def validate_tournament_venue(venue):
    if venue.isdigit():
        raise ValidationError("Invalid Venue name")
    return venue


def validate_tournament_double_elimination(double_elimination):
    if double_elimination.lower() == "y" or double_elimination.lower() == "n":
        return double_elimination
    else:
        raise ValidationError("Only Y or N")


def validate_tournament_game(game):
    games = ["Valorant", "CS:GO", "League of Legends", "Rocket League", "Fortnite"]
    if game not in games:
        raise ValidationError("Game must be ", *games)

    return game

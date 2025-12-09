
from curses.ascii import isdigit
from datetime import datetime
from Models.models import Player, TeamCaptain, Team
import ValidationError


def validate_player_name(name: str) -> None:

    valid_name = name.strip()

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
    


    # Team name


def validate_team_captain(team_captain: TeamCaptain) -> None:
    errors: list[str] = []
    # Team id
    if not team_captain.team_id:
        errors.append("Team id may not be empty")
    # Handle
    if not team_captain.handle or not team_captain.handle.strip():
        errors.append("Handle may not be empty")

    if errors:
        raise ValidationError(errors)


def validate_team(team: Team) -> None:
    errors: list[str] = []
    # Name
    if not team.name or team.name.strip() == "":
        errors.append("Team name may not be empty")
    if len(team.name.strip()) < 3:
        errors.append("Team name must be at least 3 characters long")
    # Captain handle
    if not team.captain_handle or team.captain_handle.strip() == "":
        errors.append("Team captain handle may not be empty")
    # Logo
    if not team.logo or team.logo.strip() == "":
        errors.append("Team logo may not be empty")
    # Players 3-5
    if team.players is None:
        errors.append("Team must have players")
    else:
        player_count = len(team.players)
        if player_count < 3 or player_count > 5:
            errors.append("Team must have between 3 and 5 players")
    # Points
    if team.points is None:
        errors.append("Points may not be empty")
    elif team.points < 0:
        errors.append("Points may not be negative")

    if errors:
        raise ValidationError(errors)

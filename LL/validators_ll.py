from Models.models import Player, TeamCaptain, Team
import ValidationError
from IO.api_data import APIDATA


def validate_player(player: Player) -> None:
    errors = []

    # Name
    if not player.name or player.name.strip() == "":
        errors.append("Name can not be empty")
    elif any(char.isdigit() for char in player.name):
        errors.append("Name can not have numbers")

    # Date of birth
    try:
        datetime.strptime(player.date_of_birth, "%Y-%M-%D")
    except ValueError:
        errors.append("Date of birth should be written YYYY-MM-DD")

    # Address
    if not player.address or player.address.strip() == "":
        errors.append("Address cannot be empty")
    elif player.address.replace(" ","").isdigit():
        errors.append("Address cannot be only numbers")

    # Phone number
    if not player.phone_number.isdigit():
        errors.append("Phone number must only be numbers.")
    elif len(player.phone_number) != 7:
        errors.append("Phone number should only be 7 numbers")

    # Email
    email = player.email.strip()

    if email == "":
        errors.append("Email can not be empty")

    elif email.count("@") != 1:
        errors.append("Email has to include one '@'")

    elif "." not in email:
        errors.append("email needs to have 1 '.'")


    # Social media

    if player.social_media is None or player.social_media.strip() == "":
        pass 

    # Handle


    # Team name

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

def validate_team_name(name:str) -> None:
    # Name
    if not name or name.strip() == "":
        raise ValueError("You must enter a team name")
    if len(name) > 64:
        raise ValueError("Team name can't be longer than 64 characters")

def validation_team_handle(handle:str) -> None:
    # Captain handle

    if not handle or handle.strip() == "":
        raise ValueError("You must enter a team captain handle ")
    
    current_players = self.APIDATA.get_all_player_data()
    # Checking if player handle is available
    for p in current_players:
        if p.handle == handle:
            raise ValueError("No player exists with that handle")
    

def validate_team_logo(logo:str) -> None:
    # Logo
    if not logo or logo.strip() == "":
        raise ValueError("Team logo may not be empty")

def validate_team_social_media(social_media:str) -> None:
    # Social media
    if social_media is None or social_media.strip() == "":
        pass

def validate_team_players(players:list[str]) -> None:
    pass

def validate_team_points(points:int) -> None:
      # Points
    if points is None:
        raise ValueError("Points may not be empty")
    elif points < 0:
        raise ValueError("Points can't be negative")
from Models.models import Player, TeamCaptain, Team
from datetime import datetime, date
from IO.api_data import APIDATA

class ValidationError(Exception):
    pass


def validate_player_name(name: str):
    "0123456789"
    if name == "Steinar":
        return name
    else:
        raise ValidationError("Name must be Steinar")


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

def validation_team_handle(handle:str, api_data:APIDATA) -> None:
    # Captain handle

    if not handle or handle.strip() == "":
        raise ValueError("You must enter a team captain handle ")
    
    current_players = api_data.get_all_player_data()
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
        raise ValueError("Points may not be negative")

    # Players 3-5
    # if team.players is None:
    #    errors.append("Team must have players")


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
        start_date_iso = datetime.fromisoformat(start_date)
    except ValueError:
        raise ValidationError("Not correct format")
    if start_date_iso <= date.today():
        raise ValidationError("Invalid start date")
    return start_date


def validate_tournament_end_date(start_date, end_date):
    # Verður að vera rétt format.
    # Verður að byrja eftir start date
    try:
        end_date_iso = datetime.fromisoformat(end_date)
    except ValueError:
        raise ValidationError("Not correct format")
    if end_date_iso < datetime.fromisoformat(start_date):
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

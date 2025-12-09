from Models.models import Player, TeamCaptain, Team
import ValidationError


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


def validate_team_name(name:str) -> None:
    # Name
    if not name or name.strip() == "":
        raise ValueError("You must enter a team name")
    elif any(char.isdigit() for char in name):
        raise ValueError("Name can only contain letters")

    #if len(name.strip()) < 3:
    #    errors.append("Team name must be at least 3 characters long")


def validation_team_handle(handle:str) -> None:
    # Captain handle
    if not handle or handle.strip() == "":
        raise ValueError("You must enter a team captain handle ")


def validate_team_logo(logo:str) -> None:
    # Logo
    if not logo or logo.strip() == "":
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
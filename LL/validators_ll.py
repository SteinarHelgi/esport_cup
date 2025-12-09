from Models.models import Player, TeamCaptain, Team
import ValidationError


def validate_player(player: Player) -> None:
    errors = []

    # Name
    if not player.name or player.name.strip() == "":
        errors.append("Nafn má ekki vera tómt")
    elif any(char.isdigit() for char in player.name):
        errors.append("Nafn má ekki innihalda tölustafi")

    # Date of birth


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
    # Captain handle
    if not team.captain_handle or team.captain_handle.strip() == "":
        errors.append("Team captain handle may not be empty")
    # Logo
    if not team.logo or team.logo.strip() == "":
        errors.append("Team logo may not be empty")
    # Players 3-5
    #if team.players is None:
    #    errors.append("Team must have players")
    #else:
    #    player_count = len(team.players)
    #    if player_count < 3 or player_count > 5:
    #        errors.append("Team must have between 3 and 5 players")
    # Points
    if team.points is None:
        errors.append("Points may not be empty")
    elif team.points < 0:
        errors.append("Points may not be negative")

    if errors:
        raise ValidationError(errors)


def validate_tournament(tournament: Tournament) -> None:
    errors: list[str] = []
    # Name
    if not tournament.name or tournament.name.strip() == "":
        errors.append("Tournament name may not be empty")
    # Date
    #
    if not tournament.start_date < tournament.end_date:
        errors.append("Start date must be before end date")
    # venue
    if not tournament.venue or tournament.venue.strip() == "":
        errors.append("Venue may not be empty")
    # number of servers
    if not tournament.no_servers or tournament.no_servers.strip() == "":
        errors.append("Number of servers may not be empty")
    elif not tournament.no_servers.isdigit() or int(tournament.no_servers) <= 0:
        errors.append("Number of servers must be a positive integer")
    # contact_person
    if not tournament.contact_person or tournament.contact_person.strip() == "":
        errors.append("Contact person may not be empty")
    
    if errors:
        raise ValidationError(errors)
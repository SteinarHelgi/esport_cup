from Models import team_captain
from Models.player import Player
from Models.team_captain import TeamCaptain
from Models.team import Team

class ValidationError(Exception):
    def __init__(self, errors: list[str]) -> None:
        self.errors = errors
        super().__init__("\n".join(errors))
    
    def validate_player(player: Player) -> None:
        errors = []

        # Name
        if not player.name or player.name.strip() == "":
            errors.append("Nafn má ekki vera tómt")
        elif any(char.isdigit() for char in player.name):
            errors.append("Nafn má ekki innihalda tölustafi")
    
        # Date of birth

    def validate_team_captain(team_captain:TeamCaptain) -> None:
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

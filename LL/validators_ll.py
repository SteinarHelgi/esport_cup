from Models.player import Player

def validate_player(player: Player) -> None:
    errors = []

    # Name
    if not player.name or player.name.strip() == "":
        errors.append("Nafn má ekki vera tómt")
    elif any(char.isdigit() for char in player.name):
        errors.append("Nafn má ekki innihalda tölustafi")
    
    # Date of birth

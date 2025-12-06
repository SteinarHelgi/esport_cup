from IO.api_data import APIDATA
from LL.organiser_ll import OrganiserLL
from Models.contact_person import ContactPerson
from Models.player import Player
from Models.team_captain import TeamCaptain
from Models.organiser import Organiser
from LL.team_captain_ll import TeamCaptainLL


new_captain = TeamCaptain("1", "boss", "pass", "1", "theboss")

new_player = Player(
    "þröstur",
    "12/11/78",
    "mosarimi 5",
    "844-0110",
    "throstur78@gmail.com",
    "wwww.facebook.com",
    "þrölli",
    "dusty",
)

player_to_modify = Player(
    "Þröstur",
    "2005-03-29",
    "Fizzgata 3 Reykjavik",
    "+3546110048",
    "sif.canary@example.com",
    "https://twitter.com/StackCanarySif",
    "StackCanarySif",
    "Pepsi Max Overflow",
)

player_id = "P042"
player_to_modify.set_id(player_id)


new_organiser = Organiser(1, "robbi", "12345")
api_data = APIDATA()
organiser = OrganiserLL(api_data)
teamcaptain = TeamCaptainLL(api_data)

teamcaptain.modify_player(player_to_modify)

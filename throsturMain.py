from IO.api_data import APIDATA
from LL.organiser_ll import OrganiserLL
from Models.contact_person import ContactPerson
from Models.player import Player
from Models.team_captain import TeamCaptain
from Models.organiser import Organiser
from LL.team_captain_ll import TeamCaptainLL


new_captain = TeamCaptain("1",
                      "boss",
                      "pass",
                      "1",
                      "theboss")

new_player = Player("þröstur",
                12/11/78,
                "mosarimi 5",
                "844-0110",
                "throstur78@gmail.com",
                "wwww.facebook.com",
                "þrölli",
                "dusty")

new_organiser = Organiser("1", "robbi", "12345")

api_data = APIDATA()
organiser = OrganiserLL(api_data)
teamcaptain = TeamCaptainLL(APIDATA)

organiser.register_match_result("1", 99, 98, True)

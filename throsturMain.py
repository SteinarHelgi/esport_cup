from IO.api_data import APIDATA
from LL.organiser_ll import OrganiserLL
from Models.contact_person import ContactPerson
from Models.player import Player
from Models.team_captain import TeamCaptain
from LL.team_captain_ll import TeamCaptainLL


captain = TeamCaptain("1",
                      "boss",
                      "pass",
                      "1",
                      "theboss")

player = Player("þröstur",
                12/11/78,
                "mosarimi 5",
                "844-0110",
                "throstur78@gmail.com",
                "wwww.facebook.com",
                "þrölli",
                "dusty")

api_data = APIDATA()
organiser = OrganiserLL(api_data)
teamcaptain = TeamCaptainLL(APIDATA, captain)



new_player = teamcaptain.create_player(player)





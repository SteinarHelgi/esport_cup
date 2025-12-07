from IO.api_data import APIDATA
from LL.organiser_ll import OrganiserLL
from Models.contact_person import ContactPerson
from Models.player import Player
from Models.team_captain import TeamCaptain
from Models.organiser import Organiser
from Models.team import Team
from Models.match import Match
from LL.team_captain_ll import TeamCaptainLL

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


team = Team(
    "Viking Lite",
    "1",
    "https://example.com/pepsimax_overflow",
    "ASCII_OVERFLOWING_CAN"
)

match_to_add = Match(
    "1",
    "Final",
    "RaceCondition Racers",
    "Chuck Norris Fan Club",
    "2025-12-07",
    "13:00",
    "1"
)

new_organiser = Organiser(1, "robbi", "12345")
api_data = APIDATA()
organiser = OrganiserLL(api_data)
teamcaptain = TeamCaptainLL(api_data)
new_captain = TeamCaptain("1", "boss", "pass", "1", "theboss")

organiser.get_player_stats()

#organiser.give_club_points("KR", 5)
#organiser.give_team_points("Viking Lite", 4)
#organiser.give_player_points("DanglingPtrDan", 3)
#teams = teamcaptain.get_all_teams_in_a_club("1")
#for team in teams:
#    print(team.name)
#teamcaptain.add_team_to_club(team, "1")
#organiser.create_match(match_to_add)
#teamcaptain.modify_team_data(team_to_modify)
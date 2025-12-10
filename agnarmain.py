from datetime import datetime
from LL.api_ll import APILL
from Models.models import Match, Tournament
from IO.api_data import APIDATA
from LL.organiser_ll import OrganiserLL
from Models.contact_person import ContactPerson
from LL.validators_ll import Errors, validate_match_creation
from UI.menu_manager import MenuManager

api_data = APIDATA()
api_ll = APILL()
organiser = OrganiserLL(api_data)
menu_manager = MenuManager(api_ll)


tournament1 = menu_manager.api_ll.get_tournament_by_name("RU Open")
tournament = Tournament("12",datetime.fromisoformat("2025-12-12"),datetime.fromisoformat("2025-12-24"),"Paris","Valorant","8","Hilmir")
match = Match("2", "R16", "SegFault Spartans", "NullPointer Ninjas","2026-01-06","10:00")
if tournament1:

    valid_match = validate_match_creation(match,tournament1,api_data)

    if valid_match == Errors.INVALID_SERVER_COUNT:
        print("INVALID SERVER COUNT")
    if valid_match == Errors.TEAM_ALREADY_IN_SLOT:
        print("TEAM ALREADY IN SLOT")
    if valid_match == Errors.TEAM_ALREADY_IN_ROUND:
        print("TEAM ALREADY IN ROUND")
    if valid_match == Errors.TIMESLOT_FULL:
        print("TIME SLOT FULL")
    if valid_match == Errors.TEAM_LOST_LAST_ROUND:
        print("TEAM LOST LAST ROUND")
    if valid_match == Errors.OK:
        print("OK")
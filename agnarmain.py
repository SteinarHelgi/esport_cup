from datetime import datetime
from LL.api_ll import APILL
from Models.models import Match, Tournament
from IO.api_data import APIDATA
from Models.contact_person import ContactPerson
from LL.validators_ll import Errors, validate_match_creation
from UI.menu_manager import MenuManager

api_data = APIDATA()
api_ll = APILL()
menu_manager = MenuManager(api_ll)

from IO.api_data import APIDATA
from LL.organiser_ll import OrganiserLL
from Models.contact_person import ContactPerson

api_data = APIDATA()
organiser = OrganiserLL(api_data)

raw_cp = ContactPerson(
    id=0,                       # dummy, verður yfirskrifað
    name="Ragnar Ragnarsson",
    email="ragnar@example.com",
    phone="555-1234",
    tournament_id=1,
)

cp = organiser.create_contact_person(raw_cp)
print(cp.id, cp.name, cp.email, cp.phone, cp.tournament_id)

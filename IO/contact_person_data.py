#Þröstur
import csv
from Models.models import ContactPerson

class ContactPersonData:
    def __init__(self):
        self.contact_person_filepath = "Data/ContactPerson.csv"


    def get_contact_person_data(self) -> ContactPerson:
        contact_persons = []
        with open(self.contact_person_filepath, "+r") as file:
            csvReader = csv.reader(file)
            next(csvReader)
            for line in csvReader:
                id = int(line[0])
                name = line[1]
                email = line[2]
                phone = line[3]
                tournament_id = int(line[4])

                contact_person = ContactPerson(
                    id,
                    name,
                    email,
                    phone,
                    tournament_id
                )
                contact_persons.append(contact_person) 
        return contact_persons

    #Setja þetta í logic layer - Sigrún/Agnar
    def get_contact_person_by_id(self, id: int) -> ContactPerson:
        contact_persons = self.get_contact_person_data()
        for contact in contact_persons:
            try:
                if contact.id == id:
                    return contact
            except:
                return None
        

    def store_contact_person_data(self, contact_person: ContactPerson):
        with open(self.contact_person_filepath, "a") as file:
            csvWriter = csv.writer(file)
            try:
                csvWriter.writerow(contact_person.toCSVList())
            except:
                return None
        return contact_person
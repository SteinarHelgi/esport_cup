# Þröstur
import csv
from Models.models import ContactPerson


class ContactPersonData:
    def __init__(self):
        self._filepath: str = "Data/contact_person.csv"

    def get_all_contact_person_data(self) -> list[ContactPerson]:
        contact_persons: list[ContactPerson] = []
        with open(self._filepath, "+r", encoding="utf-8") as file:
            csvReader = csv.reader(file)
            next(csvReader)
            for line in csvReader:
                id: str = line[0]
                name: str = line[1]
                email: str = line[2]
                phone: str = line[3]
                tournament_id: str = line[4]

                contact_person: ContactPerson = ContactPerson(
                    id, name, email, phone, tournament_id
                )
                contact_persons.append(contact_person)
        return contact_persons

    def store_contact_person_data(
        self, contact_person: ContactPerson
    ) -> ContactPerson | None:
        with open(self._filepath, "a") as file:
            csvWriter = csv.writer(file)
            try:
                csvWriter.writerow(contact_person.toCSVList())
            except:
                return None
        return contact_person
import csv
from Models.models import ContactPerson


class ContactPersonData:
    def __init__(self):
        self._filepath: str = "Data/contact_person.csv"

    def get_all_contact_person_data(self) -> list[ContactPerson]:
        """Returns a list of all contact persons stored in the CSV file."""

        contact_persons: list[ContactPerson] = []

        # open the file in read mode
        with open(self._filepath, "+r", encoding="utf-8") as file:
            csvReader = csv.reader(file)

            # Skip header row if present
            next(csvReader, None)

            # Read each remaining line and create ContactPerson objects
            for line in csvReader:
                if not line:
                    continue  # Skip empty lines if any

                id: str = line[0]
                name: str = line[1]
                email: str = line[2]
                phone: str = line[3]
                tournament_id: str = line[4]

                contact_person: ContactPerson = ContactPerson(
                    name, email, phone, tournament_id
                )
                contact_person.set_id(id)
                contact_persons.append(contact_person)

        return contact_persons

    def store_contact_person_data(
        self, contact_person: ContactPerson
    ) -> ContactPerson | None:
        """Appends a single contact person to the CSV file. Returns the contact person if successful, otherwise None."""
        with open(self._filepath, "a") as file:
            csvWriter = csv.writer(file)
            try:
                csvWriter.writerow(contact_person.toCSVList())
            except (OSError, csv.Error):
                return None
        return contact_person

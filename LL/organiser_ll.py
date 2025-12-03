from IO.contact_person_data import ContactPerson

class OrganiserLL:
    def __init__(self):
        self.id = 0

    def create_tournament(self):
        # TODO
        pass

    def delete_tournament(self):
        # TODO
        pass

    def create_schedule(self):
        # TODO
        pass

    def create_match(self):
        # TODO
        pass

    def register_result(self):
        # TODO
        pass
    
    def get_contact_person_by_id(self, id: int) -> ContactPerson:
        contact_persons = self.get_contact_person_data()
        for contact in contact_persons:
            try:
                if contact.id == id:
                    return contact
            except:
                return None
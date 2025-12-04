from Models.models import Tournament


class ContactPerson:
    def __init__(self, id: str, name: str, email: str, phone: str, tournament_id: str):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.tournament_id = tournament_id

    def toCSVList(self):
        ret = []
        ret.append(self.id)
        ret.append(self.name)
        ret.append(self.email)
        ret.append(self.phone)
        ret.append(self.tournament_id)
        return ret

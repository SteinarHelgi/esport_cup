from Models.models import Tournament


class ContactPerson:
    def __init__(
        self, id: int, name: str, email: str, phone: str, tournament: Tournament
    ):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.tournament = tournament

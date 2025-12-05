import datetime as dt

from Models.match import Match


class Tournament:
    def __init__(
        self,
        name: str,
        start_date: dt.datetime,
        end_date: dt.datetime,
        venue: str,
        game_id: str,
        no_servers: str,
        contact_person_name: str,
    ):
        self.id: str = "0"
        self.start_date = start_date
        self.end_date = end_date
        self.name = name
        self.venue = venue
        self.game_id = game_id
        self.no_servers = no_servers
        self.contact_person = contact_person_name
        self.matches = []

    def toCSVList(self):
        ret = []
        ret.append(self.id)
        ret.append(self.name)
        ret.append(self.start_date)
        ret.append(self.end_date)
        ret.append(self.venue)
        ret.append(self.game_id)
        ret.append(self.no_servers)
        ret.append(self.contact_person)
        return ret

    def set_id(self, id):
        self.id = id

    def add_match(self, match: Match):
        self.matches.append(match)

    def __str__(self) -> str:
        return f"{self.name} : {self.venue}"

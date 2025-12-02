import datetime as dt

from Models.models import ContactPerson, Game


class Tournament:
    def __init__(
        self,
        id: int,
        start_date: dt.datetime,
        end_date: dt.datetime,
        name: str,
        venue: str,
        games: list[Game],
        no_servers: int,
        contact_person: ContactPerson,
    ):
        self.id = id
        self.start_date = start_date
        self.end_date = end_date
        self.name = name
        self.venue = venue
        self.games = games
        self.no_servers = no_servers
        self.contact_person = contact_person

    def toCSVList(self):
        ret = []
        ret.append(self.id)
        ret.append(self.start_date)
        ret.append(self.end_date)
        ret.append(self.name)
        ret.append(self.venue)
        ret.append(self.games)
        ret.append(self.no_servers)
        ret.append(self.contact_person)
        return ret

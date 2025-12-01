import datetime as dt

from contact_person import ContactPerson
from game import Game

class Tournament:

    def __init__(self, id: int, start_date: dt, end_date: dt, name: str, venue: str, games: list[Game], no_servers: int, contact_person: ContactPerson):
        self.id = id
        self.start_date = start_date
        self.end_date = end_date
        self.name = name
        self.venue = venue
        self.games = games
        self.no_servers = no_servers
        self.contact_person_id = ContactPerson


 
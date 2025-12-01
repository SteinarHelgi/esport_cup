from team import Team

class TeamCaptain():
    def __init__(self, username: str, password: str, id: int, team: Team, name: str):
        self.username = username
        self.password = password
        self.id = id
        self.team = team
        self.name = name

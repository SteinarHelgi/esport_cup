class TeamCaptain:
    def __init__(self, id: str, username: str, password: str, team_id: str, name: str):
        self.id = id
        self.username = username
        self.password = password
        self.team_id = team_id
        self.name = name
        self.tournaments = []
        self.available_tournaments = []

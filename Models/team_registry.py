class TeamRegistry:
    def __init__(self, team_id: str, tournament_id: str, team_name: str, tournament_name: str):
        self.team_id = team_id
        self.tournament_id = tournament_id
        self.team_name = team_name
        self.tournament_name = tournament_name
    
    def toCSVList(self):
        ret = []
        ret.append(self.team_id)
        ret.append(self.tournament_id)
        ret.append(self.team_name)
        ret.append(self.tournament_name)
        return ret

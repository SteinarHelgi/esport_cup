class TeamRegistry:
    def __init__(self, team_id: str, tournament_id: str):
        self.team_id = team_id
        self.tournament_id = tournament_id
    
    def toCSVList(self):
        ret = []
        ret.append(self.team_id)
        ret.append(self.tournament_id)
        return ret

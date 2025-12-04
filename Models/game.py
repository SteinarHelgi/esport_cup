# Þröstur
class Game:
    def __init__(self, game_id: str, name: str, duration: str):
        self.id: str = game_id
        self.name: str = name
        self.duration: str = duration

    def toCSVList(self):
        ret: list[str] = []
        ret.append(self.id)
        ret.append(self.name)
        ret.append(self.duration)
        return ret


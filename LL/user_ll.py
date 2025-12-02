class UserLL:
    def __init__(self, api_data):
        self.id = 0
        self.api_data = api_data

    def get_all_teams(self):
        teams = ""
        return teams

    def get_all_tournaments(self) -> dict:
        tournaments = self.api_data.get_all_tournaments()
        return tournaments

    def get_players(self):
        #TODO
        pass

    def get_ongoing_tournament(self):
        #TODO
        pass

    def get_past_tournament(self):
        #TODO
        pass

    def get_upcoming_tournament(self):
        #TODO
        pass

    def show_schedule(self):
        #TODO
        pass

    def get_statistics(self):
        #TODO
        pass
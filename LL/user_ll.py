from datetime import datetime

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
        # TODO
        pass

    def get_ongoing_tournament(self, today):
        tournament = self.api_data.get_all_tournaments()
        ongoing = []

        for t in tournament:
            if t.start_date <= today <= t.end_date:
                ongoing.append(t)

        return ongoing
        

    def get_past_tournament(self, today): 
        tournament = self.api_data.get_all_tournaments()
        past = []

        for t in tournament:
            if t.end_date < today:
                past.append(t)

        return past

    def get_upcoming_tournament(self, today):
        tournament = self.api_data.get_all_tournaments()
        upcoming = []

        for t in tournament:
            if t.end_date > today:
                upcoming.append(t)
        
        return upcoming

    def show_schedule(self):
        # TODO
        pass

    def get_statistics(self):
        # TODO
        pass
    
    def get_all_clubs(self):
        clubs = self.api_data.get_all_clubs()
        return clubs

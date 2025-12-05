from datetime import datetime
from IO.api_data import APIDATA
from Models.team import Team


class UserLL:
    def __init__(self, api_data: APIDATA):
        self.id = 0
        self.api_data = api_data

    def get_all_teams(self) -> list[Team]:
        teams = self.api_data.get_all_team_data()
        players = self.api_data.get_all_player_data()
        for team in teams:
            for player in players:
                if player.team_name == team.name:
                    team.add_player(player.handle)
        return teams

    def get_all_tournaments(self) -> list:
        tournaments = self.api_data.get_all_tournament_data()
        return tournaments

    def get_all_players(self) -> list:
        players = self.api_data.get_all_player_data()
        return players

    def get_ongoing_tournament(self, today):
        tournament = self.api_data.get_all_tournament_data()
        ongoing = []

        for t in tournament:
            if t.start_date <= today <= t.end_date:
                ongoing.append(t)

        return ongoing

    def get_past_tournament(self, today):
        tournament = self.api_data.get_all_tournament_data()
        past = []

        for t in tournament:
            if t.end_date < today:
                past.append(t)

        return past

    def get_upcoming_tournament(self, today):
        tournament = self.api_data.get_all_tournament_data()
        upcoming = []

        for t in tournament:
            if t.end_date > today:  # kíkja á
                upcoming.append(t)

        return upcoming

    # TODO
    # def show_schedule(self):
    #     schedule = self.api_data.get_schedule_info()
    #     return schedule

    def get_statistics(self):
        # TODO
        pass

    # TODO
    # def get_all_clubs(self):
    #     clubs = self.api_data.get_all_clubs()
    #     return clubs

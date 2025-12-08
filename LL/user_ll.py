from datetime import date, datetime
from IO.api_data import APIDATA
from Models.team import Team
from Models.tournament import Tournament
from Models.match import Match
from Models.player import Player
from Models.club_stat import ClubStat
from Models.elimination_stat import EliminationStat
from Models.player_stat import PlayerStat
#import matplotlib.pyplot as plt
from typing import Union

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
        matches = self.api_data.get_all_match_data()
        for tournament in tournaments:
            for match in matches:
                if match.tournament_id == tournament.id:
                    tournament.add_match(match)
        return tournaments

    def get_all_players(self) -> list:
        players = self.api_data.get_all_player_data()
        return players

    def get_ongoing_tournament(self):
        today = datetime.today()
        tournament = self.api_data.get_all_tournament_data()
        ongoing = []

        for t in tournament:
            if t.start_date <= today <= t.end_date:
                ongoing.append(t)

        return ongoing

    def get_past_tournament(self):
        tournament = self.api_data.get_all_tournament_data()
        today = datetime.today()
        past = []

        for t in tournament:
            if t.end_date < today:
                past.append(t)

        return past

    def get_upcoming_tournament(self):
        tournament = self.api_data.get_all_tournament_data()
        upcoming = []
        today = datetime.today()

        for t in tournament:
            if t.end_date > today:  # kíkja á
                upcoming.append(t)

        return upcoming

    def show_player_stats_bar_chart(self):
        """Retrieves player points and shows a bar chart of the top players"""
        players = self.api_data.get_all_player_data()
        stats: list[list[Union[int, str]]] = []
        for player in players:
            results: list[Union[int, str]] = []
            results = [player.points, player.handle]
            stats.append(results)
        #Sort the results by points - highest is first.
        sorted_results = sorted(stats, key=lambda item: item[0], reverse = True)
        
        #Going to show this many players in our bar chart
        number_of_players_to_display = 5
        #creating the value and keys for the bar chart 
        handle: list[str] = []
        points: list[int] = []
        for i in range(number_of_players_to_display):
            handle.append(sorted_results[i][1])
            points.append(sorted_results[i][0])
        plt.bar(handle, points)
        plt.show()

    def get_elimination_stats(self, tournament_id):
        matches = self.api_data.get_all_match_data()
        team_registry = self.api_data.get_all_team_registry_data()
        teams = self.api_data.get_all_team_data()
        stats: list[EliminationStat] = []
        for registry in team_registry:
            if registry.tournament_id == tournament_id:
                stat = EliminationStat(registry.team_name)
                for match in matches:
                    if match.completed == "TRUE":
                        if match.team_a_name == stat.team_name:
                            stat.games_played += 1
                            stat.score_for += int(match.score_a)
                            stat.score_against += int(match.score_b)
                        if match.team_b_name == stat.team_name:
                            stat.games_played += 1
                            stat.score_for += int(match.score_b)
                            stat.score_against += int(match.score_a)
                        if match.winner_team_name == stat.team_name:
                            stat.won += 1
                stat.lost = stat.games_played - stat.won
                if stat.games_played == 0:
                    stat.winning_ratio = 0
                else:
                    stat.winning_ratio = stat.won/stat.games_played * 100
                for team in teams:
                    if team.name == registry.team_name:
                        stat.points = team.points
                        break
                stats.append(stat)
            
        sorted_by_winning_ratio = sorted(stats, key=lambda s: s.winning_ratio, reverse = True)
        
        return sorted_by_winning_ratio

    def get_all_player_stat(self, tournament_id) -> list[PlayerStat]:
        all_player_stats: list[PlayerStat] = []
        matches: list[Match] = self.api_data.get_all_match_data()
        players: list[Player] = self.api_data.get_all_player_data()
        elimination_stat: list[EliminationStat] = self.get_elimination_stats(tournament_id)
        for player in players:
            team_name = player.team_name
            player_stat: PlayerStat = PlayerStat(player.handle)
            player_stat.points = player.points
            for stat in elimination_stat:
                if stat.team_name == team_name:
                    player_stat.games_played = int(stat.games_played)
                    player_stat.won = int(stat.won)
                    player_stat.lost = int(stat.lost)
                    player_stat.winning_ratio = float(stat.winning_ratio)
            all_player_stats.append(player_stat)
        return all_player_stats
    
    def get_player_stat(self, player_handle, tournament_id) -> PlayerStat | None:
        all_player_stat = self.get_all_player_stat(tournament_id)
        for player_stat in all_player_stat:
            if player_stat.player_handle == player_handle:
                return player_stat
        return None
    
    def get_all_club_stat(self)->list[ClubStat]:
        all_clubs_stat: list[ClubStat] = []
        clubs: list[Club] = self.get_all_club_data()
        #eliminations_stat = TODO Sækja hér elimination data úr organiser_ll klasanum.
        for club in clubs:
            new_club = ClubStat(club.name)
            teams_in_club = self.get_all_teams_in_a_club(club.id)
            for team in teams_in_club:
                pass



        return all_clubs_stat

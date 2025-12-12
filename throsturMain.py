from IO.api_data import APIDATA
from Models import team_captain
from Models.contact_person import ContactPerson
from Models.player import Player
from Models.team_captain import TeamCaptain
from Models.organiser import Organiser
from Models.team import Team
from Models.match import Match
from LL.tournament_ll import TournamentLL
from LL.main_ll import MainLL

new_player = Player(
    "þröstur",
    "12/11/78",
    "mosarimi 5",
    "844-0110",
    "throstur78@gmail.com",
    "wwww.facebook.com",
    "þrölli",
    "dusty",
)

player_to_modify = Player(
    "Þröstur",
    "2005-03-29",
    "Fizzgata 3 Reykjavik",
    "+3546110048",
    "sif.canary@example.com",
    "https://twitter.com/StackCanarySif",
    "StackCanarySif",
    "Pepsi Max Overflow",
)


team = Team(
    "Viking Lite",
    "1",
    "https://example.com/pepsimax_overflow",
    "ASCII_OVERFLOWING_CAN"
)

match_to_add = Match(
    "1",
    "Final",
    "RaceCondition Racers",
    "Chuck Norris Fan Club",
    "2025-12-07",
    "13:00",
)

new_organiser = Organiser(1, "robbi", "12345")
api_data = APIDATA()
main = MainLL(api_data)
tournament = TournamentLL(api_data,main)
tournament.setup_R16_qualifying_matches("1")
#user = UserLL(api_data)
#teamcaptain = TeamCaptainLL(api_data)
#new_captain = TeamCaptain("1", "boss", "pass", "1", "theboss")



#team_captain.get_all_club_stat()
#organiser.get_club_stat("KR")



#stat = organiser.get_player_stat("SegFaultSam", "1")
#player_stat = organiser.get_all_player_stat("1")
#for stat in player_stat:
#    print(stat.player_handle, stat.winning_ratio, stat.points)

#stats = organiser.get_elimination_stats("1")
#for stat in stats:
#    print(stat.team_name, stat.games_played, stat.won, stat.lost, stat.score_for, stat.score_against, stat.winning_ratio, stat.points)

#user.show_player_stats_bar_chart()
#organiser.give_club_points("KR", 5)
#organiser.give_team_points("Viking Lite", 4)
#organiser.give_player_points("DanglingPtrDan", 3)
#teams = teamcaptain.get_all_teams_in_a_club("2")
#teamcaptain.add_team_to_club(team, "1")
#organiser.create_match(match_to_add)
#teamcaptain.modify_team_data(team_to_modify)






#---------------------------
#Nöfn á functions

#organiser.get_player_stat("SegFaultSam", "1")
#organiser.get_all_player_stat("1")
#organiser.get_elimination_stats("1")
#organiser.show_player_stats_bar_chart()
#organiser.give_club_points("KR", 5)
#organiser.give_team_points("Viking Lite", 4)
#organiser.give_player_points("DanglingPtrDan", 3)
#teamcaptain.get_all_teams_in_a_club("2")
#teamcaptain.add_team_to_club(team, "1")
#organiser.create_match(match_to_add)
#teamcaptain.modify_team_data(team_to_modify)

"""class PlayerStat:
    def __init__(
            self,
            player_handle: str
    ) -> None:
            self.player_handle = player_handle
            self.points: int = 0
            self.games_played: int = 0
            self.won: int = 0
            self.lost: int = 0
            self.winning_ratio: float = 0

class EliminationStat:
    def __init__(
            self,
            team_name: str
    ) -> None:
            self.team_name = team_name
            self.games_played: int = 0
            self.won: int = 0
            self.lost: int = 0
            self.score_for: int = 0
            self.score_against: int = 0
            self.difference: int = 0
            self.winning_ratio: float = 0
            self.points: int = 0

class ClubStat:
    def __init__(
            self,
            club_name: str
    ) -> None:
            self.club_name = club_name
            self.games_played: int = 0
            self.won: int = 0
            self.lost: int = 0
            self.winning_ratio: float = 0
            self.points: int = 0"""


    # def show_player_stats_bar_chart(self):
    #    return self.userLL.show_player_stats_bar_chart()

    # def get_elimination_stats(self, tournament_id):
    #    return self.userLL.get_elimination_stats(tournament_id)

    # def get_all_player_stat(self, tournament_id) -> list[PlayerStat]:
    #    return self.userLL.get_all_player_stat(tournament_id)

    # def get_player_stat(self, player_handle, tournament_id) -> PlayerStat | None:
    #    return self.userLL.get_player_stat(player_handle, tournament_id)

        # def get_all_club_stat(self) -> list[ClubStat]:
    #     return self.userLL.get_all_club_stat()

"""   def setup_R16_qualifying_matches(self, tournament_id: str) -> None:
        #Creates R16 qualifying matches for the given tournament.
        team_registry = self.APIDATA.get_all_team_registry_data()
        all_tournaments = self.APIDATA.get_all_tournament_data()
        playing_times: list[str] = ["10:00", "12:00", "14:00", "16:00"]

        start_date: datetime = datetime(year=2000, month=1, day=1)
        for t in all_tournaments:
            if t.id == tournament_id:
                start_date = t.start_date
                break
        # If tournament id was not found - raise valueerror
        if start_date.year == 2000:
            raise ValueError
        next_day = start_date.day + 1
        next_date: datetime = datetime(
            year=start_date.year, month=start_date.month, day=next_day
        )

        dates: list[datetime] = [start_date, next_date]

        teams_playing: list[str] = []
        for registry in team_registry:
            if registry.tournament_id == tournament_id:
                teams_playing.append(registry.team_name)

        # R16 is 8 matches Four matches per day for 2 days
        match_id = 1
        for j in range(2):
            date_of_game = dates[j]
            for i in range(4):
                new_tournament_id: str = tournament_id
                round: str = "R16"
                team_a_name: str = random.choice(teams_playing)
                teams_playing.remove(team_a_name)
                team_b_name: str = random.choice(teams_playing)
                teams_playing.remove(team_b_name)
                time_of_match = playing_times[i]
                new_match = Match(
                    new_tournament_id,
                    round,
                    team_a_name,
                    team_b_name,
                    str(date_of_game),
                    time_of_match,
                )
                new_match.match_id = str(match_id)
                new_match.match_number = str(match_id)
                server_id = "SRV-PEPSI"
                new_match.server_id = server_id
                self.APIDATA.store_match_data(new_match)
                match_id += 1


    def give_club_points(self, club_name: str, points: int) -> None:
        #Adds points to the club with the given name.
        self.APIDATA.give_club_points(club_name, points)

    def give_player_points(self, handle: str, points: int) -> None:
        #Adds points to the player with the given handle.
        self.APIDATA.give_player_points(handle, points)

from Models.models import Match, Tournament


class Schedule:
    def __init__(self, schedule_id: int, matches: list[Match], tournament_id: str):
        self.id = schedule_id
        self.matches = matches
        self.tournament_id = tournament_id """

    # def get_all_club_stat(self) -> list[ClubStat]:
    #     return self.userLL.get_all_club_stat()
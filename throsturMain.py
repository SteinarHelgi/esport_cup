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
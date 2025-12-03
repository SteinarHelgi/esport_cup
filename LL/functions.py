
from Models.player import Player
from Models.team import Team

def format_tournament_table(self, tournaments):
   #Define fixed widths for columns
    w_name = 25
    w_date = 15

    # print header
    print(f"{'NAME':<{w_name}} {'START DATE':<{w_date}} {'END DATE':<{w_date}}")
    
    #Print a divider line
    print("-" * (w_name + w_date + w_date))
    empty_string = ""
    #Loop through the data
    for tournament in tournaments:
        # Clean up the dates
        s_date = str(tournament.start_date).split(" ")[0]
        e_date = str(tournament.end_date).split(" ")[0]

        # Print the actual variables (tournament.name), not the string "NAME"
        empty_string += f"{tournament.name:<{w_name}} {s_date:<{w_date}} {e_date:<{w_date}}\n"
    return empty_string

def format_team_list(self, teams:list[Team]): #TODO add club to this

    #Define fixed widths for columns
    w_name = 30
    w_captain = 25
    #w_club = 15

    # print header
    print(f"{'TEAM NAME':<{w_name}} {'TEAM CAPTAIN':<{w_captain}}")
    
    #Print a divider line
    print("-" * (w_name + w_captain))
    empty_string = ""
    #Loop through the data
    for team in teams:
        # Clean up the dates
        captain_fix = str(team.captain_id).split(" ")[0]
        #e_date = str(tournament.end_date).split(" ")[0]

        # Print the actual variables (tournament.name), not the string "NAME"
        empty_string += f"{team.name:<{w_name}} {captain_fix:<{w_captain}}\n"
    return empty_string

def format_player_list(self, players:list[Player]): #TODO KLÁRA? 
    #Define fixed widths for columns
    w_player_name = 30
    w_player_handle = 25
    #w_club = 15

    # print header
    print(f"{'PLAYER NAME':<{w_player_name}} {'PLAYER HANDLE':<{w_player_handle}}")
    
    #Print a divider line
    print("-" * (w_player_name + w_player_handle))
    empty_string = ""
    #Loop through the data
    for player in players:
        # Clean up the dates
        #captain_fix = str(team.captain_id).split(" ")[0]
        #e_date = str(tournament.end_date).split(" ")[0]

        # Print the actual variables (tournament.name), not the string "NAME"
        empty_string += f"{player.name:<{w_player_name}} {player.handle:<{w_player_handle}}\n"
    return empty_string
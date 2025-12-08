from IO import game_data
from Models.player import Player
from Models.team import Team
from Models.tournament import Tournament


def format_tournament_table(tournaments: list[Tournament]):
    # Define fixed widths for columns
    w_name = 20
    w_date = 12
    w_game = 20
    w_id = 3

    # print header
    print(
        f" {'Id':>{w_id}} {'NAME':<{w_name}} {'START DATE':<{w_date}} {'END DATE':<{w_date}}{'GAME':>{w_game - 3}}"
    )

    # Print a divider line
    line_length = w_id + w_name + w_date + w_date + w_date + (w_game - 5)
    print("-" * line_length)
    empty_string = ""
    divider_Line = "-" * line_length + "\n"
    # Loop through the data
    for counter, tournament in enumerate(tournaments):
        # Clean up the dates
        s_date = str(tournament.start_date).split(" ")[0]
        e_date = str(tournament.end_date).split(" ")[0]

        # Print the actual variables (tournament.name), not the string "NAME"
        empty_string += f"{counter + 1:>{w_id}}.{tournament.name:<{w_name}}{s_date:^{w_date}}|{e_date:^{w_date}}{tournament.game_id:>{w_game}}\n"
        empty_string += divider_Line

    return empty_string


def format_team_list(teams: list[Team]):  # TODO add club to this
    # Define fixed widths for columns
    w_name = 30
    w_captain = 25
    w_counter = 15

    # print header
    print(
        f"{'Id':<{w_counter}}{'TEAM NAME':<{w_name}} {'TEAM CAPTAIN':>{w_captain - 3}}"
    )

    # Print a divider line
    line_length = w_name + w_captain + w_counter
    print("-" * (line_length))
    empty_string = ""
    divider_Line = "-" * line_length + "\n"
    # Loop through the data
    for counter, team in enumerate(teams):
        # Clean up the dates
        captain_fix = str(team.captain_handle).split(" ")[0]
        # e_date = str(tournament.end_date).split(" ")[0]

        # Print the actual variables (tournament.name), not the string "NAME"
        empty_string += f"{counter + 1:<{w_counter}}{team.name:<{w_name}} {captain_fix:>{w_captain - 3}}\n"
        empty_string += divider_Line
    return empty_string


def format_player_list(players: list[Player]):  # TODO KLÁRA?
    # Define fixed widths for columns
    w_player_name = 25
    w_player_handle = 20
    w_counter = 3
    # w_club = 15

    # print header
    print(
        f"{'ID':<{w_counter}} {'PLAYER NAME':<{w_player_name}} {'PLAYER HANDLE':<{w_player_handle}}"
    )

    # Print a divider line
    print("-" * (w_counter + w_player_name + w_player_handle))
    empty_string = ""
    # Loop through the data

    for id, player in enumerate(players):
        # Clean up the dates
        # captain_fix = str(team.captain_id).split(" ")[0]
        # e_date = str(tournament.end_date).split(" ")[0]

        # Print the actual variables (tournament.name), not the string "NAME"

        rank_string = f"{id + 1}."
        empty_string += f"{rank_string:<{w_counter}}{player.name:<{w_player_name}} {player.handle:<{w_player_handle}}\n"
    return empty_string

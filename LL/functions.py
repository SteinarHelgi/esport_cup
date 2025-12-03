
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

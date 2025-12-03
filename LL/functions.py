
def format_tournament_table(self, tournaments):
    # 1. Define fixed widths (integers) for your columns
    w_name = 25
    w_date = 15

    # 2. Print the Header ONCE (outside the loop)
    # We use the widths here to reserve space
    print(f"{'NAME':<{w_name}} {'START DATE':<{w_date}} {'END DATE':<{w_date}}")
    
    # Optional: Print a divider line
    print("-" * (w_name + w_date + w_date))

    # 3. Loop through the data
    for tournament in tournaments:
        # Clean up the dates
        s_date = str(tournament.start_date).split(" ")[0]
        e_date = str(tournament.end_date).split(" ")[0]

        # Print the actual variables (tournament.name), not the string "NAME"
        print(f"{tournament.name:<{w_name}} {s_date:<{w_date}} {e_date:<{w_date}}")

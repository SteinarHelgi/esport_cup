from UI.main_ui import MainUI


def main():
    main_ui = MainUI()
    teams = main_ui.APILL.get_all_teams()
    for team in teams:
        print(team)


main()

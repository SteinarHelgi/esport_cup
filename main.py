from UI.main_ui import MainUI


def main():
    mainUI = MainUI()

    mainUI.showLoginMenu()
    userInput = input()
    while userInput != "q":
        if userInput == "1":
            mainUI.userUI.showTeams()
        if userInput == "2":
            mainUI.userUI.showTournaments()

        mainUI.showLoginMenu()
        userInput = input()


main()

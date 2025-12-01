from UI.user_ui import UserUI


class MainUI:
    def __init__(self):
        self.userUI = UserUI()

    def showLoginMenu(self):
        print("""1. Show Teams\n2. Show Tournaments""")

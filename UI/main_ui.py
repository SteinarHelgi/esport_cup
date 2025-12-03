from UI.menu_manager import MenuManager
from UI.team_captain_ui import TeamCaptainUI
from UI.user_ui import UserUI
from LL.api_ll import APILL


class MainUI:
    def __init__(self):
        self.APILL = APILL()
        self.menu_manager = MenuManager(self.APILL)
        self.current_screen = "LOGIN_MENU"

    def run(self) -> None:
        """Main loop handling navigation"""
        while True:
            func = self.menu_manager.pages.get(self.current_screen)

            if func is None:
                print(f"Unknown screen: {self.current_screen}")
                break

            next_screen = func()

            if next_screen in (None, "QUIT"):
                print("Quitting")
                break

            self.current_screen = next_screen

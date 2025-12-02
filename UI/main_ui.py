from UI.menu_manager import MenuManager
from UI.team_captain_ui import TeamCaptainUI
from UI.user_ui import UserUI
from LL.api_ll import APILL


class MainUI:
    def __init__(self):
        self.APILL = APILL()
        self.userUI = UserUI(self.APILL)
        self.menu_manager = MenuManager(self.APILL)
        self.team_captain_ui = TeamCaptainUI(self.APILL)
        self.current_screen = "LOGIN_MENU"

    def run(self) -> None:
        """Main loop handling navigation."""
        while True:
            if self.current_screen == "LOGIN_MENU":
                action: str = self.menu_manager.print_login_menu()
                if action == "USER_FRONT_PAGE":
                    self.current_screen = "USER_FRONT_PAGE"
                elif action == "ORGANISER_FRONT_PAGE":
                    self.current_screen = "ORGANISER_FRONT_PAGE"
                elif action == "ORGANISER_FRONT_PAGE":
                    self.current_screen = "ORGANISER_FRONT_PAGE"
                elif action == "QUIT":
                    print("Bless!")
                    break

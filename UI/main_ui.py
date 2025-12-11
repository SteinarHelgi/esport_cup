from UI.menu_manager import MenuManager
from LL.api_ll import APILL
import UI.ui_functions as u


class MainUI:
    """Main ui functions are in here"""
    def __init__(self):
        self.APILL = APILL()
        self.menu_manager = MenuManager(self.APILL)
        self.previous_screen = ""
        self.current_screen = "LOGIN_MENU"

    def run(self) -> None:
        """Main loop handling navigation"""

        # 1. PRINT WELCOME SIGN ONCE (Before the loop starts)
        u.clear_terminal()
        u.set_system_color_green()
        print(u.print_welcome_sign())
        u.set_system_color_red()

        # Optional: Pause so the user can actually see the welcome sign
        input("\nPress Enter to start")

        while True:
            func = self.menu_manager.pages.get(self.current_screen)

            if func is None:
                print(f"Unknown screen: {self.current_screen}")
                break

            # 2. PRINT SMALL LOGO ALWAYS (Inside the loop)
            u.clear_terminal()
            u.set_system_color_green()
            print(u.print_logo())
            u.set_system_color_red()

            next_screen = func()

            if next_screen in (None, "QUIT"):
                break

            self.current_screen = next_screen
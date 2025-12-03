from Models.team import Team
from UI.user_ui import UserUI
from UI.main_ui import MainUI


def main():
    user = MainUI()
    user.menu_manager.user_ui.show_players(Team(name ="NullPointer Ninjas"))
    


main()


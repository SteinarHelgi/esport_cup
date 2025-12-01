from UI.team_captain_ui import TeamCaptainUI
from UI.user_ui import UserUI
from LL.api_ll import APILL


class MainUI:
    def __init__(self):
        self.APILL = APILL()
        self.userUI = UserUI(self.APILL)
        self.organiserUI = "organiserUI"
        self.teamCaptainUI = TeamCaptainUI(self.APILL)

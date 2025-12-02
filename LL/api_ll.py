from LL.user_ll import UserLL


class APILL:
    def __init__(self) -> None:
        self.userLL = UserLL()
        self.teamCaptainLL = "teamCaptainLL"
        self.organiserLL = "organiserLL"

    def get_all_teams(self):
        return self.userLL.get_all_teams()

    def get_all_tournaments(self):
        return self.userLL.get_all_tournaments()

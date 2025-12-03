from UI.main_ui import MainUI
from LL.user_ll import UserLL
from datetime import datetime

def main():
    user = MainUI()
    #today = datetime.today()
    today = datetime(2025, 3, 10)
    ongoing = user.APILL.get_upcoming_tournaments(today)

    print("ONGOING TOURNAMENTS:")
    for t in ongoing:
        print(f"- {t.id}: {t.name}  {t.start_date} – {t.end_date}")
main()
class UserLL:
    def __init__(self):
        self.id = 0

    def getAllTeams(self):
        teams = {
            "1": [
                "Astralis",
                ["Faker", "Niko", "Monesy", "skadoodle"],
                "Logo",
                "CAPTAIN",
                "www.url.com",
                "Valur",
                "100",
            ],
            "2": [
                "G2",
                ["Shroud", "Biseps", "Stewie2k"],
                "logo",
                "CAPTAIN",
                "www.url.com",
                "Valur",
                "180",
            ],
            "3": [
                "NIP",
                ["HALL", "s1mple", "Stewie2k"],
                "logo",
                "CAPTAIN",
                "www.url.com",
                "Valur",
                "180",
            ],
        }
        return teams

    def getAllTournaments(self) -> dict:
        tournaments = {
            "1": [
                "Paris major",
                "2025/08/09",
                "2025/08/13",
                "Paris church",
                "valorant",
                "8",
                "Valur reynisson",
            ],
            "2": [
                "Iceland major",
                "2025/10/14",
                "2025/10/20",
                "Laugardagshöll",
                "CS:GO",
                "7",
                "Hilmir",
            ],
        }
        return tournaments

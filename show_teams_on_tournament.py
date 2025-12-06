def show_teams_on_tournament(self, target_tournament_id: str) -> list[str]:

        #Fetch team registry and search for team_id in a specific tournament id
        team_registry = self.api_data.get_all_team_registry_data()
        all_teams_id_in_tournament: list[str] = []
        for registry in team_registry:
            if registry.tournament_id == target_tournament_id:
                all_teams_id_in_tournament.append(registry.team_id)

        #Fetch a list of teams and their id
        all_teams_in_tournament: list[str] = []
        teams: Team = self.api_data.get_all_team_data()
        for team in teams:
            if team.id in all_teams_id_in_tournament:
                all_teams_in_tournament.append(team.name)
        return all_teams_in_tournament



def get_standings(teams):
    sorted_teams = sorted(
        teams,
        key=get_team_ranking)
    return sorted_teams


def get_team_ranking(team):
    goal_difference = team["goals_for"] - team["goals_against"]
    return (
        -team["points"],
        -goal_difference,
        -team["goals_for"],
        team["name"].lower())
    
    

def show_standings(teams):
    if not teams:
        print("No teams registered.")
        return
    sorted_teams = get_standings(teams)
    print("\n========== TOURNAMENT STANDINGS ==========")
    for team in sorted_teams:
        goal_difference = team["goals_for"] - team["goals_against"]

        print(
            team["name"],
            team["played"],
            team["wins"],
            team["draws"],
            team["losses"],
            team["goals_for"],
            team["goals_against"],
            goal_difference,
            team["points"])
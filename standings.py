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
        
        
        
        

def show_leading_team(teams):
    if not teams:
        print("No teams registered.")
        return

    sorted_teams = get_standings(teams)

    if sorted_teams[0]["played"] == 0:
        print("No leading team yet. No matches played.")
        return

    leading_team = sorted_teams[0]

    print("\n========== LEADING TEAM ==========")
    print(f"Team: {leading_team['name']}")
    print(f"Points: {leading_team['points']}")
    print(f"Wins: {leading_team['wins']}")
    print(f"Goal difference: {leading_team['goals_for'] - leading_team['goals_against']}")
    
    
    
def show_best_attacking_team(teams):
    played_teams = []
    for team in teams:
        if team["played"] > 0:
            played_teams.append(team)
    if not played_teams:
        print("No matches played yet.")
        return

    highest_goals = max(team["goals_for"] for team in played_teams)
    print("\n========== BEST ATTACKING TEAM ==========")

    for team in played_teams:
        if team["goals_for"] == highest_goals:
            print(f"{team['name']} - {team['goals_for']} goals") 
            
            

def show_team_success_rate(teams):
    if not teams:
        print("No teams registered.")
        return
    print("\n========== TEAM SUCCESS RATE ==========")
    for team in teams:
        if team["played"] == 0:
            print(f"{team['name']}: No games")
        else:
            success_rate = (team["points"] / (team["played"] * 3)) * 100
            print(f"{team['name']}: {success_rate:.2f}%")



def show_teams_without_wins(teams):
    found_teams = False
    print("\n========== TEAMS WITHOUT WINS ==========")

    for team in teams:
        if team["played"] > 0 and team["wins"] == 0:
            print(f"{team['name']} | Played: {team['played']} | Points: {team['points']}")
            found_teams = True
    if not found_teams:
        print("No teams found.")
        
        
        
def show_tournament_summary(teams, matches):
    total_teams = len(teams)
    total_matches = len(matches)

    total_goals = 0
    draws = 0
    for match in matches:
        total_goals += match["home_goals"] + match["away_goals"]

        if match["home_goals"] == match["away_goals"]:
            draws += 1

    print("\n========== TOURNAMENT SUMMARY ==========")
    print(f"Total teams: {total_teams}")
    print(f"Total matches: {total_matches}")
    print(f"Total goals: {total_goals}")
    print(f"Draws: {draws}")

    if total_matches == 0:
        print("Average goals per match: 0")
        print("Leading team: No matches played yet.")
    else:
        average_goals = total_goals / total_matches
        print(f"Average goals per match: {average_goals:.2f}")

        sorted_teams = get_standings(teams)
        print(f"Leading team: {sorted_teams[0]['name']}")
        
        
def check_championship_potential(teams):
    if not teams:
        print("No teams registered.")
        return
    print("\n========== CHAMPIONSHIP POTENTIAL ==========")

    for team in teams:
        remaining_matches = len(teams) - 1 - team["played"]
        max_points = team["points"] + (remaining_matches * 3)
        can_win = True
        for other_team in teams:
            if other_team["id"] != team["id"]:
                if max_points <= other_team["points"]:
                    can_win = False
                    break
        if can_win:
            print(f"{team['name']}: Can still win (Max points: {max_points})")
        else:
            print(f"{team['name']}: Cannot win (Max points: {max_points})")
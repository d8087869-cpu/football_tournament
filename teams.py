import logging
from validators import validate_team_id, validate_team_name



def add_team(teams, team_id, team_name):
    validate_team_id(team_id, teams)
    validate_team_name(team_name, teams)
    
    new_team = {"id:":team_id,
                "name":team_name.strip(),
                "played":0,
                "wins":0,
                "draws":0,
                "losses":0,
                "goals_for":0,
                "goals_against":0,
                "points":0}
    teams.append(new_team)
    logging.info("team added %s (ID %s)", team_name, team_id)

    return new_team


def show_all_teams(teams):
    if not teams:
        print("no teams to show")
        return
    print("\n============ ALL TEAMS ============")
    print(f"{'ID'}  {'team name'}         {'played'}       {'points'}")
    for team in teams:
        print(
            f"{team["id"]:<5}"
            f"{team['name']:<20}"
            f"{team['played']:<10}"
            f"{team['points']:<10}")
import logging

from validators import validate_match

def add_match(teams, matches, home_team_id, away_team_id,
    home_goals, away_goals):

    validate_match(
        home_team_id,
        away_team_id,
        home_goals,
        away_goals,
        teams,
        matches)

    home_team = None
    away_team = None

    for team in teams:
        if team["id"] == home_team_id:
            home_team = team

        if team["id"] == away_team_id:
            away_team = team

    match = {
        "home_team_id": home_team_id,
        "away_team_id": away_team_id,
        "home_goals": home_goals,
        "away_goals": away_goals}

    matches.append(match)

    update_team_stats(home_team, away_team, home_goals, away_goals)




def update_team_stats(home_team, away_team, home_goals, away_goals):

    home_team["played"] += 1
    away_team["played"] += 1

    home_team["goals_for"] += home_goals
    home_team["goals_against"] += away_goals

    away_team["goals_for"] += away_goals
    away_team["goals_against"] += home_goals

    if home_goals > away_goals:
        home_team["wins"] += 1
        home_team["points"] += 3
        away_team["losses"] += 1

    elif away_goals > home_goals:
        away_team["wins"] += 1
        away_team["points"] += 3
        home_team["losses"] += 1

    else:
        home_team["draws"] += 1
        away_team["draws"] += 1

        home_team["points"] += 1
        away_team["points"] += 1


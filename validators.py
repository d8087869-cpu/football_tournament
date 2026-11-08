def validate_team_id(team_id,teams):
    if team_id <=0:
        raise ValueError("team id must be positve number")
    for team in teams:
        if team["id"] == team_id:
            raise ValueError ("team already exist")
        
def validate_team_name(name, teams):
    if not name.strip():
        raise ValueError ("team name cannot be empty")
    for team in teams:
        if team["name"].lower() == name.strip().lower():
            raise ValueError ("team name exists")


def validate_match(home_team_id, away_team_id, home_goals, away_goals, teams, matches):
    if home_team_id == away_team_id:
        raise ValueError("team cannot play againts itself")
    team_ids=[team["id"] for team in teams]
    if home_team_id not in team_ids:
        raise ValueError("home team dose not exists")
    if away_team_id not in team_ids:
        raise ValueError("away team dose not exists")
    if home_goals < 0 or away_goals < 0:
        raise ValueError("goals cannot be negative")
    
    for match in matches:
        same_teams = (match["home_team_id"] == home_team_id and 
                      match["away_team_id"]==away_team_id)
        reverse_teams = (match["home_team_id"] == away_team_id
                         and match["away_team_id"] == home_team_id)
        if same_teams or reverse_teams:
            raise ValueError("these teams already played")
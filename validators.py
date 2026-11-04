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


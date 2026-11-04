import logging
from menu import show_menu, get_user_choice
from mock_data import teams, matches
from teams import add_team, show_all_teams
from matches import add_match 
from standings import show_standings


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s")

    logging.info("Tournament Manager started")

    while True:
        show_menu()
        choice = get_user_choice()

        if choice == 0:
            logging.info("tournament manager closed")
            print("goodbye!")
            break
        elif choice == 1:
            try:
                team_id = int(input("enter team id: "))
                team_name = input("enter team name: ")
                add_team(teams,team_id,team_name)
                print("team added")
            except ValueError as error:
                print(f"Error: {str(error)}")
                logging.warning("Failed to add team: %s", error)
        elif choice == 2:
            show_all_teams(teams)
            
        elif choice == 3:
            try:
                home_team_id = int(input("enter home team id: "))
                away_team_id = int(input("enter away team id: "))
                
                home_goals = int(input("enter home goals: "))
                away_goals =int(input("enter away goals: "))
                add_match(teams,matches,home_team_id,away_team_id,home_goals,away_goals)
                print("match added successfully")
            except ValueError as error:
                print(f"error: {error}")
                logging.warning("faild to add match: %s", error)
            
            
        elif choice == 4:
            show_standings(teams)
        elif choice == 5:
            print("Show leading team")
        elif choice == 6:
            print("Show best attacking team")
        elif choice == 7:
            print("Show team success rate")
        elif choice == 8:
            print("Show teams without wins")
        elif choice == 9:
            print("Show tournament summary")
        elif choice == 10:
            print("Check championship potential")
        else:
            print("Invalid choice. Please try again.")
            
print(teams)

if __name__ == "__main__":
    main()
    
    
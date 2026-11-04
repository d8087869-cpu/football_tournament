def show_menu():
    print("\n========== TOURNAMENT MANAGER ==========")
    print("1. Add team")
    print("2. Show all teams")
    print("3. Add match result")
    print("4. Show standings")
    print("5. Show leading team")
    print("6. Show best attacking team")
    print("7. Show team success rate")
    print("8. Show teams without wins")
    print("9. Show tournament summary")
    print("10. Check championship potential")
    print("0. Exit")

def get_user_choice():
    try:
        return int(input("Choose an option: "))
    except ValueError:
        return -1
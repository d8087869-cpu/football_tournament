import logging
from menu import show_menu, get_user_choice
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
            print("add team")
        elif choice == 2:
            print("Show all teams")
        elif choice == 3:
            print("Add match result")
        elif choice == 4:
            print("Show standings")
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
if __name__ == "__main__":
    main()
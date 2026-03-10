# cli/profile_view.py

from utils.screen import clear_screen
from utils.colors import Colors


def show_profile(user_data):

    clear_screen()

    print(Colors.TITLE + "========================================")
    print("              USER PROFILE              ")
    print("========================================" + Colors.RESET)

    print()
    print(Colors.OPTION + f"Full Name : {user_data['full_name']}")
    print(f"Username  : {user_data['username']}")
    print(f"Email     : {user_data['email']}" + Colors.RESET)

    print("----------------------------------------")

    input("Press Enter to return...")
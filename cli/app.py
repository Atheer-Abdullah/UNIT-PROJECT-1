# cli/app.py

import time
from cli.main_menu import main_menu
from auth.register import register
from utils.screen import clear_screen, print_header, print_divider
from utils.colors import Colors


def show_about_project():

    clear_screen()

    print_header("ABOUT CODEECHO")

    print()
    print("CodeEcho is a coding platform designed")
    print("to help learners with ADHD stay focused")
    print("while learning programming.")

    print()
    print("Platform Goals")

    print("• ADHD-friendly learning flow")
    print("• Secure user data handling")
    print("• Step-by-step coding lessons")

    print_divider()

    input("Press Enter to return to the main menu...")

def exit_program():
    """Exit message"""
    clear_screen()
    print(Colors.TITLE + "========================================")
    print("         THANK YOU FOR VISITING         ")
    print("========================================" + Colors.RESET)

    print(Colors.OPTION + "\nWe hope to see you again soon at CodeEcho." + Colors.RESET)
    print(Colors.OPTION + "Safe travels in your coding journey!" + Colors.RESET)

    print(Colors.WARNING + "\nClosing system..." + Colors.RESET)
    time.sleep(2)


def handle_invalid_choice(value):
    print(f"\nInvalid option: {value}. Please select between 0 and 3.")
    time.sleep(2)


def run():
    """Main application controller"""

    while True:

        choice = main_menu()

        if choice == "1":

            result = register()

            if result == "CANCELLED":
                continue

            if isinstance(result, dict):

                from cli.dashboard import dashboard
                dashboard(result)

            elif result == "GO_TO_LOGIN":

                from auth.login import login
                user_data = login()

                if isinstance(user_data, dict):

                    from cli.dashboard import dashboard
                    dashboard(user_data)

        elif choice == "2":

            from auth.login import login
            user_data = login()

            if isinstance(user_data, dict):
                from cli.dashboard import dashboard
                dashboard(user_data)

            elif user_data == "RETRY_LOGIN":
                continue

        elif choice == "3":
            show_about_project()

        elif choice == "0":
            exit_program()
            break

        else:
            handle_invalid_choice(choice)
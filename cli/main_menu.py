# cli/main_menu.py

from utils.screen import clear_screen
from utils.navigator import get_choice
from utils.colors import Colors


def main_menu():

    clear_screen()

    print("========================================")
    print(Colors.TITLE + "             ✦ CODEECHO ✦")
    print("        Designed for ADHD Focus" + Colors.RESET)
    print("========================================")

    print()

    print("1  Sign Up")
    print("2  Login")
    print("3  About Project")

    print(Colors.ERROR + "0  Exit" + Colors.RESET)

    print()

    print("----------------------------------------")

    while True:

        choice = get_choice("Select option: ")

        if choice in ["1", "2", "3", "0"]:
            return choice

        print(Colors.ERROR + "Invalid option" + Colors.RESET)
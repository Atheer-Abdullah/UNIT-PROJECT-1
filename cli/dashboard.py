# cli/dashboard.py

import time
from learning.path_menu import choose_path
from cli.profile_view import show_profile
from database.json_handler import DataHandler
from utils.colors import Colors
from utils.screen import clear_screen, print_header, print_divider
from config.paths import SETTINGS_FILE, PROGRESS_FILE
from cli.community_menu import community_menu

def save_learning_speed(username, speed):

    settings = DataHandler.load_json(SETTINGS_FILE)

    if not settings:
        settings = {}

    if username not in settings:
        settings[username] = {}

    settings[username]["learning_speed"] = speed

    DataHandler.save_json(SETTINGS_FILE, settings)


def settings_menu(user_data):

    while True:

        clear_screen()

        print("========================================")
        print(Colors.TITLE + "                SETTINGS" + Colors.RESET)
        print("========================================")

        print("1. Learning Speed")
        print(Colors.ERROR + "0. Back" + Colors.RESET)

        print("----------------------------------------")

        choice = input("Select option: ").strip()

        if choice == "1":

            clear_screen()

            print("========================================")
            print(Colors.TITLE + "             LEARNING SPEED" + Colors.RESET)
            print("========================================")

            print("\nChoose your learning pace\n")

            print("1. Calm Mode (slow)")
            print("2. Normal Mode")
            print("3. Fast Mode")

            print("----------------------------------------")

            speed_choice = input("Select speed: ").strip()

            if speed_choice == "1":
                speed = 1.2

            elif speed_choice == "3":
                speed = 0.85

            else:
                speed = 1.0

            save_learning_speed(user_data["username"], speed)

            print(Colors.SUCCESS + "\nLearning speed saved successfully" + Colors.RESET)
            input("\nPress Enter to continue...")

        elif choice == "0":
            return

        else:

            print(Colors.ERROR + "\nInvalid option" + Colors.RESET)
            time.sleep(1)


def dashboard(user_data):

    while True:

        clear_screen()

        progress_data = DataHandler.load_json(PROGRESS_FILE) or {}
        user_progress = progress_data.get(user_data["username"], {})

        daily_goal = user_progress.get("daily_goal", 2)
        today_progress = user_progress.get("today_progress", 0)

        #  حتى لا يتجاوز الهدف
        today_progress = min(today_progress, daily_goal)

        print_header(f"WELCOME, {user_data['full_name'].upper()}")

        print()

        print(Colors.WARNING + f"Today's Goal: {daily_goal} lessons" + Colors.RESET)
        print(Colors.SUCCESS + f"Progress: {today_progress} / {daily_goal}" + Colors.RESET)

        print_divider()

        print("1  Start Learning")
        print("2  View Profile")
        print("3  Community")
        print("4  Settings")
        print(Colors.ERROR + "0  Logout" + Colors.RESET)

        print_divider()

        choice = input("Select option: ").strip()

        if choice == "1":

            choose_path(user_data)

        elif choice == "2":

            show_profile(user_data)

        elif choice == "3":

            community_menu(user_data)

        elif choice == "4":

            settings_menu(user_data)

        elif choice == "0":

            print(Colors.WARNING + "\nLogging out..." + Colors.RESET)
            time.sleep(1)

            break

        else:

            print(Colors.ERROR + "\nInvalid option" + Colors.RESET)
            time.sleep(1)
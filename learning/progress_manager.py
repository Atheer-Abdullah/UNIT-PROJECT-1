# learning/progress_manager.py

from datetime import datetime, timedelta
from database.json_handler import DataHandler
from utils.navigator import get_choice
from utils.screen import clear_screen
from colorama import Fore, Style

PROGRESS_FILE = "data/progress.json"


# -------------------------------------------------
# Resume Learning
# -------------------------------------------------
def resume_learning(user_data):

    progress = DataHandler.load_json(PROGRESS_FILE)
    user_progress = progress.get(user_data["username"])

    if not user_progress:
        print("No learning progress found.")
        input("Press Enter to return...")
        return

    while True:

        clear_screen()

        print(Fore.CYAN + "========================================")
        print("         RESUME YOUR LEARNING           ")
        print(Fore.CYAN + "========================================")

        paths = [
            key for key in user_progress.keys()
            if key not in ["last_study_date", "streak"]
        ]

        for i, path in enumerate(paths, 1):

            path_name = path.replace("_", " ").upper()
            level = user_progress[path]

            print(
                f"{Fore.GREEN}{i}.{Style.RESET_ALL} "
                f"{path_name:<15} | Current Lesson: {Fore.YELLOW}{level}"
            )

        print(f"{Fore.GREEN}B.{Style.RESET_ALL} Back")

        print(Fore.WHITE + "-" * 40)

        choice = get_choice("Select path: ")

        if choice == "b":
            return

        if choice.isdigit():

            index = int(choice) - 1

            if 0 <= index < len(paths):
                return paths[index]


# -------------------------------------------------
# Learning Streak System
# -------------------------------------------------
def update_learning_streak(username):

    progress = DataHandler.load_json(PROGRESS_FILE)

    if username not in progress:
        return

    user = progress[username]

    today = datetime.today().date()

    last_date_str = user.get("last_study_date")

    if last_date_str:

        last_date = datetime.strptime(last_date_str, "%Y-%m-%d").date()

        if today == last_date:
            return

        elif today == last_date + timedelta(days=1):
            user["streak"] = user.get("streak", 0) + 1

        else:
            user["streak"] = 1

    else:
        user["streak"] = 1

    user["last_study_date"] = str(today)

    DataHandler.save_json(PROGRESS_FILE, progress)
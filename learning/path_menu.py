#learning/path_menu.py
from database.json_handler import DataHandler
from learning.lesson_runner import start_learning_path
from utils.screen import clear_screen
from utils.navigator import get_choice, is_back
from services.adhd_tools import focus_timer
from utils.colors import Colors

PROGRESS_FILE = "data/progress.json"


PATHS = {
    "1": ("Python Programming 101", "python_101.json"),
    "2": ("Java Programming 101", "java_101.json"),
    "3": ("C++ Programming 101", "cpp_101.json"),
}


def choose_path(user_data):

    while True:

        clear_screen()

        print("========================================")
        print(Colors.TITLE + "            LEARNING PATHS" + Colors.RESET)
        print("========================================")

        print()

        for key, value in PATHS.items():
            print(f"{key}. {value[0]}")

        print()
        print(Colors.ERROR + "B. Back" + Colors.RESET)

        print("----------------------------------------")

        choice = get_choice("Select a learning path: ")

        if is_back(choice):
            return

        if choice in PATHS:

            path_title, file_name = PATHS[choice]

            show_lessons(user_data, path_title, file_name)


def show_lessons(user_data, path_title, file_name):

    path_data = DataHandler.load_json(f"data/{file_name}")
    progress_data = DataHandler.load_json(PROGRESS_FILE)

    lessons = path_data["lessons"]

    user_progress = progress_data.get(user_data["username"], {})

    current_lesson = user_progress.get(file_name.replace(".json", ""), 1)

    while True:

        clear_screen()

        print("========================================")
        print(Colors.TITLE + f"        {path_title.upper()}" + Colors.RESET)
        print("========================================")

        print()

        for i, lesson in enumerate(lessons, 1):

            title = lesson["title"]

            if i < current_lesson:
                status = Colors.SUCCESS + "Completed" + Colors.RESET

            elif i == current_lesson:
                status = Colors.WARNING + "Current Lesson" + Colors.RESET

            else:
                status = Colors.ERROR + "Locked" + Colors.RESET

            print(f"{i}. {title:<22} {status}")

        print()
        print("----------------------------------------")

        print(Colors.WARNING + "Select a lesson number" + Colors.RESET)
        print(Colors.ERROR + "B. Back" + Colors.RESET)

        print("----------------------------------------")

        choice = get_choice("Select a learning path: ")

        if choice == "b":
            return

        if choice.isdigit():

            lesson_number = int(choice)

            if lesson_number > current_lesson:

                print(
                    Colors.ERROR
                    + "\nLesson locked. Complete previous lessons first."
                    + Colors.RESET
                )

                input("\nPress Enter to continue...")
                continue

            clear_screen()

            focus_timer(1)

            start_learning_path(user_data, file_name, lesson_number)
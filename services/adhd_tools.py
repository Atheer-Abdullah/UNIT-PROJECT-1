# services/adhd_tools.py

import time
import random
import sys
import os
from colorama import Fore, Style


def focus_timer(minutes=3):

    total_seconds = minutes * 60

    print("========================================")
    print(Fore.CYAN + "              FOCUS MODE" + Style.RESET_ALL)
    print("========================================")

    print()

    print("Focus session started")

    print(
        Fore.YELLOW
        + f"\nDuration: {minutes} minute"
        + Style.RESET_ALL
    )

    print("\nStay focused on the lesson\n")

    while total_seconds > 0:

        mins = total_seconds // 60
        secs = total_seconds % 60

        timer = f"{mins:02d}:{secs:02d}"

        print(
            Fore.YELLOW
            + f"\rTime remaining: {timer}"
            + Style.RESET_ALL,
            end=""
        )

        time.sleep(1)

        total_seconds -= 1

    print("\n")

    print(Fore.GREEN + "Great focus!" + Style.RESET_ALL)

    try:

        if os.name == "nt":

            import msvcrt

            while msvcrt.kbhit():
                msvcrt.getch()

        else:

            import termios

            termios.tcflush(sys.stdin, termios.TCIFLUSH)

    except:
        pass

    input("\nPress Enter to start the lesson...")


def motivation_message():

    messages = [

        "Great focus! Keep going.",
        "Small steps lead to big coding skills.",
        "You're doing amazing. Keep learning.",
        "Consistency beats talent.",
        "Every lesson makes you stronger."

    ]

    print(
        Fore.MAGENTA
        + "\n"
        + random.choice(messages)
        + "\n"
        + Style.RESET_ALL
    )


def focus_header(title):

    print("========================================")
    print(Fore.CYAN + f"{title.center(40)}" + Style.RESET_ALL)
    print("========================================")


def show_learning_streak(progress):

    completed = 0

    for key, value in progress.items():

        if key in ["streak", "last_study_date"]:
            continue

        if isinstance(value, int):
            completed += value

    print(
        Fore.CYAN
        + f"\nLearning streak: {completed} lessons completed!\n"
        + Style.RESET_ALL
    )


def choose_learning_speed():

    print("\nChoose learning speed:\n")

    print("1. Calm Mode")
    print("2. Normal Mode")
    print("3. Fast Mode")

    choice = input("\nSelect: ").strip()

    if choice == "1":
        return 3.0

    elif choice == "3":
        return 0.1

    return 1.0


def get_speed(user_settings):

    return user_settings.get("learning_speed", 0.8)
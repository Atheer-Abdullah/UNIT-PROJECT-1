# utils/screen.py

import subprocess
import platform
import time
from utils.colors import Colors


def clear_screen():
    command = "cls" if platform.system() == "Windows" else "clear"
    subprocess.run(command, shell=True)


def print_header(title, subtitle=None):
    """
    Unified header for the whole project
    """

    print("========================================")
    print(Colors.TITLE + title.center(40) + Colors.RESET)

    if subtitle:
        print(Colors.TITLE + subtitle.center(40) + Colors.RESET)

    print("========================================")


def print_divider():
    """
    White divider line
    """
    print("----------------------------------------")


def pause(seconds=1):
    time.sleep(seconds)
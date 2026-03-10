# lesson_player.py
import time
from utils.screen import clear_screen
from services.audio_service import play_audio
from colorama import Fore, Back, Style


def play_lesson(lesson, speed=1):

    lines = []

    for step in lesson["content"]:

        for line in step["code"].split("\n"):
            lines.append({
                "text": line,
                "audio": step.get("audio_code", line),
                "type": "code"
            })

        if "note" in step:
            lines.append({
                "text": f"Note: {step['note']}",
                "audio": step.get("audio_note", step["note"]),
                "type": "note"
            })

    should_replay = True

    while True:

        if should_replay:

            for idx, item in enumerate(lines, 1):

                clear_screen()

                print("========================================")
                print(Fore.CYAN + f"             {lesson['title'].upper()}" + Style.RESET_ALL)
                print("========================================")
                print()

                for prev in range(idx - 1):
                    print(f"{prev+1}. {lines[prev]['text']}")

                line_text = item["text"]

                color = Fore.WHITE if item["type"] == "code" else Fore.YELLOW

                print(
                    f"{Fore.WHITE}{Back.BLACK}{idx}. "
                    f"{color}{Style.BRIGHT}{line_text}{Style.RESET_ALL}"
                )

                play_audio(item["audio"], speed)

                time.sleep(speed)

            should_replay = False

        clear_screen()

        print("========================================")
        print(Fore.CYAN + f"             {lesson['title'].upper()}" + Style.RESET_ALL)
        print("========================================")
        print()

        for i, item in enumerate(lines, 1):

            color = Fore.WHITE if item["type"] == "code" else Fore.YELLOW

            print(f"{i}. {color}{item['text']}{Style.RESET_ALL}")

        print("\n----------------------------------------")

        print(Fore.CYAN + "CONTROLS" + Style.RESET_ALL)
        print("Enter  → Quiz")
        print("R      → Replay lesson")
        print("Number → Replay line")
        print(Fore.RED + "B      → Back" + Style.RESET_ALL)

        print("----------------------------------------")

        choice = input("Your choice: ").strip().lower()

        if choice == "r":
            should_replay = True
            continue

        elif choice.isdigit():

            idx = int(choice) - 1

            if 0 <= idx < len(lines):

                clear_screen()

                for i, item in enumerate(lines):

                    if i == idx:

                        color = Fore.WHITE if item["type"] == "code" else Fore.YELLOW

                        print(
                            f"{Fore.WHITE}{Back.BLACK}{i+1}. "
                            f"{color}{Style.BRIGHT}{item['text']}{Style.RESET_ALL}"
                        )

                        play_audio(item["audio"])

                    else:

                        print(f"{i+1}. {lines[i]['text']}")

                input("\nPress Enter to return...")

            continue

        elif choice == "b":
            return "BACK"

        elif choice == "":
            break

    quiz = lesson.get("quiz")

    if quiz:

        while True:

            clear_screen()

            print("========================================")
            print(Fore.CYAN + "                 QUIZ" + Style.RESET_ALL)
            print("========================================")

            print()

            print("Question")
            print(quiz["question"])

            print("\n----------------------------------------\n")

            for opt in quiz["options"]:
                print(opt)

            print("\n----------------------------------------")

            answer = input(
                Fore.YELLOW + "\nAnswer (A / B / C): " + Style.RESET_ALL
            ).strip().upper()

            if answer not in ["A", "B", "C"]:

                print(Fore.YELLOW + "\nEnter A, B, or C only" + Style.RESET_ALL)
                time.sleep(1.5)
                continue

            if answer == quiz["answer"]:

                print(Fore.GREEN + "\nCorrect!" + Style.RESET_ALL)
                time.sleep(1.5)
                break

            else:

                print(Fore.RED + "\nIncorrect answer" + Style.RESET_ALL)
                time.sleep(1.5)

        while True:

            clear_screen()

            print("========================================")
            print(Fore.CYAN + "              QUIZ COMPLETE" + Style.RESET_ALL)
            print("========================================")

            print()

            print(Fore.GREEN + "Correct answer." + Style.RESET_ALL)

            print("\n----------------------------------------\n")

            print("Enter  → Next lesson")
            print(Fore.RED + "B      → Back to lessons" + Style.RESET_ALL)

            print("\n----------------------------------------")

            choice = input(
                Fore.YELLOW + "\nYour choice: " + Style.RESET_ALL
            ).strip().lower()

            if choice == "":
                break

            elif choice == "b":
                return "BACK"

            else:
                print(Fore.YELLOW + "Press Enter or type B" + Style.RESET_ALL)
                time.sleep(1)
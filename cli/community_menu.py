from utils.screen import clear_screen, print_header, print_divider
from utils.navigator import get_choice
from services.community_service import load_questions, add_question, add_answer
from utils.colors import Colors


def community_menu(user_data):

    while True:

        clear_screen()

        print_header("COMMUNITY")

        print("1 Ask Question")
        print("2 View Questions")
        print("B Back")

        print_divider()

        choice = get_choice("Select option: ")

        if choice == "1":
            ask_question(user_data)

        elif choice == "2":
            view_questions(user_data)

        elif choice == "b":
            return


def ask_question(user_data):

    clear_screen()

    print_header("ASK QUESTION")

    question = input("Write your question: ").strip()

    if not question:
        print(Colors.ERROR + "Question cannot be empty" + Colors.RESET)
        input("Press Enter to continue...")
        return

    add_question(user_data["username"], question)

    print(Colors.SUCCESS + "Question posted successfully" + Colors.RESET)

    input("Press Enter to continue...")


def view_questions(user_data):

    data = load_questions()

    questions = data["questions"]

    if not questions:

        print("No questions yet")

        input("Press Enter to return")
        return

    while True:

        clear_screen()

        print_header("QUESTIONS")

        for q in questions:
            print(f"{q['id']} - {q['question']} (by {q['user']})")

        print()
        print("B Back")

        print_divider()

        choice = get_choice("Select question number: ")

        if choice == "b":
            return

        if choice.isdigit():

            question_id = int(choice)

            for q in questions:

                if q["id"] == question_id:

                    open_question(user_data, q)

                    break


def open_question(user_data, question):

    while True:

        clear_screen()

        print_header("QUESTION")

        print(question["question"])
        print(f"asked by {question['user']}")

        print_divider()

        print("Answers:\n")

        if not question["answers"]:
            print("No answers yet\n")

        for a in question["answers"]:
            print(f"{a['user']}: {a['answer']}\n")

        print_divider()

        print("1 Add Answer")
        print("B Back")

        print_divider()

        choice = get_choice("Select option: ")

        if choice == "1":

            answer = input("Write your answer: ").strip()

            if answer:

                add_answer(question["id"], user_data["username"], answer)

                print(Colors.SUCCESS + "Answer added" + Colors.RESET)

                input("Press Enter to continue...")

        elif choice == "b":
            return
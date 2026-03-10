# utils/navigator.py

def get_choice(prompt):

    while True:

        choice = input(prompt).strip().lower()

        if choice == "b":
            return "b"

        if choice.isdigit():
            return choice

        print("Invalid option")

def is_back(choice):
    """
    يتحقق إذا المستخدم يريد الرجوع
    """
    return choice.lower() == "b"


def is_exit(choice):
    """
    يتحقق إذا المستخدم يريد الخروج
    """
    return choice.lower() == "exit"
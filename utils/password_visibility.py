# utils/password_visibility.py

from utils.colors import Colors


def ask_password_visibility():
    """
   ؟ يسأل المستخدم هل تريد إظهار كلمة المرور أثناء الكتابة
    يرجع:
    True  -> إظهار كلمة المرور
    False -> إخفاء كلمة المرور
    "CANCELLED" -> إذا كتب المستخدم exit
    """

    while True:

        choice = input(
            "Show password "
            + Colors.WARNING
            + "(y/n)"
            + Colors.RESET
            + ": "
        ).strip().lower()

        if choice == "exit":
            return "CANCELLED"

        if choice in ["y", "n"]:
            return choice == "y"

        print(Colors.ERROR + "Enter y or n" + Colors.RESET)
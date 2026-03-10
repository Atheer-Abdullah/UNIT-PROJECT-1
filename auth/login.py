# auth/login.py
import time
import pwinput
from utils.screen import clear_screen
from database.db_manager import DBManager
from utils.security import check_password
from utils.validator import validate_email
from utils.colors import Colors
from utils.input_attempts import attempt_loop
from utils.password_visibility import ask_password_visibility

def login():
    clear_screen()

    print("========================================")
    print(Colors.TITLE + "                LOGIN" + Colors.RESET)
    print("========================================")

    print(Colors.WARNING + "\nType 'exit' anytime to cancel" + Colors.RESET)
    print("----------------------------------------\n")

    # 1. طلب الإيميل
    for attempts in attempt_loop():

        email = input(
            "Gmail Address "
            + Colors.WARNING
            + f"({attempts} attempts left)"
            + Colors.RESET
            + ": "
        ).strip().lower()

        if email == 'exit':
            return "CANCELLED"

        if not validate_email(email):
            print(Colors.ERROR + "Enter a valid Gmail address" + Colors.RESET)

            

            if attempts == 1:
                print(Colors.ERROR + "Too many failed attempts" + Colors.RESET)
                time.sleep(2)
                return "FAILED"

            continue

        user = DBManager.get_user_by_email(email)

        if not user:
            print(Colors.ERROR + "Account not found" + Colors.RESET)

            while True:
                choice = input("Retry (R) | Sign up (S) | Forgot password (F): ").lower().strip()

                if choice in ['r', 's', 'f', 'exit']:
                    break

                print(Colors.ERROR + "Enter R, S, F or exit" + Colors.RESET)

            if choice == 'exit':
                return "CANCELLED"

            elif choice == 's':
                return "GO_TO_REGISTER"

            elif choice == 'f':
                from auth.forgot_password import reset_password
                reset_password()
                return "RETRY_LOGIN"

            

            if attempts == 1:
                print(Colors.ERROR + "Too many failed attempts" + Colors.RESET)
                time.sleep(2)
                return "FAILED"

            continue

        break

    # سؤال إظهار كلمة المرور
    show_pass = ask_password_visibility()

    if show_pass == "CANCELLED":
        return "CANCELLED"

    # 2. التحقق من كلمة المرور
    attempts = 3

    while attempts > 0:

        prompt_msg = (
            "Password "
            + Colors.WARNING
            + f"({attempts} attempts left)"
            + Colors.RESET
            + ": "
        )

        if show_pass:
            password = input(prompt_msg).strip()
        else:
            password = pwinput.pwinput(prompt=prompt_msg, mask="*")

        if password.lower() == 'exit':
            return "CANCELLED"

        if check_password(password, user['password']):
            print(Colors.SUCCESS + f"Welcome back, {user['full_name']}" + Colors.RESET)
            time.sleep(1.5)
            return user

        

        if attempts > 0:
            print(Colors.ERROR + "Incorrect password" + Colors.RESET)

            while True:
                reset_choice = input("Reset password? (y/n): ").lower().strip()

                if reset_choice == 'exit':
                    return "CANCELLED"

                if reset_choice == 'y':
                    from auth.forgot_password import reset_password
                    reset_password()
                    return "RETRY_LOGIN"

                elif reset_choice == 'n':
                    break

                print(Colors.ERROR + "Enter y or n" + Colors.RESET)

        else:
            print(Colors.ERROR + "Access denied" + Colors.RESET)
            time.sleep(2)
            return "FAILED"
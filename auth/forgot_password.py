# auth/forgot_password.py
import random
import time
import pwinput
from utils.screen import clear_screen
from database.db_manager import DBManager
from services.email_service import send_otp
from utils.security import hash_password
from utils.validator import validate_email, validate_password
from utils.colors import Colors
from utils.otp_handler import verify_otp
from utils.password_visibility import ask_password_visibility

def reset_password():

    clear_screen()

    print("========================================")
    print(Colors.TITLE + "           PASSWORD RECOVERY" + Colors.RESET)
    print("========================================")

    print(Colors.WARNING + "\nReset your CodeEcho password")
    print("Type 'exit' anytime to cancel" + Colors.RESET)

    print("----------------------------------------\n")

    while True:

        email = input(
            "Gmail Address "
            + Colors.WARNING
            + "(registered account)"
            + Colors.RESET
            + ": "
        ).strip().lower()

        if email == "exit":
            return "CANCELLED"

        if not validate_email(email):

            print(Colors.ERROR + "Invalid Gmail address format" + Colors.RESET)
            continue

        user = DBManager.get_user_by_email(email)

        if not user:

            print(Colors.ERROR + "No account found with this email" + Colors.RESET)
            continue

        break

    otp_code = str(random.randint(100000, 999999))

    print(Colors.WARNING + f"\nSending recovery code to {email}" + Colors.RESET)

    if not send_otp(email, otp_code):

        print(Colors.ERROR + "Failed to send recovery email" + Colors.RESET)
        return "FAILED"

    verification = verify_otp(otp_code)

    if verification == "CANCELLED":
        return "CANCELLED"

    if verification is False:
        return "FAILED"

    show_pass = ask_password_visibility()

    if show_pass == "CANCELLED":
        return "CANCELLED"

    while True:

        print(
            Colors.WARNING
            + "\nPassword must include letters, numbers, and symbols"
            + Colors.RESET
        )

        prompt_1 = "New Password: "
        prompt_2 = "Confirm Password: "

        if show_pass:

            new_password = input(prompt_1).strip()

            if new_password.lower() == "exit":
                return "CANCELLED"

            confirm_password = input(prompt_2).strip()

        else:

            new_password = pwinput.pwinput(prompt_1, mask="*").strip()

            if new_password.lower() == "exit":
                return "CANCELLED"

            confirm_password = pwinput.pwinput(prompt_2, mask="*").strip()

        if validate_password(new_password):

            if new_password == confirm_password:

                hashed = hash_password(new_password)

                if DBManager.update_password(email, hashed):

                    print(Colors.SUCCESS + "\nPassword updated successfully" + Colors.RESET)
                    print("Please login with your new password")

                    time.sleep(2)

                    return "SUCCESS"

                else:

                    print(Colors.ERROR + "Failed to update password" + Colors.RESET)
                    return "FAILED"

            else:

                print(Colors.ERROR + "Passwords do not match" + Colors.RESET)

        else:

            print(
                Colors.ERROR
                + "Password is too weak. Use letters, numbers, and symbols"
                + Colors.RESET
            )
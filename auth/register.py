#auth/rigister.py
import random
import time
import pwinput
from utils.screen import clear_screen
from database.db_manager import DBManager
from services.email_service import send_otp
from utils.security import hash_password
from utils.validator import validate_name, validate_email, validate_username, validate_password
from utils.colors import Colors
from utils.input_attempts import attempt_loop
from utils.otp_handler import verify_otp
from utils.password_visibility import ask_password_visibility

def register():

    clear_screen()

    print("========================================")
    print(Colors.TITLE + "            CREATE ACCOUNT" + Colors.RESET)
    print("========================================")

    print(Colors.WARNING + "\nCreate your CodeEcho account")
    print("Type 'exit' anytime to cancel" + Colors.RESET)

    print("----------------------------------------\n")

    # Full Name 
    while True:
        full_name = input(
            "Full Name "
            + Colors.WARNING
            + Colors.RESET
            + ": "
        )

        if full_name.lower() == "exit":
            return "CANCELLED"

        if validate_name(full_name):
            break
        
        print(Colors.ERROR + "Name must contain letters only" + Colors.RESET)

        if attempts == 1:
            return "FAILED"

    #Username 
    for attempts in attempt_loop():

        username = input(
            "Username "
            + Colors.WARNING
            + "(letters & numbers, min 4)"
            + Colors.RESET
            + f" ({attempts} attempts)"
            + ": "
        ).strip()

        if username.lower() == "exit":
            return "CANCELLED"

        if validate_username(username):

            if not DBManager.user_exists_by_username(username):
                break

            print(Colors.ERROR + "Username already exists" + Colors.RESET)

        else:
            print(Colors.ERROR + "Invalid username" + Colors.RESET)


        if attempts == 1:
            return "FAILED"

    # Email 
    for attempts in attempt_loop():

        email = input(
            "Gmail Address "
            + Colors.WARNING
            + "(gmail only)"
            + Colors.RESET
            + f" ({attempts} attempts)"
            + ": "
        ).strip().lower()

        if email == "exit":
            return "CANCELLED"

        if validate_email(email):

            if DBManager.user_exists(email):

                print(Colors.ERROR + "Email already registered" + Colors.RESET)

                action = input("Login instead or Retry? (L/R): ").lower()

                if action == "l":
                    return "GO_TO_LOGIN"

            else:
                break

        else:
            print(Colors.ERROR + "Enter a valid Gmail address" + Colors.RESET)


        if attempts == 1:

            print(Colors.ERROR + "\nToo many failed attempts." + Colors.RESET)

            while True:

                choice = input(
                    "\n1. Retry email\n2. Back to menu\nSelect: "
                ).strip()

                if choice == "1":
                    attempts = 3
                    break

                elif choice == "2":
                    return "FAILED"

                else:
                    print("Invalid choice")

    #  Show password 
    show_pass = ask_password_visibility()

    if show_pass == "CANCELLED":
        return "CANCELLED"

    #  Password 
    for attempts in attempt_loop():

        print(Colors.WARNING + "Password must include letter, number, symbol" + Colors.RESET)

        prompt1 = "Password: "
        prompt2 = "Confirm Password: "

        if show_pass:

            password = input(prompt1).strip()

            if password.lower() == "exit":
                return "CANCELLED"

            confirm_password = input(prompt2).strip()

        else:

            password = pwinput.pwinput(prompt=prompt1, mask="*").strip()

            if password.lower() == "exit":
                return "CANCELLED"

            confirm_password = pwinput.pwinput(prompt=prompt2, mask="*").strip()

        if validate_password(password):

            if password == confirm_password:
                break

            print(Colors.ERROR + "Passwords do not match" + Colors.RESET)

        else:
            print(Colors.ERROR + "Password too weak" + Colors.RESET)


        if attempts == 1:
            return "FAILED"

    #  OTP 
    otp_code = str(random.randint(100000, 999999))

    print(Colors.WARNING + f"\nSending verification code to {email}" + Colors.RESET)

    if not send_otp(email, otp_code):

        print(Colors.ERROR + "\nUnable to send verification email" + Colors.RESET)
        input("Press Enter to return")

        return "FAILED"

    verification = verify_otp(otp_code)

    if verification == "CANCELLED":
        return "CANCELLED"

    if verification is False:
        return "FAILED"
    #  Save user 
    user_data = {
        "full_name": full_name,
        "username": username,
        "email": email,
        "password": hash_password(password),
        "created_at": time.strftime("%Y-%m-%d %H:%M:%S")
    }

    if DBManager.save_user(user_data):

        print("\n" + "=" * 40)
        print(Colors.SUCCESS + "Account created successfully" + Colors.RESET)

        time.sleep(2)

        return user_data

    else:

        print(Colors.ERROR + "Failed to save account data" + Colors.RESET)

        time.sleep(2)

        return "FAILED"
from utils.input_attempts import attempt_loop
from utils.colors import Colors


def verify_otp(expected_code):

    for attempts in attempt_loop():

        user_otp = input(
            "Enter the 6-digit verification code "
            + Colors.WARNING
            + f"[{attempts} attempts left]"
            + Colors.RESET
            + ": "
        ).strip()

        if user_otp.lower() == "exit":
            return "CANCELLED"

        if user_otp == expected_code:
            print(Colors.SUCCESS + "Email verified successfully" + Colors.RESET)
            return True

        print(Colors.ERROR + "Incorrect verification code" + Colors.RESET)

        if attempts == 1:
            print(Colors.ERROR + "Too many incorrect attempts" + Colors.RESET)
            return False
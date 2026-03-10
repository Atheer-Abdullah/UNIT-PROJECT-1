# auth/email_service.py
import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv 

# Load environment variables from .env file
load_dotenv()

def send_otp(receiver_email, otp_code):
    # يجلب القيم داخل الدالة لضمان قراءتها من النظام في كل محاولة
    sender_email = os.getenv("CODEECHO_EMAIL")
    app_password = os.getenv("CODEECHO_APP_PASSWORD")

    # التحقق من أن القيم موجودة
    if not sender_email or not app_password:
        print(" Error: Environment variables CODEECHO_EMAIL or CODEECHO_APP_PASSWORD are missing!")
        return False

    msg = EmailMessage()
    msg.set_content(f"Your CodeEcho Verification Code is: {otp_code}")
    msg['Subject'] = 'CodeEcho Verification'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    try:
        # استخدام المنفذ 465 مع SSL
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, app_password)
            smtp.send_message(msg)
        return True
    except Exception as e:
        if "10054" in str(e):
            print("\n Network Error: Your network/firewall is blocking the email connection.")
            print(" Suggestion: Try switching to a different Wi-Fi or mobile hotspot.")
        else:
            print(f" Error sending email: {e}")
        return False
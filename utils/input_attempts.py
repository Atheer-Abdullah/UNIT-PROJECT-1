# utils/input_attempts.py

def attempt_loop(max_attempts=3):
    """
    مولد يساعد في تكرار المحاولات بدون تكرار الكود في كل ملف
    يرجع عدد المحاولات المتبقية في كل دورة.
    """
    attempts = max_attempts

    while attempts > 0:
        yield attempts
        attempts -= 1
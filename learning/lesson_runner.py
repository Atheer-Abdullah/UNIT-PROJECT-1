#lesson_runner.py
from database.json_handler import DataHandler
from learning.lesson_player import play_lesson
from services.adhd_tools import get_speed, show_learning_streak
from learning.progress_manager import update_learning_streak

SETTINGS_FILE = "data/settings.json"
PROGRESS_FILE = "data/progress.json"


def start_learning_path(user_data, filename, lesson_number=1):

    path_data = DataHandler.load_json(f"data/{filename}")

    settings = DataHandler.load_json(SETTINGS_FILE)
    user_settings = settings.get(user_data['username'], {})

    speed = get_speed(user_settings)

    progress = DataHandler.load_json(PROGRESS_FILE)
    user_progress = progress.get(user_data['username'], {})

    show_learning_streak(user_progress)

    lessons = path_data.get("lessons", [])

    for lesson in lessons[lesson_number - 1:]:

        result = play_lesson(lesson, speed)

        if result == "b" or result == "BACK":
            return

        update_learning_streak(user_data["username"])

        progress = DataHandler.load_json(PROGRESS_FILE)

        username = user_data["username"]
        user = progress.get(username, {})

# تحديث تقدم المسار
        path_key = filename.replace(".json", "")
        user[path_key] = lesson["lesson_id"] + 1

# تحديث تقدم اليوم
        user["today_progress"] = user.get("today_progress", 0) + 1

        progress[username] = user

        DataHandler.save_json(PROGRESS_FILE, progress)
#community_service.py
from database.json_handler import DataHandler

COMMUNITY_FILE = "data/community.json"


def load_questions():
    data = DataHandler.load_json(COMMUNITY_FILE)

    if not data:
        return {"questions": []}

    return data


def save_questions(data):
    DataHandler.save_json(COMMUNITY_FILE, data)


def add_question(username, question_text):

    data = load_questions()

    question_id = len(data["questions"]) + 1

    question = {
        "id": question_id,
        "user": username,
        "question": question_text,
        "answers": []
    }

    data["questions"].append(question)

    save_questions(data)


def add_answer(question_id, username, answer_text):

    data = load_questions()

    for q in data["questions"]:

        if q["id"] == question_id:

            q["answers"].append({
                "user": username,
                "answer": answer_text
            })

            break

    save_questions(data)
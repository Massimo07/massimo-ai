import json
import os

USERS_PATH = "data/users.json"
USERS = {}

def load_all_users():
    global USERS
    if os.path.exists(USERS_PATH):
        with open(USERS_PATH, "r", encoding="utf-8") as f:
            USERS = json.load(f)
    else:
        USERS = {}

def save_all_users():
    with open(USERS_PATH, "w", encoding="utf-8") as f:
        json.dump(USERS, f, ensure_ascii=False, indent=2)

def get_user(user_id):
    if str(user_id) not in USERS:
        USERS[str(user_id)] = {
            "lang": "it",
            "name": "",
            "nation": "",
            "level": 0,
            "quiz_done": False,
            "registered": False,
            "code": "",
            "sponsor": "",
            "support": "",
            "faq_done": False,
        }
    return USERS[str(user_id)]

def fallback_handler(update, context):
    try:
        # Se c'è message normale
        if hasattr(update, 'message') and update.message:
            update.message.reply_text("Non ho capito, usa il menu! ⬅️")
        # Se callback da pulsante
        elif hasattr(update, 'callback_query') and update.callback_query:
            update.callback_query.message.reply_text("Non ho capito, usa il menu! ⬅️")
    except Exception as e:
        print(f"Errore nel fallback: {e}")

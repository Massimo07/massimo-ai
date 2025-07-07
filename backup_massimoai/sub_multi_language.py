from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

# services/multi_language.py

import json

def load_translation(lang_code):

    with open(f"translations/{lang_code}.json", "r", encoding="utf-8") as f:

        return json.load(f)

def translate(text_id, lang_code):

    translations = load_translation(lang_code)

    return translations.get(text_id, text_id)

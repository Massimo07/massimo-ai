from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

# services/feedback.py

def save_feedback(user_id, service, feedback, feedback_db):

    feedback_db.append({

        "user_id": user_id,

        "service": service,

        "feedback": feedback

    })

    # Salva su file o DB

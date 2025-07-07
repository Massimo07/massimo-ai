from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

# AI PDF Q&A – Risposte AI a domande su PDF caricati

async def ai_pdf_qa_handler(update, context):

    await update.callback_query.edit_message_text(

        "📑 Carica un PDF (regolamento, catalogo, manuale) e chiedi qualsiasi cosa: Massimo AI ti risponde subito con la risposta estratta dal documento."

    )

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")

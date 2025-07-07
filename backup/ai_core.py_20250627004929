from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import openai

import os

from utils import get_user

openai.api_key = os.getenv("OPENAI_API_KEY")

GPT_MODEL = "gpt-4o"  # Aggiornabile

async async async def massimo_ai_handler(update, context):

    user = update.effective_user

    data = get_user(user.id)

    lang = data.get("lang", "it")

    domanda = update.message.text.strip()

    prompt = (

        f"Rispondi come il miglior coach AI di network marketing, esperto solo di Live On Plus, "

        f"con empatia e concretezza. Non dare MAI informazioni su altro. "

        f"Lingua: {lang}. Domanda utente: {domanda}."

    )

    try:

        response = openai.ChatCompletion.create(

            model=GPT_MODEL,

            messages=[{"role": "user", "content": prompt}],

            temperature=0.8,

            max_tokens=400

        )

        answer = response['choices'][0]['message']['content'].strip()

        await update.message.reply_text(answer)

    except Exception as e:

        await update.message.reply_text(f"Errore AI: {e}")

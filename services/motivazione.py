from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

import openai

async def motivazione_handler(update, context):

    user = update.effective_user

    name = user.first_name

    prompt = f"Scrivi una frase motivazionale personalizzata per network marketing e crescita personale per {name}. Firma come Massimo AI."

    response = openai.ChatCompletion.create(

        model="gpt-4o",

        messages=[{"role": "user", "content": prompt}],

        temperature=0.8,

        max_tokens=80

    )

    text = f"✨ {response['choices'][0]['message']['content'].strip()}"

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")

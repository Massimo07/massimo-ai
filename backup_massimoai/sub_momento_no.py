from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

async async async def momento_no_handler(update, context):

    user = update.effective_user

    prompt = (

        "Rispondi con empatia e motivazione a una persona triste, abbattuta o in difficoltà che chiede aiuto a Massimo AI. "

        "Usa tono positivo, umano, concreto. Incoraggiala a credere in sé stessa e a ripartire, come faresti tu Massimo."

    )

    import openai

    response = openai.ChatCompletion.create(

        model="gpt-4o",

        messages=[{"role": "user", "content": prompt}],

        temperature=0.8,

        max_tokens=100

    )

    text = f"🤗 {response['choices'][0]['message']['content'].strip()}"

    await context.bot.send_message(chat_id=user.id, text=text)

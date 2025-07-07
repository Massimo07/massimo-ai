from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_adobe_livello_2_handler(update, context):

    user = update.effective_user

    text = (

        "🖌️ *Adobe Suite – Livello 2*\n\n"

        "Photoshop: filtri, livelli, testo. Illustrator: icone semplici. Canva: grafica social. Premiere: timeline base. Acrobat: aggiungi firma."

    )

    await context.bot.send_message(chat_id=user.id, text=text)


from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_autotraining_livello_5_handler(update, context):

    user = update.effective_user

    text = (

        "🧘 *Autotraining & Meditazione – Livello 5*\n\n"

        "Meditazione avanzata: esercizi audio, tecniche di rilassamento profondo e reset emotivo prima dei grandi eventi."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")

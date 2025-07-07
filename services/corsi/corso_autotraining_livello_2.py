from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_autotraining_livello_2_handler(update, context):

    user = update.effective_user

    text = (

        "🧘 *Autotraining & Meditazione – Livello 2*\n\n"

        "Meditazione guidata breve: elimina lo stress, trova la calma interiore, esercizi audio per ricaricare le energie."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")

from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_mentalita_milionario_livello_1_handler(update, context):

    user = update.effective_user

    text = (

        "💎 *Mentalità del Milionario – Livello 1*\n\n"

        "Le basi della mentalità vincente: cos’è la mentalità del milionario, mindset aperto, pensare in grande fin dai primi passi."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")

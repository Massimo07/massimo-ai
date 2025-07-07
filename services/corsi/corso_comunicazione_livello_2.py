from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_comunicazione_livello_2_handler(update, context):

    user = update.effective_user

    text = (

        "🗣️ *Corso Comunicazione – Livello 2*\n\n"

        "Comunicazione assertiva, tecniche per essere chiaro ma mai aggressivo. Primi esercizi di role-play e feedback."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")

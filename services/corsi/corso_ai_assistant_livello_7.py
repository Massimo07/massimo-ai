from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_ai_assistant_livello_7_handler(update, context):

    user = update.effective_user

    text = (

        "🤖 *AI Assistant Master – Livello 7*\n\n"

        "Assistant ultra personalizzato, avatar AI, risposte proattive e predittive, coaching AI, voice multi-lingua."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")

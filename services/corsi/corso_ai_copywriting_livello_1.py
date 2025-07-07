from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_ai_copywriting_livello_1_handler(update, context):

    user = update.effective_user

    text = (

        "✍️ *AI Copywriting – Livello 1*\n\n"

        "Scrivi il tuo primo post social con l’AI: prompt base, struttura efficace, parole chiave."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")

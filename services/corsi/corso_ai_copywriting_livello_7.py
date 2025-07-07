from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_ai_copywriting_livello_7_handler(update, context):

    user = update.effective_user

    text = (

        "✍️ *AI Copywriting – Livello 7*\n\n"

        "Scrittura ultra-personalizzata, deep content automation, multi-lingua, brand voice AI, copywriting scalabile mondiale!"

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")

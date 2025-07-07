from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_ai_copywriting_livello_4_handler(update, context):

    user = update.effective_user

    text = (

        "✍️ *AI Copywriting – Livello 4*\n\n"

        "Email automation, gestione obiezioni con testi AI, script webinar, call-to-action persuasive."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")

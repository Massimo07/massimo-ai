from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_video_editing_livello_3_handler(update, context):

    user = update.effective_user

    text = (

        "🎬 *Video Editing – Livello 3*\n\n"

        "Montaggio avanzato: sovrapposizioni, voiceover, sottotitoli, effetti sonori, branding video personalizzato."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")

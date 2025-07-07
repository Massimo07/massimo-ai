from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_social_livello_2_handler(update, context):

    user = update.effective_user

    text = (

        "📱 *Corso Social Media – Livello 2*\n\n"

        "Creare contenuti efficaci: foto, video, storie, reel. Hashtag, orari di pubblicazione, coinvolgimento reale della community."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")

from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_gamification_livello_7_handler(update, context):

    user = update.effective_user

    text = (

        "🎯 *Gamification Master – Livello 7*\n\n"

        "Gamification AI-powered: badge generati da performance reali, premi digitali/physici automatici, community e tornei internazionali."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")

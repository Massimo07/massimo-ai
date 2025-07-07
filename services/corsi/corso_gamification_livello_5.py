from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_gamification_livello_5_handler(update, context):

    user = update.effective_user

    text = (

        "🎯 *Gamification – Livello 5*\n\n"

        "Sfide avanzate, team competition, blockchain badge, premi spendibili e progressi visibili nel profilo."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")

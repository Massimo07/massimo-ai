from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_leadership_livello_3_handler(update, context):

    user = update.effective_user

    text = (

        "👑 *Corso Leadership – Livello 3*\n\n"

        "Leadership situazionale, guida nei momenti di crisi, gestione delle aspettative e delle dinamiche di gruppo."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")

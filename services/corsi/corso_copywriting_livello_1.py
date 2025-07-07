from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_copywriting_livello_1_handler(update, context):

    user = update.effective_user

    text = (

        "✍️ *Copywriting Base – Livello 1*\n\n"

        "Impara le regole d’oro per scrivere post semplici e coinvolgenti. Esempi base per i tuoi primi contenuti Live On Plus."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")

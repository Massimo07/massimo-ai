from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_duplicazione_livello_4_handler(update, context):

    user = update.effective_user

    text = (

        "🔁 *Corso Duplicazione – Livello 4*\n\n"

        "Cos’è la duplicazione, come spiegarla al team, checklist per la prima duplicazione corretta, errori da evitare."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")

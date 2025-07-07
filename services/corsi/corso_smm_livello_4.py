from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_smm_livello_4_handler(update, context):

    user = update.effective_user

    text = (

        "📣 *Corso Social Media Manager – Livello 4*\n\n"

        "Gestione contenuti multi-canale: piano editoriale, programmazione post, rispondere ai commenti e prime automazioni base per risparmiare tempo."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")

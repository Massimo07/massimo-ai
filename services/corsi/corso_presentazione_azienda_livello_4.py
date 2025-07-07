from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_presentazione_azienda_livello_4_handler(update, context):

    user = update.effective_user

    text = (

        "🏢 *Corso Presentazione Azienda – Livello 4*\n\n"

        "Come raccontare Live On Plus in 3 minuti: elementi chiave, pdf, video brevi, rispondere alle domande più comuni in modo efficace."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")

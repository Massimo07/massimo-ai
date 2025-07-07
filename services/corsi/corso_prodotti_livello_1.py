from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_prodotti_livello_1_handler(update, context):

    user = update.effective_user

    text = (

        "📦 *Corso Prodotti – Livello 1*\n\n"

        "Scopri i prodotti principali Live On Plus, differenze tra categorie (skincare, make-up, integratori), come raccontarli con semplicità e sicurezza.\n"

        "Modulo 1: Cos’è un prodotto di qualità?\n"

        "Modulo 2: Come si consiglia un prodotto?\n"

        "Quiz pratico finale."

    )

    # Bottoni e flusso quiz

    # ...

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")

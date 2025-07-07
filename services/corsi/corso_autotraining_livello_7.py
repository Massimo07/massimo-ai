from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_autotraining_livello_7_handler(update, context):

    user = update.effective_user

    text = (

        "🧘 *Autotraining Master – Livello 7*\n\n"

        "Sessioni guidate da AI, meditazione personalizzata, esercizi di squadra, mindhacking e tecniche da top performer mondiali."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")

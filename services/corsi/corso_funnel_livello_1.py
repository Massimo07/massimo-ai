from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_funnel_livello_1_handler(update, context):

    user = update.effective_user

    text = (

        "🛒 *Funnel Marketing – Livello 1*\n\n"

        "Cos’è un funnel, come funziona e come puoi usarlo per i tuoi primi contatti Live On Plus."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")

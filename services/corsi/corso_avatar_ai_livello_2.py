from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_avatar_ai_livello_2_handler(update, context):

    user = update.effective_user

    text = (

        "🧑‍💻 *Avatar & Voice AI – Livello 2*\n\n"

        "Personalizza la voce AI, scegli tra maschile/femminile, lingua e tono. Registra il tuo messaggio di benvenuto personalizzato."

    )

    await context.bot.send_message(chat_id=user.id, text

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")

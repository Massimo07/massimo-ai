from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_social_livello_1_handler(update, context):

    user = update.effective_user

    text = (

        "📱 *Corso Social Media – Livello 1*\n\n"

        "Impara le basi per usare i social: Facebook, Instagram, WhatsApp.\n"

        "Modulo 1: Aprire e configurare un account\n"

        "Modulo 2: Pubblicare contenuti base\n"

        "Modulo 3: Le regole d’oro per non sbagliare."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")

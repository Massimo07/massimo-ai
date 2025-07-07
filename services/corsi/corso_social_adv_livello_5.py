from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_social_adv_livello_5_handler(update, context):

    user = update.effective_user

    text = (

        "📢 *Social Advertising – Livello 5*\n\n"

        "Campagne multilivello, pubblicità su Messenger, WhatsApp e Instagram Stories, automazioni risposte ADV."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")

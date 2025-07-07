from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_vr_training_livello_2_handler(update, context):

    user = update.effective_user

    text = (

        "🕶️ *VR Training – Livello 2*\n\n"

        "Esperienze VR guidate: tutorial, video a 360°, navigazione base tra le aree, uso di avatar digitali semplici."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")

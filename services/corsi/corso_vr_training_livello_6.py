from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_vr_training_livello_6_handler(update, context):

    user = update.effective_user

    text = (

        "🕶️ *VR Training – Livello 6*\n\n"

        "Simulazioni vendita-rete, formazione immersiva avanzata, tracciamento performance e feedback AI in VR."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")

from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_vr_training_livello_1_handler(update, context):

    user = update.effective_user

    text = (

        "🕶️ *VR Training – Livello 1*\n\n"

        "Cos’è la formazione immersiva? Scopri i primi ambienti virtuali Live On Plus e come esplorare uno stand virtuale."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")

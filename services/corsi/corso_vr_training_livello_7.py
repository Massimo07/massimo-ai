from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_vr_training_livello_7_handler(update, context):

    user = update.effective_user

    text = (

        "🕶️ *VR Training Master – Livello 7*\n\n"

        "Eventi virtuali mondiali, gamification in VR, formazione personalizzata AI e interazione con mentor avatar."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")

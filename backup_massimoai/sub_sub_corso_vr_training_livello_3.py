from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_vr_training_livello_3_handler(update, context):

    user = update.effective_user

    text = (

        "🕶️ *VR Training – Livello 3*\n\n"

        "Training interattivo, esercitazioni reali, quiz virtuali, feedback in tempo reale e certificazione base VR."

    )

    await context.bot.send_message(chat_id=user.id, text=text)


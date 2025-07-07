from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_gamification_livello_1_handler(update, context):

    user = update.effective_user

    text = (

        "🎯 *Gamification – Livello 1*\n\n"

        "Introduzione: che cos’è la gamification, badge, punti, piccoli premi e come aumentano la motivazione."

    )

    await context.bot.send_message(chat_id=user.id, text=text)


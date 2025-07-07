from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_gamification_livello_2_handler(update, context):

    user = update.effective_user

    text = (

        "🎯 *Gamification – Livello 2*\n\n"

        "Sfide tra team, prime leaderboard, badge virtuali Live On Plus e come condividerli sui social."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

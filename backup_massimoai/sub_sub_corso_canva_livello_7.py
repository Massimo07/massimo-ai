from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_canva_livello_7_handler(update, context):

    user = update.effective_user

    text = (

        "🎨 *Canva & Social Visual – Livello 7*\n\n"

        "Team Canva Enterprise: creazione asset, contenuti multilingua, automazione social, personal branding e produzione massiva AI!"

    )

    await context.bot.send_message(chat_id=user.id, text=text)


from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_canva_livello_5_handler(update, context):

    user = update.effective_user

    text = (

        "🎨 *Canva & Social Visual – Livello 5*\n\n"

        "Canva PRO: automazioni, strumenti di rimozione sfondo, creazione post ADV, collaborazione in team."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

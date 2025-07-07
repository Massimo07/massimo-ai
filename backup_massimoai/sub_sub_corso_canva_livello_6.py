from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_canva_livello_6_handler(update, context):

    user = update.effective_user

    text = (

        "🎨 *Canva & Social Visual – Livello 6*\n\n"

        "Design avanzato, uso AI Canva, automazione campagne ADV, export per tutte le piattaforme e gestione feedback clienti."

    )

    await context.bot.send_message(chat_id=user.id, text=text)


from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_canva_livello_1_handler(update, context):

    user = update.effective_user

    text = (

        "🎨 *Canva & Social Visual – Livello 1*\n\n"

        "Cos’è Canva, come si apre un template e si crea un post per i social in 2 minuti."

    )

    await context.bot.send_message(chat_id=user.id, text=text)


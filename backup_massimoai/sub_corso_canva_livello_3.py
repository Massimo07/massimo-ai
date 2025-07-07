from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_canva_livello_3_handler(update, context):

    user = update.effective_user

    text = (

        "🎨 *Canva & Social Visual – Livello 3*\n\n"

        "Crea caroselli e storie animate. Canva Video: editing veloce, aggiungi musica e loghi personalizzati."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

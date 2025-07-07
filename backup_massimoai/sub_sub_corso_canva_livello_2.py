from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_canva_livello_2_handler(update, context):

    user = update.effective_user

    text = (

        "🎨 *Canva & Social Visual – Livello 2*\n\n"

        "Personalizza font e colori, aggiungi foto e sticker, salva la grafica per Instagram."

    )

    await context.bot.send_message(chat_id=user.id, text=text)


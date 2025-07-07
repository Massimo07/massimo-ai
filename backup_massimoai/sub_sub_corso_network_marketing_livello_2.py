from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_network_marketing_livello_2_handler(update, context):

    user = update.effective_user

    text = (

        "🌐 *Corso Network Marketing – Livello 2*\n\n"

        "Approccio ai contatti: come presentare l’opportunità, spiegare vantaggi e piani in modo semplice. Evitare errori comuni."

    )

    await context.bot.send_message(chat_id=user.id, text=text)


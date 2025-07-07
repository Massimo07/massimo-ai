from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_notion_livello_2_handler(update, context):

    user = update.effective_user

    text = (

        "📒 *Notion – Livello 2*\n\n"

        "Crea database semplici, gestione progetti, calendari e task per la produttività."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

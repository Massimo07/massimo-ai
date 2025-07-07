from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_office_livello_6_handler(update, context):

    user = update.effective_user

    text = (

        "💻 *Microsoft Office – Livello 6*\n\n"

        "Word: collaborazione cloud, commenti smart. Excel: script, analisi dati AI. PowerPoint: video interattivi, plugin. Outlook: CRM integrato e automazioni avanzate."

    )

    await context.bot.send_message(chat_id=user.id, text=text)


from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_automation_livello_2_handler(update, context):

    user = update.effective_user

    text = (

        "🤖 *Automation Lab – Livello 2*\n\n"

        "Crea un flusso multi-app (es: salva file da Telegram a Google Drive automaticamente)."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async async async def corso_notion_livello_5_handler(update, context):

    user = update.effective_user

    text = (

        "📒 *Notion – Livello 5*\n\n"

        "Kanban avanzato, knowledge base di team, dashboard finanziarie, automazioni API base."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

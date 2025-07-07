from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_ai_video_livello_1_handler(update, context):

    user = update.effective_user

    text = (

        "🎥 *AI Video – Livello 1*\n\n"

        "Cos’è un video AI? Crea il tuo primo video con un template guidato e musica di sottofondo."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")

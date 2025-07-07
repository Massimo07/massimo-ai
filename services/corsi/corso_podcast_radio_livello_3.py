from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_podcast_radio_livello_3_handler(update, context):

    user = update.effective_user

    text = (

        "🎙️ *Podcast & Radio – Livello 3*\n\n"

        "Primi montaggi audio, musica di sottofondo, pubblicazione podcast base su piattaforme gratuite."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")

from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_copywriting_livello_3_handler(update, context):

    user = update.effective_user

    text = (

        "✍️ *Copywriting – Livello 3*\n\n"

        "Struttura un post di vendita perfetto. Crea headline, elenchi, testimonianze e usa l’empatia per connetterti col lettore."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")

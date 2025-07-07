from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_adobe_livello_6_handler(update, context):

    user = update.effective_user

    text = (

        "🖌️ *Adobe Suite – Livello 6*\n\n"

        "Photoshop: automazioni script. Illustrator: plugin avanzati. Canva: AI design. Premiere: editing AI, multicam. Acrobat: OCR, AI PDF."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")

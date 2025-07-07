from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
async def corso_presentazione_piano_livello_4_handler(update, context):

    user = update.effective_user

    text = (

        "💎 *Corso Presentazione Piano Marketing – Livello 4*\n\n"

        "Schemi, esempi visivi, le parole giuste per spiegare piano unilevel, bonus, royalty, differenze tra bonus e sconto, errori da evitare."

    )

    await context.bot.send_message(chat_id=user.id, text=text)

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")

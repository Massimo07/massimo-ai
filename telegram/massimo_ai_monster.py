import os
import threading
import asyncio
import nest_asyncio
from flask import Flask
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

# App Flask
app = Flask(__name__)

# Token Telegram (metti il tuo token nel .env o qui)
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN") or "INSERISCI_IL_TUO_TOKEN_TELEGRAM"

# Patch asyncio per evitare l'errore event loop già in esecuzione
nest_asyncio.apply()

# Funzione principale bot async
async def main_bot():
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    async def start(update, context):
        await update.message.reply_text("Ciao! Sono Massimo AI, il tuo assistente.")

    application.add_handler(CommandHandler("start", start))
    # Puoi aggiungere altri handler qui

    await application.run_polling(close_loop=False)

# Thread per far girare il bot Telegram
def run_bot_thread():
    asyncio.run(main_bot())

@app.route("/")
def home():
    return "Massimo AI Server è attivo e funzionante!"

if __name__ == "__main__":
    # Avvio bot in thread separato
    bot_thread = threading.Thread(target=run_bot_thread, daemon=True)
    bot_thread.start()

    # Avvio server Flask
    app.run(host="0.0.0.0", port=8000)

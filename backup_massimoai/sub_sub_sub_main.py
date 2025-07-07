import logging
import os
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from handlers import get_handlers

# Configura logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# Prendi il token dal file .env
from dotenv import load_dotenv
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

def main():
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    # Importa e aggiungi tutti gli handler
    handlers = get_handlers()
    for handler in handlers:
        application.add_handler(handler)

    print("🚀 MASSIMO AI (Telegram bot) AVVIATO, ora si vola!")
    application.run_polling()

if __name__ == "__main__":
    main()
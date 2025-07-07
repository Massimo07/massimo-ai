from telegram.ext import ContextTypes, ContextTypes
import os
import re

def patch_imports(base_dir):
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".py") and not file.startswith("venv"):
                path = os.path.join(root, file)
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()

                original = content

                # Patch import Filters -> filters
                content = re.sub(r"from telegram\.ext import Filters", "from telegram.ext import filters", content), ContextTypes
                content = re.sub(r"Filters\.", "filters.", content)

                # Patch relative utils import
                content = re.sub(r"from \.\.utils import get_user", "from utils import get_user", content)

                # Patch all-in-one old PTB imports
                content = re.sub(
                    r"from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackQueryHandler",, ContextTypes
                    "from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackQueryHandler",, ContextTypes
                    content
                )

                # Elimina tripli ritorni a capo
                content = re.sub(r"\n{3,}", "\n\n", content)

                if content != original:
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(content)
                    print(f"✅ Patchato: {path}")

def main():
    base_dir = os.getcwd()
    print(f"🔎 Patch massiva di tutti i file Python nella cartella: {base_dir}")
    patch_imports(base_dir)
    print("🚀 Patch automatica completata!")

if __name__ == "__main__":
    main()
async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")

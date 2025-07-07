from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import os

target_dir = "services"

for filename in os.listdir(target_dir):

    if filename.endswith(".py"):

        path = os.path.join(target_dir, filename)

        with open(path, "r", encoding="utf-8") as f:

            lines = f.readlines()

        changed = False

        new_lines = []

        for line in lines:

            # Correggi tutte le importazioni

            if "from utils import get_user" in line or "from utils import get_user" in line:

                new_lines.append("from utils import get_user\n")

                changed = True

            else:

                new_lines.append(line)



        if changed:

            with open(path, "w", encoding="utf-8") as f:

                f.writelines(new_lines)

            print(f"Patchato: {filename}")

print("Fatto! Ora tutti i servizi usano: from utils import get_user")

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")

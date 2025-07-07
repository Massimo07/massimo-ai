from telegram.ext import CommandHandler
from telegram.ext import ContextTypes, ContextTypes
import os

import re

def patch_file(path):

    try:

        with open(path, "r", encoding="utf-8") as f:

            text = f.read()

    except UnicodeDecodeError:

        print(f"⚠️  File NON in UTF-8: {path}")

        return

    # Rimuove l'import obsoleto

    text_new = re.sub(

        r"from telegram\.ext import (?:.*\b)?Filters\b(.*)",

        r"from telegram.ext import\1",

        text

    )

    # Aggiungi nuovo import se manca

    if "from telegram.ext import filters" not in text_new:, ContextTypes

        text_new = text_new.replace(

            "from telegram.ext import",

            "from telegram.ext import\nfilters,",

            1

        )

    # Sostituisci tutti i filters.X con filters.X (nuova sintassi)

    text_new = re.sub(r"Filters\.", "filters.", text_new)

    if text_new != text:

        with open(path, "w", encoding="utf-8") as f:

            f.write(text_new)

        print(f"✅ Patchato: {path}")

def patch_all_py(root):

    for dirpath, dirs, files in os.walk(root):

        for file in files:

            if file.endswith(".py"):

                patch_file(os.path.join(dirpath, file))

if __name__ == "__main__":

    patch_all_py(".")

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")

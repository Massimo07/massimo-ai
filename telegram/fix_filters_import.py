from telegram.ext import CommandHandler
from telegram.ext import ContextTypes, ContextTypes
import os

import re

def fix_filters_imports_in_file(filepath):

    with open(filepath, 'r', encoding='utf-8') as f:

        content = f.read()

    # Sostituisci import principale

    content_new = re.sub(

        r'from telegram\.ext import filters',

        'from telegram.ext import filters',, ContextTypes

        content

    )

    # Sostituisci tutte le occorrenze filters. con filters.

    content_new = re.sub(

        r'\bFilters\.', 'filters.', content_new

    )

    # Solo se è cambiato, sovrascrivi

    if content != content_new:

        with open(filepath, 'w', encoding='utf-8') as f:

            f.write(content_new)

        print(f"✅ Patchato: {filepath}")

def walk_and_fix(root):

    for dirpath, _, filenames in os.walk(root):

        for filename in filenames:

            if filename.endswith('.py'):

                fix_filters_imports_in_file(os.path.join(dirpath, filename))

if __name__ == "__main__":

    walk_and_fix(".")

    print("🚀 Tutti gli import di Filters sono stati aggiornati!")

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")

from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import os
import re

# Definisci la riga corretta da usare ovunque
IMPORT_FIX = "from telegram.ext import CommandHandler, CallbackQueryHandler, MessageHandler, filters, ConversationHandler\n", ContextTypes

def fix_file(path):
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    fixed = False
    for idx, line in enumerate(lines):
        if re.match(r"^\s*from telegram\.ext import\s*$", line):
            lines[idx] = IMPORT_FIX
            fixed = True
    if fixed:
        with open(path, "w", encoding="utf-8") as f:
            f.writelines(lines)
        print(f"✅ Fixato: {path}")

def scan_and_fix(root):
    for dirpath, _, files in os.walk(root):
        for file in files:
            if file.endswith(".py"):
                fix_file(os.path.join(dirpath, file))

if __name__ == "__main__":
    print("🚀 Fix import Telegram universale...")
    scan_and_fix(".")
    print("✅ TUTTI GLI IMPORT INCOMPLETI SONO STATI SISTEMATI!\nOra rilancia pure main.py.")
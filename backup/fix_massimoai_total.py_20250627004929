from telegram.ext import ContextTypes, ContextTypes
import os

import re

import codecs

SRC_DIR = os.path.dirname(os.path.abspath(__file__))

SERVICES_DIR = os.path.join(SRC_DIR, "services")

HANDLERS_FILE = os.path.join(SRC_DIR, "handlers.py")

def to_utf8(filename):

    try:

        with open(filename, 'rb') as f:

            raw = f.read()

        try:

            text = raw.decode('utf-8')

        except UnicodeDecodeError:

            text = raw.decode('latin-1')

        with open(filename, 'w', encoding='utf-8') as f:

            f.write(text)

        return True

    except Exception as e:

        print(f"❌ [UTF-8 FAIL] {filename}: {e}")

        return False

def fix_imports(text):

    # Fix telegram.ext imports

    text = re.sub(r'from telegram\.ext import filters', 'from telegram.ext import filters', text), ContextTypes

    text = re.sub(r'import filters', 'import filters', text)

    text = re.sub(r'Filters\.', 'filters.', text)

    # Fix other common broken import (es: CommandHandler senza Handler)

    text = re.sub(r'from telegram\.ext import(\s*)(\w+)([^,\n]*)$', r'from telegram.ext import \2\3', text, flags=re.MULTILINE), ContextTypes

    # Fix relative imports (from utils import) → (from utils import)

    text = re.sub(r'from\s+\.\.utils\s+import', 'from utils import', text)

    # Fix from services import X → from services import X

    text = re.sub(r'from\s+\.(services)', r'from \1', text)

    return text

def find_all_handlers():

    # Cerca tutti i file *_handler.py in services

    handler_files = [f for f in os.listdir(SERVICES_DIR) if f.endswith("_handler.py")]

    handler_names = [os.path.splitext(f)[0] for f in handler_files]

    return handler_files, handler_names

def generate_handlers_py(handler_names):

    lines = [

        "# handlers.py - AUTOGENERATO! Non modificare a mano.",

        "from telegram.ext import *",, ContextTypes

    ]

    for h in handler_names:

        lines.append(f"from services.{h} import {h}")

    lines.append("")

    lines.append("def get_handlers():")

    lines.append("    return [")

    for h in handler_names:

        lines.append(f"        {h},")

    lines.append("    ]")

    return "\n".join(lines)

def patch_all_py_files():

    print("🔧 Inizio patch di tutti i file .py...")

    for root, dirs, files in os.walk(SRC_DIR):

        for file in files:

            if file.endswith(".py"):

                path = os.path.join(root, file)

                to_utf8(path)

                with open(path, "r", encoding="utf-8") as f:

                    text = f.read()

                new_text = fix_imports(text)

                if new_text != text:

                    with open(path, "w", encoding="utf-8") as f:

                        f.write(new_text)

                    print(f"✅ Patchato: {file}")

def create_missing_handler_templates(handler_names):

    for h in handler_names:

        filename = os.path.join(SERVICES_DIR, h + ".py")

        if not os.path.exists(filename):

            with open(filename, "w", encoding="utf-8") as f:

                f.write(f"# {h}.py - handler placeholder\n\n{h} = None\n")

            print(f"🆕 Creato template handler: {h}.py")

if __name__ == "__main__":

    patch_all_py_files()

    handler_files, handler_names = find_all_handlers()

    print(f"📦 Handler trovati in services/: {handler_names}")

    create_missing_handler_templates(handler_names)

    # Rigenera handlers.py

    code = generate_handlers_py(handler_names)

    with open(HANDLERS_FILE, "w", encoding="utf-8") as f:

        f.write(code)

    print("🚀 handlers.py rigenerato con tutti gli handler trovati!")

    print("\n🔥 **FIX COMPLETO E AUTOMATICO TERMINATO!** 🔥")

    print("Prova ora a lanciare di nuovo main.py.")

    print("Se qualche handler non ti serve/elimina il file dal progetto.")

    print("Se hai nuovi servizi, basta ricreare un handler.py e rilanciare questo fix.")

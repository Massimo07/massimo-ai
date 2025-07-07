from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import importlib.util

import os

PLUGINS_PATH = "services/"

def list_plugins():

    return [

        f[:-3] for f in os.listdir(PLUGINS_PATH)

        if f.endswith(".py") and not f.startswith("_")

    ]

def load_plugin(plugin_name):

    try:

        module_path = os.path.join(PLUGINS_PATH, f"{plugin_name}.py")

        spec = importlib.util.spec_from_file_location(plugin_name, module_path)

        module = importlib.util.module_from_spec(spec)

        spec.loader.exec_module(module)

        return module

    except Exception as e:

        print(f"Errore caricamento plugin {plugin_name}: {e}")

        return None

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")

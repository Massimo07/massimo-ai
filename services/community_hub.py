from telegram.ext import CommandHandler
from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

# services/community_hub.py

async def invite_to_community(update, context, platform):

    links = {

        "telegram": "https://t.me/tuogruppo",

        "facebook": "https://www.facebook.com/groups/magicteamliveonplus",

        "whatsapp": "https://wa.me/123456789"

    }

    await await update.message.reply_text(f"Unisciti alla nostra community su {platform}: {links[platform]}")

async def catch_all(update, context):
    await update.message.reply_text("🙋‍♂️ Scrivi /start per cominciare oppure scegli una delle opzioni dal menu.")

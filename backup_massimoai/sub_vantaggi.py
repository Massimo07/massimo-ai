from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

from translations import t

async async def vantaggi_handler(update, context):

    user = update.effective_user if hasattr(update, "effective_user") else update.callback_query.from_user

    data = get_user(user.id)

    lang = data.get("lang", "it")

    await context.bot.send_photo(

        chat_id=user.id,

        photo=open("data/vantaggi_live_on_plus.jpg", "rb"),

        caption=t("vantaggi_msg", lang)

    )

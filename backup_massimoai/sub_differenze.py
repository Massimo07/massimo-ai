from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

from translations import t

async async async def differenze_handler(update, context):

    user = update.effective_user if hasattr(update, "effective_user") else update.callback_query.from_user

    data = get_user(user.id)

    lang = data.get("lang", "it")

    await context.bot.send_message(

        chat_id=user.id,

        text=t("differenze_msg", lang)

    )

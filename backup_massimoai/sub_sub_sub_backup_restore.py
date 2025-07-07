from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import shutil

def backup_users():

    shutil.copy("data/users.json", f"data/backup_users_{time.time()}.json")

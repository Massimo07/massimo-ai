from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

# services/auto_update.py

import os

import git

def auto_update_repo(repo_path, remote_url="origin"):

    try:

        repo = git.Repo(repo_path)

        repo.git.pull(remote_url)

        return True, "Aggiornamento completato!"

    except Exception as e:

        return False, f"Errore aggiornamento: {e}"


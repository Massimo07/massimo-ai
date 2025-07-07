from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

# services/esporta_utenti_liveonplus.py

import csv

def export_users_to_csv(users, filename="utenti_liveonplus.csv"):

    fieldnames = users[0].keys()

    with open(filename, "w", newline='', encoding='utf-8') as csvfile:

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for user in users:

            writer.writerow(user)


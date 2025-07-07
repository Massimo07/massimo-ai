from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

# services/webhook_manager.py

from flask import Flask, request

app = Flask(__name__)

@app.route("/webhook/stripe", methods=["POST"])

def stripe_webhook():

    payload = request.data

    # Elabora evento Stripe, aggiorna abbonamenti

    # ...

    return "OK", 200

from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

import openai

import os

OPENAI_KEY = os.getenv("OPENAI_API_KEY")

def ask_openai(prompt, model="gpt-4o", temp=0.7, max_tokens=400):

    try:

        openai.api_key = OPENAI_KEY

        response = openai.ChatCompletion.create(

            model=model,

            messages=[{"role": "user", "content": prompt}],

            temperature=temp,

            max_tokens=max_tokens

        )

        return response['choices'][0]['message']['content'].strip()

    except Exception as e:

        print("Errore OpenAI:", e)

        return f"Errore AI: {e}"

import os
from dotenv import load_dotenv

load_dotenv()

def get_secret(name: str, default=None):
    return os.getenv(name, default)

from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_user

# services/plugin_loader.py

def load_plugin(plugin_name):

    try:

        module = __import__(f"services.plugins.{plugin_name}", fromlist=[''])

        return module

    except ImportError:

        return None

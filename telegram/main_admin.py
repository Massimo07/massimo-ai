import logging
from telegram.ext import ApplicationBuilder
from admin_tools import get_admin_handlers  # Handler dedicati admin
from utils import load_all_users, save_all_users

if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )
    app = ApplicationBuilder().token("INSERISCI_TOKEN_ADMIN").build()
    
    load_all_users()
    
    # Handler solo per funzioni admin (stats, export, dashboard, ecc.)
    for handler in get_admin_handlers():
        app.add_handler(handler)
    
    print("Massimo AI (Admin) dashboard ON AIR! 👑")
    app.run_polling()
    
    save_all_users()

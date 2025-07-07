# -*- coding: utf-8 -*-
"""
Modulo: handlers.py
Contiene tutti gli handler per i comandi e i messaggi del bot Telegram.
"""

import logging
from telegram.ext import CommandHandler, MessageHandler, filters
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode
import json # Necessario per caricare le categorie dal DB se sono salvate come JSON o per gestire i metadati

# Importa le funzioni dal servizio OpenAI
# Assicurati che openai_service.py sia aggiornato e che `conn` sia accessibile
from openai_service import get_openai_response, build_vector_store
from openai_service import conn as db_conn # Importa la connessione al database da openai_service

# Configurazione del logger per handlers.py (opzionale, main.py già lo configura)
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     level=logging.INFO
# )
# log = logging.getLogger("handlers")


# --- Funzioni per i comandi Telegram ---

async async async def start_command(update: Update, context):
    """Gestisce il comando /start."""
    await update.message.reply_text(
        "Benvenuto! Sono Massimo AI, il tuo assistente personale di Live On Plus. "
        "Posso darti informazioni sui prodotti, sul piano marketing e sulla crescita personale. "
        "Come posso aiutarti oggi?"
    )

async async async def help_command(update: Update, context):
    """Gestisce il comando /help."""
    await update.message.reply_text(
        "Ecco cosa posso fare:\n"
        "/start - Avvia la conversazione\n"
        "/help - Mostra questo messaggio di aiuto\n"
        "/prodotti - Visualizza le categorie di prodotti\n"
        "/marketing - Informazioni sul piano marketing\n"
        "Puoi anche chiedermi direttamente sui prodotti o sulla crescita personale!"
    )

async async async def products_command(update: Update, context):
    """Mostra le categorie dei prodotti con bottoni e immagini, leggendo dal database."""
    chat_id = update.effective_chat.id
    buttons = []
    temp_categories_display = []

    try:
        if db_conn:
            db_cursor_local = db_conn.cursor()
            db_cursor_local.execute("SELECT name, url, image_url FROM categories")
            categories_from_db = [{"name": r[0], "url": r[1], "image": r[2]} for r in db_cursor_local.fetchall()]
            
            if categories_from_db:
                temp_categories_display = categories_from_db
                logging.info(f"Caricate {len(categories_from_db)} categorie dal database.")
            else:
                logging.warning("Nessuna categoria trovata nel database 'categories'.")
                temp_categories_display = [{"name": "Categorie Non Disponibili", "url": "https://liveonplus.it/", "image": "https://placehold.co/250x250?text=N/D"}]
        else:
            logging.error("Connessione al database non disponibile in products_command.")
            temp_categories_display = [{"name": "Errore Connessione DB", "url": "https://liveonplus.it/", "image": "https://placehold.co/250x250?text=Errore"}]

    except Exception as e:
        logging.error(f"Errore durante il caricamento delle categorie dal DB per i bottoni: {e}", exc_info=True)
        temp_categories_display = [{"name": "Errore Caricamento Categorie", "url": "https://liveonplus.it/", "image": "https://placehold.co/250x250?text=Errore"}]

    for cat in temp_categories_display:
        buttons.append([InlineKeyboardButton(cat['name'], url=cat['url'])])
    
    reply_markup = InlineKeyboardMarkup(buttons)

    # Invia un messaggio con la lista di bottoni
    await context.bot.send_message(
        chat_id=chat_id,
        text="🔎 *Scopri tutte le categorie Live On Plus!*",
        reply_markup=reply_markup,
        parse_mode=ParseMode.MARKDOWN
    )

    # Invia le immagini categoria per categoria (facoltativo, può essere molto verboso)
    for cat in temp_categories_display:
        try:
            # Controllo URL validità per evitare errori di Telegram
            if cat['image'] and (cat['image'].startswith('http://') or cat['image'].startswith('https://')):
                await context.bot.send_photo(
                    chat_id=chat_id,
                    photo=cat['image'],
                    caption=f"*{cat['name']}*\n[Apri catalogo]({cat['url']})",
                    parse_mode=ParseMode.MARKDOWN
                )
            else:
                logging.warning(f"URL immagine non valido per la categoria {cat['name']}: {cat['image']}. Invio solo testo.")
                await context.bot.send_message(
                    chat_id=chat_id,
                    text=f"*{cat['name']}*\n[Apri catalogo]({cat['url']})",
                    parse_mode=ParseMode.MARKDOWN
                )
        except Exception as e:
            logging.warning(f"Impossibile inviare l'immagine per la categoria {cat['name']} (URL: {cat.get('image', 'N/D')}): {e}. Invio solo testo.", exc_info=True)
            await context.bot.send_message(
                chat_id=chat_id,
                text=f"*{cat['name']}*\n[Apri catalogo]({cat['url']})",
                parse_mode=ParseMode.MARKDOWN
            )


async async async def marketing_command(update: Update, context):
    """Gestisce il comando /marketing."""
    await update.message.reply_text(
        "Il piano marketing di Live On Plus offre diverse opportunità. "
        "Sei interessato a diventare un 'Customer', 'Junior', 'Visor', 'Super Visor', o 'Ambassador'? "
        "Posso darti più dettagli su ciascun livello e sui relativi bonus."
    )

async async async def handle_message(update: Update, context):
    """Gestisce tutti i messaggi testuali non comandi."""
    user_message = update.message.text
    if user_message:
        logging.info(f"Messaggio ricevuto dall'utente: {user_message}")
        ai_response = get_openai_response(user_message)
        await update.message.reply_text(ai_response, parse_mode=ParseMode.MARKDOWN)
    else:
        await update.message.reply_text("Ho ricevuto un messaggio non testuale. Puoi scrivermi solo testo.")

def get_handlers():
    """
    Ritorna una lista di tutti gli handler per l'ApplicationBuilder del bot.
    """
    return [
        CommandHandler("start", start_command),
        CommandHandler("help", help_command),
        CommandHandler("prodotti", products_command),
        CommandHandler("marketing", marketing_command),
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message),
    ]


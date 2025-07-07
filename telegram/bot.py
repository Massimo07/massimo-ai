#!/usr/bin/env python3
import os
import threading
import logging
import csv
import sqlite3
from io import BytesIO
from datetime import datetime

from flask import Flask, request, abort
import stripe
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Update,
    InputFile
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters,
    ContextTypes
)
import openai
# rimuovere TTS per compatibilità senza gtts
# from gtts import gTTS
from apscheduler.schedulers.background import BackgroundScheduler

# --- CONFIGURAZIONE LOG ---
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# --- VARIABILI D'AMBIENTE ---
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")
STRIPE_WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET")
SUCCESS_URL = os.getenv("SUCCESS_URL")
CANCEL_URL = os.getenv("CANCEL_URL")
openai.api_key = os.getenv("OPENAI_API_KEY")

required = {
    'TELEGRAM_TOKEN': TELEGRAM_TOKEN,
    'STRIPE_SECRET_KEY': STRIPE_SECRET_KEY,
    'STRIPE_WEBHOOK_SECRET': STRIPE_WEBHOOK_SECRET,
    'SUCCESS_URL': SUCCESS_URL,
    'CANCEL_URL': CANCEL_URL,
    'OPENAI_API_KEY': openai.api_key
}
missing = [k for k,v in required.items() if not v]
if missing:
    logger.error(f"Mancano variabili ambiente: {', '.join(missing)}")
    exit(1)

stripe.api_key = STRIPE_SECRET_KEY

# --- DATABASE SETUP ---
DB_PATH = os.path.join(os.path.dirname(__file__), 'massimo_ai.db')
conn = sqlite3.connect(DB_PATH, check_same_thread=False)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users (
    chat_id INTEGER PRIMARY KEY,
    level INTEGER DEFAULT 0,
    registered INTEGER DEFAULT 0,
    sponsor TEXT,
    email TEXT,
    referral_link TEXT,
    registration_date TEXT,
    last_level_update TEXT,
    points INTEGER DEFAULT 0
)''')
c.execute('''CREATE TABLE IF NOT EXISTS badges (
    chat_id INTEGER,
    badge TEXT,
    date_earned TEXT,
    PRIMARY KEY(chat_id, badge)
)''')
conn.commit()

# --- LOAD PRODUCTS & LEVELS ---
PRODUCTS = []
products_csv = os.path.join(os.path.dirname(__file__), 'products.csv')
if os.path.isfile(products_csv):
    with open(products_csv, newline='', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            if row.get('id') and row.get('price_id'):
                PRODUCTS.append(row)
else:
    logger.warning("products.csv non trovato")

LEVELS = {int(p['id']): p['price_id'] for p in PRODUCTS}
logger.info(f"Livelli caricati: {list(LEVELS.keys())}")

# --- LOAD SPONSORS ---
SPONSORS = []
sponsors_csv = os.path.join(os.path.dirname(__file__), 'sponsors.csv')
if os.path.isfile(sponsors_csv):
    with open(sponsors_csv, newline='', encoding='utf-8') as f:
        SPONSORS = list(csv.DictReader(f))
else:
    logger.warning("sponsors.csv non trovato")

# --- FLASK APP ---
app_web = Flask(__name__)

@app_web.route('/stripe-webhook', methods=['POST'])
def stripe_webhook():
    payload = request.get_data()
    sig = request.headers.get('Stripe-Signature', '')
    try:
        event = stripe.Webhook.construct_event(payload, sig, STRIPE_WEBHOOK_SECRET)
    except Exception as e:
        logger.error(f"Webhook error: {e}")
        abort(400)
    if event['type'] == 'checkout.session.completed':
        sess = event['data']['object']
        cid = int(sess['metadata']['chat_id'])
        lvl = int(sess['metadata']['level_id'])
        now = datetime.now().isoformat()
        c.execute("REPLACE INTO users(chat_id, level, registered, last_level_update) VALUES(?,?,1,?)", (cid, lvl, now))
        conn.commit()
        name = next((p['name'] for p in PRODUCTS if int(p['id'])==lvl), f"Livello {lvl}")
        bot_instance.send_message(cid, f"🎉 Hai sbloccato *{name}*! Accedi qui: {SUCCESS_URL}", parse_mode='Markdown')
    return '',200

def run_flask():
    app_web.run(host='0.0.0.0', port=int(os.getenv('PORT',5000)), debug=False)

# --- HELPERS ---
def build_menu(buttons, cols, header=None, footer=None):
    menu = [buttons[i:i+cols] for i in range(0,len(buttons),cols)]
    if header: menu.insert(0, header)
    if footer: menu.append(footer)
    return InlineKeyboardMarkup(menu)

def ensure_user(chat_id):
    c.execute("INSERT OR IGNORE INTO users(chat_id, registration_date) VALUES(?,?)", (chat_id, datetime.now().isoformat()))
    conn.commit()

# --- TELEGRAM HANDLERS ---
async def greet_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cid = update.effective_chat.id
    ensure_user(cid)
    user = c.execute("SELECT level, registered FROM users WHERE chat_id=?", (cid,)).fetchone()
    level = user[0] if user else 0
    name = next((p['name'] for p in PRODUCTS if int(p['id'])==level), 'Info Free')
    text = f"👋 Benvenuto! Livello: *{name}*"
    opts = [
        InlineKeyboardButton('🆓 Info Free', callback_data='info_free'),
        InlineKeyboardButton('📋 FAQ', callback_data='faq'),
        InlineKeyboardButton('📈 Piano Marketing', callback_data='plan_marketing'),
        InlineKeyboardButton('🛒 Prodotti', callback_data='products'),
        InlineKeyboardButton('🤝 Sponsor', callback_data='sponsors'),
        InlineKeyboardButton('➕ Registrati', callback_data='register')
    ]
    await context.bot.send_message(cid, text, parse_mode='Markdown', reply_markup=build_menu(opts,2))

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await greet_user(update, context)

async def register_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query; await q.answer()
    cid = q.message.chat.id
    c.execute("UPDATE users SET registered=1 WHERE chat_id=?", (cid,))
    conn.commit()
    await q.message.reply_text('Registrazione completata! Ora puoi acquistare abbonamenti.')

async def info_free(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query; await q.answer()
    path = os.path.join(os.path.dirname(__file__), 'info_free.md')
    text = open(path).read() if os.path.isfile(path) else 'Nessuna info disponibile.'
    await q.message.reply_text(text, parse_mode='Markdown')

async def products(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q=update.callback_query; await q.answer()
    buttons=[]; text='*Catalogo Prodotti*\n'
    for p in PRODUCTS:
        text+=f"- {p['name']}: {p.get('price','')}€\n"
        if p.get('url'): buttons.append([InlineKeyboardButton('Acquista', url=p['url'])])
    buttons.append([InlineKeyboardButton('🔙 Indietro', callback_data='start')])
    await q.message.reply_text(text, parse_mode='Markdown', reply_markup=InlineKeyboardMarkup(buttons))

async def sponsors(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q=update.callback_query; await q.answer()
    text='*Sponsor Disponibili*\n'
    for s in SPONSORS:
        text+=f"- {s.get('name','')} ({s.get('province','')})\n"
    await q.message.reply_text(text, parse_mode='Markdown')

import json
async def load_faq():
    path=os.path.join(os.path.dirname(__file__), 'faq.json')
    return json.load(open(path)) if os.path.isfile(path) else []

async def faq(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q=update.callback_query; await q.answer()
    faq_list = await load_faq()
    text='*FAQ*\n'
    for f in faq_list: text+=f"*{f['q']}*\n{f['a']}\n\n"
    await q.message.reply_text(text, parse_mode='Markdown')

async def plan_marketing(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q=update.callback_query; await q.answer()
    pages=open(os.path.join(os.path.dirname(__file__),'marketing_plan.md')).read().split('---PAGE---')
    context.user_data['pages']=pages; context.user_data['page']=0
    btns=[InlineKeyboardButton('◀️',callback_data='prev'),InlineKeyboardButton('▶️',callback_data='next')]
    await q.message.reply_text(pages[0], parse_mode='Markdown', reply_markup=build_menu(btns,2))

async def next_page(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q=update.callback_query; await q.answer()
    pages=context.user_data['pages']; idx=min(context.user_data['page']+1,len(pages)-1)
    context.user_data['page']=idx; await q.message.edit_text(pages[idx],parse_mode='Markdown',reply_markup=q.message.reply_markup)

async def prev_page(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q=update.callback_query; await q.answer()
    pages=context.user_data['pages']; idx=max(context.user_data['page']-1,0)
    context.user_data['page']=idx; await q.message.edit_text(pages[idx],parse_mode='Markdown',reply_markup=q.message.reply_markup)

async def quiz_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q=update.callback_query; await q.answer()
    text='Regola 60/40:?' ; opts=[InlineKeyboardButton('60% Shop1',callback_data='quiz_1'),InlineKeyboardButton('60% Spillover',callback_data='quiz_0')]
    await q.message.reply_text(text,reply_markup=build_menu(opts,2))

async def quiz_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q=update.callback_query; await q.answer()
    if q.data=='quiz_1': await q.message.reply_text('Corretto! Usa /subscribe');
    else: await q.message.reply_text('Errato, riprova.')

async def buy_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message or update.callback_query.message
    opts=[]
    for lvl, pid in LEVELS.items(): opts.append(InlineKeyboardButton(f"Livello {lvl}",callback_data=f"buy_{lvl}"))
    await msg.reply_text('Seleziona livello:',reply_markup=build_menu(opts,2))

async def buy_level(update: Update, context: ContextTypes.DEFAULT_TYPE):
    q=update.callback_query; await q.answer(); cid=q.message.chat.id; lvl=int(q.data.split('_')[1])
    pid=LEVELS[lvl]
    sess=stripe.checkout.Session.create(
        payment_method_types=['card'], line_items=[{'price':pid,'quantity':1}],
        mode='subscription', success_url=SUCCESS_URL, cancel_url=CANCEL_URL,
        metadata={'chat_id':cid,'level_id':lvl}
    )
    await q.message.reply_text(f"Paga qui: {sess.url}")

async def ai_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt=update.message.text
    await update.message.reply_text('Elaboro...')
    resp=openai.ChatCompletion.create(model='gpt-4o-mini',messages=[{'role':'user','content':prompt}])
    txt=resp.choices[0].message.content; await update.message.reply_text(txt)

# --- REMINDER SCHEDULER ---
sched = BackgroundScheduler()
sched.add_job(lambda: [application.bot.send_message(u[0],'Ricorda il piano!',parse_mode='Markdown') for u in c.execute('SELECT chat_id FROM users WHERE registered=1')], 'interval', hours=24)

# --- MAIN ---
if __name__=='__main__':
    threading.Thread(target=run_flask,daemon=True).start()
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    global bot_instance; bot_instance = application.bot
    # Register
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(register_handler, pattern='^register$'))
    application.add_handler(CallbackQueryHandler(info_free, pattern='^info_free$'))
    application.add_handler(CallbackQueryHandler(faq, pattern='^faq$'))
    application.add_handler(CallbackQueryHandler(plan_marketing, pattern='^plan_marketing$'))
    application.add_handler(CallbackQueryHandler(next_page, pattern='^next$'))
    application.add_handler(CallbackQueryHandler(prev_page, pattern='^prev$'))
    application.add_handler(CallbackQueryHandler(quiz_start, pattern='^quiz_start$'))
    application.add_handler(CallbackQueryHandler(quiz_answer, pattern='^quiz_1$'))
    application.add_handler(CommandHandler('subscribe', buy_menu))
    application.add_handler(CallbackQueryHandler(buy_level, pattern=r'^buy_\d+$'))
    application.add_handler(CallbackQueryHandler(products, pattern='^products$'))
    application.add_handler(CallbackQueryHandler(sponsors, pattern='^sponsors$'))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, ai_handler))
    sched.start()
    application.run_polling()

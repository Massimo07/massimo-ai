from telegram.ext import CommandHandler, MessageHandler, CallbackQueryHandler, filters, ConversationHandler
from services.onboarding import start_handler, onboarding_handler, choose_language_handler
from services.network_marketing import network_marketing_handler
from services.liveonplus import liveonplus_handler
from services.piano_marketing import piano_marketing_handler
from services.differenze_ruoli import differenze_ruoli_handler
from services.perche_lop import perche_lop_handler
from services.perche_magicteam import perche_magicteam_handler
from services.faq import faq_handler
from services.motivazione import motivazione_handler
from services.prodotti_cataloghi import prodotti_cataloghi_handler
from services.registrati import registrati_handler
from services.sei_indeciso import sei_indeciso_handler
from services.momento_no import momento_no_handler
from services.scarica_libro import scarica_libro_handler
from services.eventi_webinar import eventi_webinar_handler
from services.news import news_handler
from services.vendere_autoconsumo import vendere_autoconsumo_handler
from services.abbonati import abbonati_handler
from services.corsi_vendita import corsi_vendita_menu_handler, corso_vendita_step_handler
from utils import fallback_handler

def get_handlers():
    return [
        CommandHandler("start", start_handler),
        CallbackQueryHandler(choose_language_handler, pattern="^lang_"),
        CallbackQueryHandler(network_marketing_handler, pattern="^network_marketing$"),
        CallbackQueryHandler(liveonplus_handler, pattern="^liveonplus$"),
        CallbackQueryHandler(piano_marketing_handler, pattern="^piano_marketing$"),
        CallbackQueryHandler(differenze_ruoli_handler, pattern="^differenze_ruoli$"),
        CallbackQueryHandler(perche_lop_handler, pattern="^perche_lop$"),
        CallbackQueryHandler(perche_magicteam_handler, pattern="^perche_magicteam$"),
        CallbackQueryHandler(faq_handler, pattern="^faq$"),
        CallbackQueryHandler(motivazione_handler, pattern="^motivazione$"),
        CallbackQueryHandler(prodotti_cataloghi_handler, pattern="^prodotti_cataloghi$"),
        CallbackQueryHandler(registrati_handler, pattern="^registrati$"),
        CallbackQueryHandler(sei_indeciso_handler, pattern="^sei_indeciso$"),
        CallbackQueryHandler(momento_no_handler, pattern="^momento_no$"),
        CallbackQueryHandler(scarica_libro_handler, pattern="^scarica_libro$"),
        CallbackQueryHandler(eventi_webinar_handler, pattern="^eventi_webinar$"),
        CallbackQueryHandler(news_handler, pattern="^news$"),
        CallbackQueryHandler(vendere_autoconsumo_handler, pattern="^vendere_autoconsumo$"),
        CallbackQueryHandler(abbonati_handler, pattern="^abbonati$"),
        CallbackQueryHandler(corsi_vendita_menu_handler, pattern="^corsi_vendita_menu$"),
        CallbackQueryHandler(corso_vendita_step_handler, pattern="^corso_vendita_step_"),
        MessageHandler(filters.ALL, fallback_handler)
    ]

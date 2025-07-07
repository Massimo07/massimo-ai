from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

MAIN_MENU_BUTTONS = [
    ["🏢 Presentazione aziendale", "💎 Presentazione piano marketing"],
    ["CHE VANTAGGI OFFRE LIVE ON PLUS", "🌟 Perché scegliere il Magic Team"],
    ["📚 Cataloghi prodotti", "🧴 Ti consiglio il prodotto adatto a te"],
    ["❓ Domande Frequenti (FAQ)", "🙋‍♂️ Hai bisogno di aiuto? PARLIAMONE"],
    ["🛒 Vuoi fare vendita?", "🌐 Vuoi fare rete?", "🏷 Vuoi fare autoconsumo?"],
    ["📖 Un libro per la tua crescita personale e professionale", "🔑 🏆 Testimonianze vere"],
    ["📞 Contatta il tuo sponsor", "🚀 Motivazione del giorno"],
    ["🎧 Radio M AI", "🔄 Cambia lingua", "🔗 Invita un amico"],
    ["E ORA… PREPARATI… SI ENTRA NEL FUTURO"],
    ["🏠 Home", "🔙 Indietro"]
]

async def show_main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = ReplyKeyboardMarkup(MAIN_MENU_BUTTONS, resize_keyboard=True)
    await update.message.reply_text(
        "Benvenuto in Massimo AI!
Seleziona una funzione dal menu:",
        reply_markup=keyboard
    )

from telegram.ext import CommandHandler

def notifications_command(update, context):
    # Logica base: invio di una notifica simulata
    update.message.reply_text(
        "🔔 Notifiche Massimo AI\n"
        "Presto riceverai tutte le notifiche importanti (promo, eventi, scadenze) direttamente qui!\n"
        "La funzione notifiche sarà attiva a breve. Rimani aggiornato!"
    )

notifications_handler = CommandHandler("notifiche", notifications_command)

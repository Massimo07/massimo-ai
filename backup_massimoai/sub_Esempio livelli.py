from telegram.ext import filters, ContextTypes
from telegram.ext import ContextTypes, ContextTypes
LEVELS = [

    {

        "nome": "Info Free",

        "desc": "Solo informazioni base, motivazione, cataloghi.",

        "servizi": [

            "faq", "prodotti", "motivazione", "registrazione", "magic_team", "live_on_plus", "piano_marketing", "differenze", "vantaggi", "indeciso", "momento_no", "book", "eventi", "news", "dashboard"

        ]

    },

    {

        "nome": "Primo Passo",

        "desc": "Tutti i servizi precedenti + corso base di vendita, quiz.",

        "servizi": [

            "faq", "prodotti", "motivazione", "registrazione", "magic_team", "live_on_plus", "piano_marketing", "differenze", "vantaggi", "indeciso", "momento_no", "book", "eventi", "news", "dashboard",

            "corsi_base"

        ]

    },

    {

        "nome": "Cambio Vita",

        "desc": "Tutti i servizi precedenti + corso crescita personale, funnel.",

        "servizi": [

            "faq", "prodotti", "motivazione", "registrazione", "magic_team", "live_on_plus", "piano_marketing", "differenze", "vantaggi", "indeciso", "momento_no", "book", "eventi", "news", "dashboard",

            "corsi_base", "corsi_crescita_personale", "funnel"

        ]

    },

    # ...e così via per tutti i livelli!

]

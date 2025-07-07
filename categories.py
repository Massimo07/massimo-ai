# categories.py

CATEGORIES = [
    {
        "name": "Profumi Uomo",
        "url": "https://liveonplus.it/index.php?route=product/category&path=99_100",
        "image": "https://liveonplus.it/image/cache/catalog/CATEGORIE/MAN-250x250.jpg"
    },
    {
        "name": "Profumi Donna",
        "url": "https://liveonplus.it/index.php?route=product/category&path=99_101",
        "image": "https://liveonplus.it/image/cache/catalog/CATEGORIE/WOMAN-250x250.jpg"
    },
    {
        "name": "Profumi Niche",
        "url": "https://liveonplus.it/index.php?route=product/category&path=99_107",
        "image": "https://liveonplus.it/image/cache/catalog/CATEGORIE/NICHES-250x250.jpg"
    },
    {
        "name": "Profumatori Casa",
        "url": "https://liveonplus.it/index.php?route=product/category&path=229",
        "image": "https://liveonplus.it/image/cache/catalog/CATEGORIE/PROFUMATORI-CASA-250x250.jpg"
    },
    {
        "name": "Cura Corpo - Nuova Skin",
        "url": "https://liveonplus.it/index.php?route=product/category&path=126",
        "image": "https://liveonplus.it/image/cache/catalog/CATEGORIE/NUOVA-SKIN-250x250.jpg"
    },
    {
        "name": "Cura Capelli",
        "url": "https://liveonplus.it/index.php?route=product/category&path=156",
        "image": "https://liveonplus.it/image/cache/catalog/CATEGORIE/NUOVA-SKIN-CAPELLI-250x250.jpg"
    },
    {
        "name": "Make Up - Mycos",
        "url": "https://liveonplus.it/index.php?route=product/category&path=183",
        "image": "https://liveonplus.it/image/cache/catalog/CATEGORIE/MYCOS-MAKEUP-250x250.jpg"
    },
    {
        "name": "Make Up Exclusive - Elite",
        "url": "https://liveonplus.it/index.php?route=product/category&path=243",
        "image": "https://liveonplus.it/image/cache/catalog/CATEGORIE/ELITE-MAKEUP-250x250.jpg"
    },
    {
        "name": "Detergenza Casa - Luccica",
        "url": "https://liveonplus.it/index.php?route=product/category&path=120",
        "image": "https://liveonplus.it/image/cache/catalog/CATEGORIE/LUCCICA-250x250.jpg"
    },
    {
        "name": "Integrazione Alimentare - Integrami",
        "url": "https://liveonplus.it/index.php?route=product/category&path=221",
        "image": "https://liveonplus.it/image/cache/catalog/CATEGORIE/INTEGRATORI-250x250.jpg"
    },
    {
        "name": "Store Plus",
        "url": "https://liveonplus.it/index.php?route=product/category&path=286",
        "image": "https://liveonplus.it/image/cache/catalog/CATEGORIE/STOREPLUS-250x250.jpg"
    },
    {
        "name": "Monodosi",
        "url": "https://liveonplus.it/index.php?route=product/category&path=92",
        "image": "https://liveonplus.it/image/cache/catalog/CATEGORIE/MONODOSI-250x250.jpg"
    },
    {
        "name": "Promozioni",
        "url": "https://liveonplus.it/index.php?route=product/category&path=275",
        "image": "https://liveonplus.it/image/cache/catalog/CATEGORIE/PROMOZIONI-250x250.jpg"
    }
]

def get_category_message(category_name):
    msg_dict = {
        "Profumi Uomo": "💎 *Profumi Uomo*: Fragranze intense, ispirate ai grandi classici della profumeria maschile. Scopri il carattere di ogni uomo nella collezione Peccati Olfattivi MAN.",
        "Profumi Donna": "🌸 *Profumi Donna*: Dedicati all’eleganza e alla personalità di ogni donna. Fragranze avvolgenti, floreali, sensuali: lasciati conquistare!",
        "Profumi Niche": "✨ *Niches*: Profumi di nicchia, per chi vuole distinguersi davvero. Concentrazione Extrait de Parfum, ispirazione artistica.",
        "Cura Corpo - Nuova Skin": "🧴 *Cura del Corpo*: Coccola la tua pelle con le formule avanzate Nuova Skin. Idratazione, elasticità e morbidezza a prova di carezza.",
        "Cura Capelli": "💇‍♂️ *Cura Capelli*: Shampoo, maschere e trattamenti professionali per una chioma sana, forte e brillante.",
        "Make Up - Mycos": "💄 *Make Up Mycos*: Esalta la tua bellezza naturale con i colori e le texture professionali Mycos.",
        "Make Up Exclusive - Elite": "🌟 *Make Up Elite*: Make up luxury per look esclusivi. Formula top, finish da passerella.",
        "Detergenza Casa - Luccica": "🏠 *Detergenza Casa*: Soluzioni smart ed efficaci per una casa sempre splendente.",
        "Profumatori Casa": "🏡 *Profumatori Casa*: Trasforma ogni ambiente con le migliori fragranze per la casa.",
        "Integrazione Alimentare - Integrami": "💊 *Integrazione*: Supporta il tuo benessere con integratori innovativi e naturali.",
        "Store Plus": "🛒 *Store Plus*: Le migliori offerte e novità Live On Plus in esclusiva!",
        "Monodosi": "🧪 *Monodosi*: Praticità, risparmio e massima efficacia in ogni dose.",
        "Promozioni": "🎁 *Promozioni*: Scopri tutte le offerte speciali riservate alla community!"
    }
    return msg_dict.get(category_name, "Scopri il meglio della categoria Live On Plus. Qualità, risultati, sicurezza garantiti!")

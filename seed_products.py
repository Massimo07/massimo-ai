# -*- coding: utf-8 -*-
import sqlite3
import json
from datetime import datetime

DB_PATH = "massimo.db"

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# CREA la tabella solo se non esiste già (schema aggiornato)
cur.execute("""
    CREATE TABLE IF NOT EXISTS products (
        url TEXT PRIMARY KEY,
        name TEXT,
        price TEXT,
        description TEXT,
        effects_ingredients TEXT,
        code TEXT,
        category TEXT,
        application_area TEXT,
        concerns TEXT,
        image_urls TEXT,
        availability TEXT,
        points TEXT,
        last_updated TEXT
    )
""")
conn.commit()

# Esempio di dati di seed (3 prodotti, puoi aggiungere tutti quelli che vuoi)
products = [
    {
        "url": "https://liveonplus.it/index.php?route=product/product&product_id=1001",
        "name": "Crema Viso Idratante Acido Ialuronico",
        "price": "29.90",
        "description": "Crema viso idratante intensiva con acido ialuronico. Ideale per pelle secca, dona elasticità e morbidezza.",
        "effects_ingredients": "Acido Ialuronico, Olio di Jojoba, Vitamina E",
        "code": "AI1001",
        "category": "Skincare Viso",
        "application_area": "face",
        "concerns": json.dumps(["hydration", "aging"]),
        "image_urls": json.dumps(["https://liveonplus.it/image/catalog/prodotti/ialuronico.jpg"]),
        "availability": "Disponibile",
        "points": "12",
        "last_updated": datetime.utcnow().isoformat()
    },
    {
        "url": "https://liveonplus.it/index.php?route=product/product&product_id=1002",
        "name": "Shampoo Nutriente Aloe Vera",
        "price": "16.90",
        "description": "Shampoo nutriente per capelli secchi e sfibrati. Con aloe vera e pantenolo.",
        "effects_ingredients": "Aloe Vera, Pantenolo, Olio di Argan",
        "code": "AL1002",
        "category": "Cura Capelli",
        "application_area": "hair",
        "concerns": json.dumps(["hydration", "hair_loss"]),
        "image_urls": json.dumps(["https://liveonplus.it/image/catalog/prodotti/shampoo-aloe.jpg"]),
        "availability": "Disponibile",
        "points": "8",
        "last_updated": datetime.utcnow().isoformat()
    },
    {
        "url": "https://liveonplus.it/index.php?route=product/product&product_id=1003",
        "name": "Profumo Peccati Olfattivi - Tentazione",
        "price": "39.90",
        "description": "Fragranza persistente e sensuale, note di vaniglia e legni preziosi. Eau de Parfum.",
        "effects_ingredients": "Vaniglia, Legni, Note Ambrate",
        "code": "PO1003",
        "category": "Profumi",
        "application_area": "perfume",
        "concerns": json.dumps([]),
        "image_urls": json.dumps(["https://liveonplus.it/image/catalog/prodotti/profumo-tentazione.jpg"]),
        "availability": "Disponibile",
        "points": "18",
        "last_updated": datetime.utcnow().isoformat()
    }
]

for product in products:
    cur.execute("""
        INSERT OR REPLACE INTO products (
            url, name, price, description, effects_ingredients, code, category, 
            application_area, concerns, image_urls, availability, points, last_updated
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        product['url'], product['name'], product['price'], product['description'],
        product['effects_ingredients'], product['code'], product['category'],
        product['application_area'], product['concerns'], product['image_urls'],
        product['availability'], product['points'], product['last_updated']
    ))

conn.commit()
print("Prodotti di esempio inseriti con successo!")
conn.close()

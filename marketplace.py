"""
Modulo: marketplace.py
Gestione dello shop Massimo AI: prodotti Live On Plus, offerte, bundle, referral, materiali promo.
Espandibile per eventi, servizi, prodotti digitali, offerte AI, skill marketplace.
"""

MARKETPLACE_PRODUCTS = [
    {
        "sku": "LONP-IALU",
        "name": "Acido Ialuronico",
        "desc": "Idratazione profonda, pelle giovane.",
        "price": 39,
        "category": "skincare"
    },
    {
        "sku": "LONP-BAVA",
        "name": "Bava di Lumaca",
        "desc": "Rigenera, illumina e cicatrizza.",
        "price": 45,
        "category": "skincare"
    },
    # Espandi con tutti i prodotti reali!
]

def get_product(sku):
    return next((p for p in MARKETPLACE_PRODUCTS if p["sku"] == sku), None)

def list_products(category=None):
    if category:
        return [p for p in MARKETPLACE_PRODUCTS if p["category"] == category]
    return MARKETPLACE_PRODUCTS

# --- ESEMPIO USO ---
if __name__ == "__main__":
    print(list_products())
    print(get_product("LONP-BAVA"))

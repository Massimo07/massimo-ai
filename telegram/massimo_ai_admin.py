import json

admin_data = {
    "superadmin": {
        "nome": "Massimo",
        "email": "massimo@liveonplus.it",
        "telegram_id": 123456789,
        "ruolo": "Founder"
    },
    "whitelist": [],
    "team": []
}
with open("massimo_ai/admin.json", "w", encoding="utf-8") as f:
    json.dump(admin_data, f, ensure_ascii=False, indent=2)
print("✅ File admin.json creato in massimo_ai/admin.json")

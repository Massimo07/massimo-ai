import json
from pathlib import Path

SERVIZI = [
    "🏢 Presentazione aziendale",
    "💎 Presentazione piano marketing",
    "CHE VANTAGGI OFFRE LIVE ON PLUS",
    "🌟 Perché scegliere il Magic Team",
    "📚 Cataloghi prodotti",
    "🧴 Ti consiglio il prodotto adatto a te",
    "❓ Domande Frequenti (FAQ)",
    "🙋‍♂️ Hai bisogno di aiuto? PARLIAMONE",
    "🛒 Vuoi fare vendita?",
    "🌐 Vuoi fare rete?",
    "🏷 Vuoi fare autoconsumo?",
    "📖 Un libro per la tua crescita personale e professionale",
    "🔑 🏆 Testimonianze vere",
    "📞 Contatta il tuo sponsor",
    "🚀 Motivazione del giorno",
    "🎧 Radio M AI",
    "🔄 Cambia lingua",
    "🔗 Invita un amico",
    "E ORA… PREPARATI… SI ENTRA NEL FUTURO"
]

def main():
    base = Path("massimo_ai")
    for folder in base.iterdir():
        if folder.is_dir() and "servizi.json" in [f.name for f in folder.iterdir()]:
            (folder / "servizi.json").write_text(json.dumps(SERVIZI, ensure_ascii=False, indent=2), encoding="utf-8")
            print(f"✅ Servizi aggiunti a {folder}")

if __name__ == "__main__":
    main()

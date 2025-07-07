# CONFIG – Cartella configurazioni avanzate

Qui trovi tutte le configurazioni per ambienti diversi:
- **base.yaml** – Configurazione standard
- **dev.yaml** – Sviluppo locale
- **prod.yaml** – Produzione (pronta per deploy)
- **test.yaml** – Testing automatizzato

**Come si usano?**
- Il backend carica il file giusto in base a una variabile ambiente (es. `ENV=dev`)
- Si può estendere la classe `Config` per caricare YAML/JSON in automatico

**Sicurezza:**  
Non caricare MAI `secrets.json` o chiavi sensibili nel repository pubblico.

**Personalizzazione:**  
Puoi aggiungere file per clienti, white-label, verticali diversi, moduli extra.

---

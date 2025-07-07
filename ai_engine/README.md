# AI_ENGINE – Massimo AI

Motore centrale per orchestrazione, pipeline, explainability, plugin e fallback AI.
- Routing automatico tra modelli (GPT, Claude, custom)
- Plug-in system: aggiungi o rimuovi modelli a runtime
- Explainability: traccia motivazione scelta, log, fallback
- Logging dedicato, audit, batch, test demo-ready
- Auto-discovery: aggiungi nuove AI “al volo” senza cambiare codice

---

## Esempio uso rapido

```python
from ai_engine.pipeline import predict

input_data = {"prompt": "Ciao, dammi 3 motivi per usare Massimo AI!"}
risultato = predict(input_data, model_name="gpt-4o")
print("Risultato:", risultato)

"""
Modulo: ai_decision_assistant.py
Decision AI: aiuta nelle scelte (business/personali), valuta opzioni, pro/contro, suggerisce step pratici, fa brainstorming live col team.
"""

def assist_decision(options):
    # options = [{"name":"A", "pro":"veloce", "con":"rischiosa"}, ...]
    if not options:
        return "Nessuna opzione inserita."
    suggestion = max(options, key=lambda x: len(x.get("pro", "")))
    pros = suggestion["pro"]
    cons = suggestion.get("con", "")
    return f"Consigliata: {suggestion['name']} — Pro: {pros} — Attento a: {cons}"

# --- ESEMPIO USO ---
if __name__ == "__main__":
    print(assist_decision([
        {"name": "Investire in social", "pro": "Visibilità immediata", "con": "Costi alti"},
        {"name": "Referral marketing", "pro": "Crescita esponenziale", "con": "Serve tempo"}
    ]))

"""
Modulo: cross_network_analyzer.py
Analizza dati da più team/reti/paesi: confronto KPI, insight, suggerimenti, alert opportunità. Pronto per espansione internazionale.
"""

def compare_teams(teams):
    # teams = [{"nome": "Team1", "pv": 25000, "members": 300}, ...]
    best = max(teams, key=lambda t: t["pv"])
    for t in teams:
        print(f"{t['nome']}: {t['pv']} PV — {t['members']} membri")
    print(f"Il team più forte: {best['nome']}")

# --- ESEMPIO USO ---
if __name__ == "__main__":
    squadre = [
        {"nome": "Magic Team", "pv": 27000, "members": 320},
        {"nome": "Dream Team", "pv": 18500, "members": 210}
    ]
    compare_teams(squadre)

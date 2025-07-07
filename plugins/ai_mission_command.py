"""
Modulo: ai_mission_command.py
Mission Command AI: lancia missioni globali reali/digitali, traccia chi accetta/completa, premia con badge NFT, crea storia nel Museo Magic Team.
"""

MISSIONS = [
    "Aiuta un collega di un’altra nazione a raggiungere il suo primo traguardo",
    "Crea una diretta su un tema che ti appassiona",
    "Porta un’innovazione tech nel team questa settimana"
]

def launch_mission():
    import random
    mission = random.choice(MISSIONS)
    return f"Missione globale lanciata: '{mission}' — Chi accetta sarà celebrato come pioniere AI!"

def complete_mission(user_id, mission):
    # In reale: aggiorna museo/team, badge NFT, storia digitale
    return f"{user_id} ha completato la missione: '{mission}'. Premio: badge NFT + menzione nel Magic Museum!"

# --- ESEMPIO USO ---
if __name__ == "__main__":
    m = launch_mission()
    print(m)
    print(complete_mission("Massimo", m))

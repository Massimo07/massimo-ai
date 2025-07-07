"""
Modulo: ai_fusion_team_lab.py
Fusion Team Lab: crea team cross-nazionali/città, lancia challenge AI, aggrega soluzioni, forma team leader per ogni mercato.
"""

FUSION_LAB = []

def create_lab(members, topic):
    lab = {"members": members, "topic": topic, "solutions": []}
    FUSION_LAB.append(lab)
    return f"Fusion Lab creato su '{topic}' con {len(members)} membri!"

def add_solution(lab_topic, solution):
    for lab in FUSION_LAB:
        if lab["topic"] == lab_topic:
            lab["solutions"].append(solution)
            return f"Soluzione '{solution}' aggiunta al lab '{lab_topic}'."
    return "Lab non trovato."

# --- ESEMPIO USO ---
if __name__ == "__main__":
    print(create_lab(["Sara", "Giorgio", "Alex"], "Espansione in Romania"))
    print(add_solution("Espansione in Romania", "Sistema onboarding multilingua istantaneo"))

# ai_relationship_builder.py
"""
AI Relationship Builder: crea, rafforza e gestisce relazioni personali/professionali.
Suggerisce strategie, azioni, follow-up e monitora salute della relazione.
"""

class RelationshipBuilderAI:
    def __init__(self):
        self.relationships = []

    def add_relationship(self, name, relation_type):
        self.relationships.append({"name": name, "type": relation_type, "actions": []})

    def add_action(self, idx, action):
        self.relationships[idx]["actions"].append(action)

    def get_summary(self, idx):
        rel = self.relationships[idx]
        return f"{rel['name']} ({rel['type']}): {len(rel['actions'])} azioni"

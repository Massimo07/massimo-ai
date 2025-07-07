# ai_cosmic_network.py
"""
Motore di networking globale: collega utenti, agenti, community e mondi. 
Scopre nuove connessioni utili e suggerisce collaborazioni.
"""

class CosmicNetwork:
    def __init__(self):
        self.nodes = {}
        self.edges = []

    def add_node(self, name, data=None):
        self.nodes[name] = data or {}

    def connect(self, a, b):
        if a in self.nodes and b in self.nodes:
            self.edges.append((a, b))

    def get_connections(self, node):
        return [b for a, b in self.edges if a == node] + [a for a, b in self.edges if b == node]

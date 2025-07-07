"""
Modulo: network_graph.py
Crea e visualizza la struttura del team in formato grafo. Esporta per Graphviz/PNG e integra in dashboard!
"""

import networkx as nx
import matplotlib.pyplot as plt

def draw_team_graph(edges, filename="team_graph.png"):
    # edges = [(sponsor, iscritto), ...]
    G = nx.DiGraph()
    G.add_edges_from(edges)
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=1800, node_color="#A5F1FA")
    plt.savefig(filename)
    plt.close()
    return filename

# --- ESEMPIO USO ---
if __name__ == "__main__":
    edges = [("Massimo", "Luca"), ("Massimo", "Sara"), ("Luca", "Gianni")]
    print(draw_team_graph(edges))

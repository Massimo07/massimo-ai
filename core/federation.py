"""
core/federation.py – Gestione cluster, peer AI, istanze remote, discovery.
"""

import logging

class FederationService:
    def __init__(self):
        self.peers = []

    def register_peer(self, peer_uri):
        if peer_uri not in self.peers:
            self.peers.append(peer_uri)
            logging.info(f"[FEDERATION] Peer aggiunto: {peer_uri}")

    def broadcast(self, event, payload):
        # Placeholder: invio reale su rete/cluster/queue
        logging.info(f"[FEDERATION] Broadcast evento '{event}' a {len(self.peers)} peer")

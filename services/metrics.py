"""
services/metrics.py

Esportatore Prometheus-ready: conta utenti, mondi generati, messaggi, pagamenti, performance.
Supporta monitoraggio esteso, logging e dashboard (Grafana ready).
"""
from prometheus_client import Counter, Summary

users_created = Counter("users_created_total", "Numero totale utenti creati")
worlds_generated = Counter("worlds_generated_total", "Mondi digitali generati")
payments_processed = Counter("payments_processed_total", "Pagamenti processati")
api_latency = Summary("api_request_latency_seconds", "Tempo medio risposta API")

def inc_users():
    users_created.inc()

def inc_worlds():
    worlds_generated.inc()

def inc_payments():
    payments_processed.inc()

def observe_latency(value):
    api_latency.observe(value)

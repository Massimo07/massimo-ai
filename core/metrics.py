"""
core/metrics.py

Massimo AI – Metrics & Monitoring
Metrics Prometheus/Grafana ready, dashboard, counter, timing, custom event logging.
"""
try:
    from prometheus_client import Counter, Summary, Gauge
except ImportError:
    Counter = lambda *args, **kwargs: None
    Summary = lambda *args, **kwargs: None
    Gauge = lambda *args, **kwargs: None

request_counter = Counter("ai_requests_total", "Conteggio totale richieste AI")
error_counter = Counter("ai_errors_total", "Conteggio errori AI")
request_latency = Summary("ai_request_latency_seconds", "Tempo risposta AI")
active_users = Gauge("ai_active_users", "Utenti attivi")

def inc_requests():
    if request_counter: request_counter.inc()

def inc_errors():
    if error_counter: error_counter.inc()

def observe_latency(value: float):
    if request_latency: request_latency.observe(value)

def set_active_users(num: int):
    if active_users: active_users.set(num)

# Esempio logging event custom
def log_event(event: str, value: float = 1.0):
    print(f"[METRIC] {event} {value}")

if __name__ == "__main__":
    inc_requests()
    observe_latency(0.12)
    set_active_users(99)
    log_event("demo_event", 1)

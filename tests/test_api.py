# tests/test_api.py
"""
Test API principali Massimo AI
- CRUD user, agent, world
- Sicurezza, errori, edge
"""

import pytest
from fastapi.testclient import TestClient
from backend.main_backend import app

client = TestClient(app)

def test_healthcheck():
    resp = client.get("/healthz")
    assert resp.status_code == 200
    assert resp.json().get("status") == "ok"

def test_create_user():
    data = {"id": 123, "nome": "Utente", "email": "u@demo.com"}
    resp = client.post("/api/users/", json=data)
    assert resp.status_code in [200, 201]
    assert "id" in resp.json()

def test_invalid_user():
    data = {"id": 123, "nome": "NoMail"}
    resp = client.post("/api/users/", json=data)
    assert resp.status_code >= 400

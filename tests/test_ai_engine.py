# tests/test_ai_engine.py
"""
Test motore AI Engine, fallback, plug-in
"""

from ai_engine.pipeline import predict

def test_predict_gpt4o():
    inp = {"prompt": "Test AI"}
    result = predict(inp, model_name="gpt-4o")
    assert "Risposta GPT-4o" in result["result"]

def test_fallback():
    inp = {"prompt": "Test AI"}
    result = predict(inp, model_name="fake-model")
    assert "Risposta GPT-4o" in result["result"]
    assert "fallback" in result["explain"]

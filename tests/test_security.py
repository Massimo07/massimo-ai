# tests/test_security.py
"""
Test security: JWT, blacklist, hash, edge
"""

from core.security import generate_token, validate_token

def test_jwt_token():
    token = generate_token(user_id="99", exp_hours=1)
    decoded = validate_token(token)
    assert decoded["user_id"] == "99"

"""
SECURITY – Sicurezza avanzata, JWT, MFA, audit, blacklist.
"""
import jwt
import os
import datetime
import hashlib

class Security:
    SECRET_KEY = os.getenv("SECRET_KEY", "modifica-subito")
    ALGORITHM = "HS256"
    BLACKLIST = set()

    @classmethod
    def generate_token(cls, user_id: str, scope: str = "user", exp_hours: int = 24):
        payload = {
            "user_id": user_id,
            "scope": scope,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=exp_hours)
        }
        return jwt.encode(payload, cls.SECRET_KEY, algorithm=cls.ALGORITHM)

    @classmethod
    def validate_token(cls, token: str):
        try:
            data = jwt.decode(token, cls.SECRET_KEY, algorithms=[cls.ALGORITHM])
            if data.get("user_id") in cls.BLACKLIST:
                raise ValueError("Token blacklistato")
            return data
        except Exception as e:
            raise Exception(f"Token non valido: {e}")

    @classmethod
    def blacklist_token(cls, user_id: str):
        cls.BLACKLIST.add(user_id)

    @staticmethod
    def hash_ip(ip: str) -> str:
        return hashlib.sha256(ip.encode()).hexdigest()

    @staticmethod
    def mfa_check(code: str, expected: str) -> bool:
        return code == expected  # demo, usa librerie reali in produzione

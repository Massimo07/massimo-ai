"""
EXCEPTIONS – Errori granulari, codici, auto-log.
"""
import logging

class MassimoAIException(Exception):
    code = "E000"
    def __init__(self, message):
        super().__init__(message)
        logging.error(f"{self.code}: {message}")

class UnauthorizedException(MassimoAIException):
    code = "E401"

class InvalidTokenException(MassimoAIException):
    code = "E403"

class AIModelException(MassimoAIException):
    code = "E500"

class DBException(MassimoAIException):
    code = "E600"

class BusinessException(MassimoAIException):
    code = "E900"

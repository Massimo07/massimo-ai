"""
VoiceService – Sintesi vocale avanzata (TTS/STT), logging, fallback, pronto per cloud, device, API.
Top: può essere esteso per ElevenLabs, Google, Apple, WebRTC, occhiali smart.
"""

import logging
from typing import Optional

class VoiceError(Exception):
    pass

class VoiceService:
    def tts(self, text: str, lang: str = "it", voice: Optional[str]=None) -> bytes:
        if not text:
            raise VoiceError("Testo obbligatorio per TTS")
        logging.info(f"[VOICE] TTS – '{text[:50]}...' [{lang}] voice={voice or 'default'}")
        # Qui chiami ElevenLabs, Google TTS, ecc.
        return b"<audio-bytes>"  # In reale: output TTS

    def stt(self, audio_bytes: bytes, lang: str = "it", model: Optional[str]=None) -> str:
        if not audio_bytes:
            raise VoiceError("Audio obbligatorio per STT")
        logging.info(f"[VOICE] STT – audio [{lang}] model={model or 'default'}")
        # Qui chiami Whisper, Google, ecc.
        return "Trascrizione simulata"

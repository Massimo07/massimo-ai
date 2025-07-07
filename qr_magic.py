"""
Modulo: qr_magic.py
Genera QR code PNG per funnel, referral, eventi, landing page, onboarding rapido. Pronto per stampa/social/app.
"""

import qrcode

def create_qr(text, filename="qr_code.png"):
    img = qrcode.make(text)
    img.save(filename)
    return filename

# --- ESEMPIO USO ---
if __name__ == "__main__":
    link = "https://magicteam.live/signup?ref=ABC12345"
    print(create_qr(link))

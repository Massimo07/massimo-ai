"""
Modulo: mobile_scan.py
Scan QR/barcode/documenti: onboarding rapido, raccolta dati, verifica ordini/consegne, collegamento istantaneo a referral/funnel!
"""

import random

def scan_code(img_file):
    # In reale: usa API come Zxing, Zbar, Google MLKit, Pyzbar
    code = f"QR-{random.randint(100000,999999)}"
    print(f"Scansionato: {code}")
    return code

# --- ESEMPIO USO ---
if __name__ == "__main__":
    print(scan_code("img_qr.png"))

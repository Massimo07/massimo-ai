"""
Modulo: doc_scan_ai.py
OCR AI documenti: estrai dati da PDF, foto, moduli. Auto-compilazione moduli, archiviazione intelligente, estrazione campi chiave.
"""

def scan_document(img_path):
    # In reale: integra pytesseract, Google Vision, AWS Textract, ecc.
    print(f"OCR su {img_path}... (demo)")
    return {"nome": "Mario", "cf": "MRORSS99C12H501F", "importo": "149€"}

# --- ESEMPIO USO ---
if __name__ == "__main__":
    print(scan_document("documento_ordine.png"))

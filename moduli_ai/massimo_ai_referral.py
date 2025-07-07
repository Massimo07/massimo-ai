import json
import uuid

REFERRAL_PATH = "massimo_ai/referral.json"

def genera_referral(user_id, livello):
    code = str(uuid.uuid4())[:8]
    data = {"user_id": user_id, "livello": livello, "code": code}
    try:
        with open(REFERRAL_PATH, "r", encoding="utf-8") as f:
            refs = json.load(f)
    except:
        refs = {}
    refs[code] = data
    with open(REFERRAL_PATH, "w", encoding="utf-8") as f:
        json.dump(refs, f, indent=2, ensure_ascii=False)
    print(f"Referral generato: {code} per user {user_id} livello {livello}")
    return code

def cerca_referral(code):
    with open(REFERRAL_PATH, "r", encoding="utf-8") as f:
        refs = json.load(f)
    return refs.get(code)

if __name__ == "__main__":
    user_id = input("User ID: ")
    livello = input("Livello: ")
    code = genera_referral(user_id, livello)
    print("Usa questo referral:", code)

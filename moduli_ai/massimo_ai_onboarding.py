import json

def onboarding_user(user_id, lingua, nome=None):
    path = f"massimo_ai/users/{user_id}.json"
    user = {"id": user_id, "lingua": lingua, "nome": nome}
    with open(path, "w", encoding="utf-8") as f:
        json.dump(user, f, indent=2, ensure_ascii=False)
    print(f"Benvenuto {nome or ''}! Lingua scelta: {lingua}")
    return user

def carica_menu(lingua):
    with open("massimo_ai/lingue.json", "r", encoding="utf-8") as f:
        lingue = json.load(f)
    return lingue.get(lingua, {})

def mostra_menu(user):
    menu = carica_menu(user["lingua"])
    print(f"Menu in {user['lingua']}:")
    for voce in menu.get("voci", []):
        print("-", voce)

if __name__ == "__main__":
    uid = input("User ID: ")
    lingua = input("Lingua (es: it): ")
    nome = input("Nome: ")
    user = onboarding_user(uid, lingua, nome)
    mostra_menu(user)

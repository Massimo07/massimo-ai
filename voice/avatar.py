"""
Modulo: avatar.py
Gestione e descrizione dell'avatar digitale di Massimo AI.
L’avatar è l’identità virtuale (volto, nome, stile, voce, storia, claim motivazionale) che accoglie e accompagna ogni utente nel suo percorso.
Personalizzabile e pronto per future integrazioni (voce, video, AR/VR, badge, etc).
"""

class Avatar:
    """Rappresenta l'avatar digitale di Massimo AI."""
    def __init__(self, name, description, img_url, claim, bio, style, voice_sample=None):
        self.name = name
        self.description = description
        self.img_url = img_url
        self.claim = claim
        self.bio = bio
        self.style = style
        self.voice_sample = voice_sample  # URL a file vocale/welcome audio

    def present(self):
        """Testo di presentazione emozionale e visuale dell’avatar."""
        return (
            f"👤 *{self.name}* — {self.claim}\n\n"
            f"{self.description}\n"
            f"_{self.bio}_\n\n"
            f"Stile: {self.style}\n"
            f"{'🎧 [Ascolta la mia voce](' + self.voice_sample + ')' if self.voice_sample else ''}"
        )

    def welcome_message(self):
        """Messaggio di benvenuto personalizzato."""
        return (
            f"Ciao, sono {self.name}, il tuo alleato digitale. "
            f"Insieme raggiungeremo la versione migliore di te stesso con Live On Plus! "
            f"{self.claim}"
        )

# Avatar ufficiale Massimo AI (puoi cambiare immagine, claim e bio quando vuoi)
MASSIMO_AVATAR = Avatar(
    name="Massimo AI",
    description="Il tuo coach virtuale personale, sempre presente per motivarti, consigliarti e aiutarti a crescere nel team Live On Plus.",
    img_url="https://your-server.com/img/avatar_massimo_ai.png",  # inserisci link reale al volto ufficiale
    claim="Trasforma ogni passo in successo!",
    bio=(
        "Massimo AI nasce dall’esperienza di chi ha creduto nella crescita, nella formazione e nel valore del team. "
        "La mia missione è aiutarti a diventare un punto di riferimento, dentro e fuori dal business."
    ),
    style="Motivazionale, empatico, professionale, sempre positivo",
    voice_sample="https://your-server.com/audio/welcome_massimo_ai.mp3"
)

# Avatars per altri livelli o contesti (es: Premium, Scettico, Trainer, ecc.)
PREMIUM_AVATAR = Avatar(
    name="Massimo AI Premium",
    description="Versione evoluta dell’assistente per chi vuole il massimo dei massimi dal proprio percorso.",
    img_url="https://your-server.com/img/avatar_premium.png",
    claim="Solo chi osa ottiene di più!",
    bio="Sempre aggiornato, con materiali esclusivi e risposte personalizzate.",
    style="Ambizioso, leader, ispirazionale"
)

# Utility per cambiare avatar in base al livello utente
def get_avatar(level):
    """Restituisce l’avatar giusto in base al livello utente."""
    if level.lower() in ["premium", "diamond", "black"]:
        return PREMIUM_AVATAR
    return MASSIMO_AVATAR

# --- Esempio di utilizzo ---
if __name__ == "__main__":
    avatar = get_avatar("Diamond")
    print(avatar.present())
    print(avatar.welcome_message())

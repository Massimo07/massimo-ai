from datetime import datetime

class User:
    def __init__(
        self,
        id,
        name,
        cell,
        email,
        country,
        language,
        signup_date=None,
        sector="generico",
        role="utente",
        income=1000,
        used_features=None,
        satisfaction=7,
        plan=None
    ):
        self.id = id
        self.name = name
        self.cell = cell
        self.email = email
        self.country = country
        self.language = language
        self.signup_date = signup_date or datetime.now()
        self.sector = sector
        self.role = role
        self.income = income
        self.used_features = used_features if used_features is not None else []
        self.satisfaction = satisfaction
        self.plan = plan

class System:
    def __init__(
        self,
        id,
        name="Personalizzato",
        user_id=None,
        sector="generico",
        role="utente",
        income=1000,
        features=None,
        branding="Brand su misura",
        dashboard_url=None
    ):
        self.id = id
        self.name = name
        self.user_id = user_id
        self.sector = sector
        self.role = role
        self.income = income
        self.features = features if features is not None else []
        self.branding = branding
        self.dashboard_url = dashboard_url or f"https://dashboard.massimoai.com/{id}"

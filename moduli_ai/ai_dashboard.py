"""
Modulo: ai_dashboard.py
Dashboard AI: KPI, progressi, alert, insight su misura. Pronto per web, Streamlit, app — aggiornata ogni giorno!
"""

import streamlit as st

def render_dashboard(user_data):
    st.title(f"Benvenuto {user_data['name']} nella tua dashboard Massimo AI!")
    st.metric("PV personale", user_data.get("pv_personale", 0))
    st.metric("PV gruppo", user_data.get("pv_gruppo", 0))
    st.metric("Referral attivi", user_data.get("referral", 0))
    st.metric("Livello attuale", user_data.get("level", "Starter"))
    st.info(f"Obiettivo del mese: {user_data.get('goal', 'Diventa Black Diamond!')}")
    # Alert predittivi:
    if user_data.get("pv_personale", 0) < 60:
        st.warning("Aumenta i tuoi PV per mantenere la qualifica!")
    if user_data.get("referral", 0) < 4:
        st.info("Invita almeno 4 nuovi Director per scalare la classifica!")

# --- ESEMPIO USO (Streamlit app) ---
# Esegui: streamlit run ai_dashboard.py
# user_data = {"name": "Massimo", "pv_personale": 55, "pv_gruppo": 29500, "referral": 3, "level": "Diamond"}
# render_dashboard(user_data)

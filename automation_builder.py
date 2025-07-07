"""
Modulo: automation_builder.py
Costruttore workflow drag&drop (base Streamlit): crea funnel, drip, automazioni, quiz… senza programmare!
"""

import streamlit as st

st.set_page_config(page_title="Automation Builder - Massimo AI")

st.title("Automation Builder (beta)")

block = st.selectbox("Scegli un blocco", ["Invia messaggio", "Aggiungi a drip", "Quiz AI", "Email di follow-up"])
params = st.text_area("Parametri blocco (testo, tempo, domanda…)")
if st.button("Aggiungi blocco"):
    st.success(f"Blocco '{block}' aggiunto con parametri: {params}")
    # Qui puoi salvare nel backend la pipeline workflow!

st.markdown("**Crea la tua automazione trascinando e aggiungendo blocchi: invio messaggi, email, quiz, azioni custom…**")

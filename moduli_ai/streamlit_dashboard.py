"""
Modulo: streamlit_dashboard.py
Mini-dashboard web Streamlit: admin può vedere membri, feedback, knowledge, audit log, modificare FAQ/prodotti.
Pronta subito per locale o cloud.
"""

import streamlit as st
import data_manager
import feedback
import log_audit
import knowledge_editable

st.set_page_config(page_title="Massimo AI Dashboard", layout="wide")

st.title("Massimo AI — Admin Dashboard")

tab1, tab2, tab3, tab4 = st.tabs(["Team", "Feedback", "Knowledge Base", "Audit Log"])

with tab1:
    st.header("Team")
    users = data_manager.get_all_users()
    st.write(users)

with tab2:
    st.header("Feedback utenti")
    st.write(feedback.get_feedbacks())

with tab3:
    st.header("Knowledge Base")
    kb = knowledge_editable.load_knowledge()
    st.json(kb)
    st.subheader("Aggiungi FAQ")
    q = st.text_input("Domanda FAQ")
    a = st.text_area("Risposta FAQ")
    if st.button("Aggiungi FAQ"):
        knowledge_editable.add_faq(q, a)
        st.success("FAQ aggiunta!")

with tab4:
    st.header("Audit log (ultime azioni)")
    log = log_audit.get_audit_log()
    st.write(log)

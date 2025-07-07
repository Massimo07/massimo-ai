# rag_module.py
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
import logging

logger = logging.getLogger(__name__)

# Configurazione del percorso del database ChromaDB
# Questo creerà una cartella 'chroma_db' nella stessa directory del bot
CHROMA_DB_PATH = os.path.join(os.path.dirname(__file__), "chroma_db")
# Assicurati che il nome del tuo PDF sia ESATTAMENTE "2025 Italiano Piano Compensi-1.pdf"
PDF_PATH = os.path.join(os.path.dirname(__file__), "2025 Italiano Piano Compensi-1.pdf")

# Inizializzazione degli embeddings OpenAI (serve la tua chiave API di OpenAI)
# Questa parte trasforma il testo in numeri che l'AI capisce meglio
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")

# Questa funzione serve a leggere il PDF, dividerlo in pezzetti e creare la "libreria"
def initialize_vector_db():
    if not os.path.exists(PDF_PATH):
        logger.error(f"File PDF non trovato al percorso: {PDF_PATH}. Impossibile inizializzare il database vettoriale.")
        return None

    logger.info(f"Caricamento del PDF da {PDF_PATH}...")
    loader = PyPDFLoader(PDF_PATH)
    documents = loader.load()
    logger.info(f"Caricati {len(documents)} pagine dal PDF.")

    # Qui il PDF viene diviso in piccoli "pezzi"
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_documents(documents)
    logger.info(f"Suddivisi i documenti in {len(texts)} chunks.")

    # Qui i "pezzi" vengono trasformati in numeri e salvati nella "libreria"
    logger.info(f"Creazione/caricamento del database vettoriale in {CHROMA_DB_PATH}...")
    db = Chroma.from_documents(texts, embeddings, persist_directory=CHROMA_DB_PATH)
    db.persist() # Forza il salvataggio su disco
    logger.info("Database vettoriale Chroma inizializzato con successo.")
    return db

# Questa funzione serve a cercare i "pezzi" più pertinenti nella "libreria" quando l'utente fa una domanda
def retrieve_documents(query, db, k=3):
    if db is None:
        logger.warning("Database vettoriale non inizializzato. Impossibile recuperare documenti.")
        return []
    
    docs = db.similarity_search(query, k=k) # Cerca i k documenti più simili
    return docs

# Questa è la "libreria" che verrà usata dal bot
vector_db = None

# Questa funzione viene chiamata all'avvio del bot per preparare la "libreria"
def setup_rag_db():
    global vector_db
    # Se la "libreria" non esiste ancora, la crea da zero
    if not os.path.exists(CHROMA_DB_PATH) or not os.listdir(CHROMA_DB_PATH):
        logger.info("Database vettoriale non trovato o vuoto. Inizializzazione da PDF...")
        vector_db = initialize_vector_db()
    else:
        # Se la "libreria" esiste già, la carica (molto più veloce)
        logger.info(f"Caricamento del database vettoriale esistente da {CHROMA_DB_PATH}...")
        try:
            vector_db = Chroma(persist_directory=CHROMA_DB_PATH, embedding_function=embeddings)
            logger.info("Database vettoriale caricato con successo.")
        except Exception as e:
            logger.error(f"Errore nel caricamento del database vettoriale esistente: {e}. Riprovo a inizializzare da zero.")
            vector_db = initialize_vector_db() # Se ci sono problemi, la ricrea
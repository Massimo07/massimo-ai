import os
import sqlite3
from datetime import datetime

from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

# Configuration
oai_api_key = os.getenv("OPENAI_API_KEY")
db_path = "memory_store.sqlite"
vector_index_path = "faiss_index"
storage_dir = "uploads"

# Ensure upload directory exists
os.makedirs(storage_dir, exist_ok=True)

# Initialize SQLite for metadata and transcripts
conn = sqlite3.connect(db_path)
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY,
        role TEXT,
        content TEXT,
        timestamp TEXT
    )''')
conn.commit()

# Initialize embeddings
embeddings = OpenAIEmbeddings(openai_api_key=oai_api_key)

# Initialize or load vector store for embeddings
if os.path.exists(f"{vector_index_path}.faiss"):
    vector_store = FAISS.load_local(vector_index_path, embeddings)
else:
    # Creazione di un index FAISS con un testo fittizio
    vector_store = FAISS.from_texts(["inizializzazione"], embeddings)
    vector_store.save_local(vector_index_path)

# Memory buffer for chat context
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Conversational chain with retrieval
llm = ChatOpenAI(temperature=0, openai_api_key=oai_api_key)
qa = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=vector_store.as_retriever(),
    memory=memory
)

# Helper to save incoming message
def save_message(role: str, content: str):
    timestamp = datetime.utcnow().isoformat()
    c.execute(
        "INSERT INTO messages (role, content, timestamp) VALUES (?, ?, ?)",
        (role, content, timestamp)
    )
    conn.commit()
    # Also index embeddings
    vector_store.add_texts([content])
    vector_store.save_local(vector_index_path)

# Endpoint simulation: process user input
def process_user_input(user_text=None, file_path=None):
    # Handle text input
    if user_text:
        save_message("user", user_text)
        response = qa.run(user_text)
        save_message("assistant", response)
        return response

    # Handle file upload (text or image)
    if file_path:
        filename = os.path.basename(file_path)
        dest = os.path.join(storage_dir, filename)
        os.rename(file_path, dest)
        meta = f"User uploaded file: {filename}"
        save_message("user", meta)
        # Optionally, extract text from files/images here
        return f"Ho ricevuto e memorizzato il file {filename}."

# Esempio d'uso
if __name__ == "__main__":
    while True:
        inp = input("Tu: ")
        if inp.lower() in ["exit", "quit"]:
            break
        bot_response = process_user_input(user_text=inp)
        print(f"AI: {bot_response}")

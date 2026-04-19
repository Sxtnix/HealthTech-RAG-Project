import os
from dotenv import load_dotenv

# LangChain (RAG)
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

# Embeddings locales (SOLUCIÓN DEFINITIVA)
from langchain_community.embeddings import HuggingFaceEmbeddings

# Cliente OpenAI (GitHub Models)
from openai import OpenAI

# ==============================
# 🔑 Cargar variables de entorno
# ==============================
load_dotenv()

# ==============================
# 📄 1. Cargar documento PDF
# ==============================
loader = PyPDFLoader("data/documento.pdf")
documents = loader.load()

# ==============================
# ✂️ 2. Dividir en chunks
# ==============================
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = splitter.split_documents(documents)

# ==============================
# 🧠 3. Embeddings locales
# ==============================
embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# ==============================
# 💾 4. Base vectorial (FAISS)
# ==============================
if os.path.exists("faiss_index"):
    vectorstore = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )
else:
    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local("faiss_index")

# ==============================
# 🔎 5. Retriever
# ==============================
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# ==============================
# 🤖 6. Cliente LLM (GitHub Models)
# ==============================
client = OpenAI(
    base_url=os.getenv("GITHUB_BASE_URL"),
    api_key=os.getenv("GITHUB_TOKEN")
)

# ==============================
# 🚀 7. Función RAG
# ==============================
def preguntar(pregunta: str):
    try:
        docs = retriever.invoke(pregunta)
        contexto = "\n".join([doc.page_content for doc in docs])

        response = client.chat.completions.create(
            model="gpt-4o-mini",  # puedes cambiarlo si el profe usa otro
            messages=[
    {
        "role": "system",
        "content": "Eres un asistente interno de HealthTech Innovations. Responde de forma clara, profesional y breve. Usa SOLO el contexto entregado. Si no hay información suficiente, indica que no hay datos disponibles."
    },
    {
        "role": "user",
        "content": f"Contexto:\n{contexto}\n\nPregunta: {pregunta}"
    }
],
            temperature=0.2
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error en el sistema: {str(e)}"
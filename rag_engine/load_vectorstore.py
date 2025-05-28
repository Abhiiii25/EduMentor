from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

# Load vector DB
def load_vectorstore():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.load_local(
        folder_path="edu_vector_store",
        embeddings=embeddings,
        allow_dangerous_deserialization=True  # ✅ This is safe if the store was created by you
    )
    return db

def retrieve_documents(query, k=4):
    db = load_vectorstore()
    docs = db.similarity_search(query, k=k)
    return docs

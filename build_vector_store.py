import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.docstore.document import Document
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()  

# Path to your main knowledge base folder
BASE_PATH = "edu_knowledge_base"

def load_documents(base_path):
    documents = []
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith(".pdf"):
                file_path = os.path.join(root, file)
                path_parts = file_path.split(os.sep)
                doc_type = path_parts[-2]  # e.g. study_tips
                subject = os.path.splitext(file)[0]  # e.g. math
                loader = PyPDFLoader(file_path)
                raw_docs = loader.load()
                for doc in raw_docs:
                    doc.metadata["type"] = doc_type
                    doc.metadata["subject"] = subject
                    documents.append(doc)
    return documents

def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    return splitter.split_documents(documents)



def create_faiss_vector_store(split_docs):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_store = FAISS.from_documents(split_docs, embeddings)
    vector_store.save_local("edu_vector_store")
    print("✅ Vector store saved to 'edu_vector_store/'")


if __name__ == "__main__":
    print("📥 Loading documents...")
    docs = load_documents(BASE_PATH)
    print(f"📄 Loaded {len(docs)} documents")

    print("✂️ Splitting documents...")
    split_docs = split_documents(docs)
    print(f"🔹 Created {len(split_docs)} text chunks")

    print("📦 Creating vector store...")
    create_faiss_vector_store(split_docs)

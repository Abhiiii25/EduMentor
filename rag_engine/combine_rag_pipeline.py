from rag_engine.load_vectorstore import retrieve_documents
from rag_engine.query_llama3_groq import query_llama3

def run_rag_pipeline(user_query):
    docs = retrieve_documents(user_query, k=4)
    context = "\n\n".join([doc.page_content for doc in docs])
    final_prompt = f"""You are an expert academic assistant helping students. Use the following context to answer their question.

Context:
{context}

Question:
{user_query}

Answer:"""

    response = query_llama3(final_prompt)
    return response

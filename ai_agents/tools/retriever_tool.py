from langchain.tools import Tool

def retriever_tool():
    def retrieve_documents(query):
        # Placeholder function to simulate document retrieval
        # Replace with actual implementation
        return []

    return Tool(
        name="StudyNoteRetriever",
        func=lambda q: "\n\n".join([doc.page_content for doc in retrieve_documents(q)]),
        description="Use this tool to get notes or tips from the knowledge base."
    )
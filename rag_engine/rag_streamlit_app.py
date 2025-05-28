# rag_streamlit_app.py
import streamlit as st
from rag_engine.combine_rag_pipeline import run_rag_pipeline

st.set_page_config(page_title="EduMentor RAG QA", layout="wide")
st.title("📚 EduMentor – Academic Question Answering (RAG)")

if "rag_chat" not in st.session_state:
    st.session_state.rag_chat = []

query = st.text_input("Ask your academic question (e.g., 'What is photosynthesis?'):")

if query:
    with st.spinner("Retrieving answer..."):
        response = run_rag_pipeline(query)
        st.session_state.rag_chat.append(("Student", query))
        st.session_state.rag_chat.append(("RAG System", response))

# Display history
for role, message in st.session_state.rag_chat:
    if role == "Student":
        st.markdown(f"**🧑 You**: {message}")
    else:
        st.markdown(f"**📘 RAG System**: {message}")

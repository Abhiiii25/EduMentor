# pages/1_📘_RAG_and_AI_Tutor.py
import streamlit as st
from rag_engine.combine_rag_pipeline import run_rag_pipeline
from ai_agents.agent_executor import run_agent

st.set_page_config(page_title="RAG + AI Tutor", layout="wide")
st.title("📘 EduMentor – Academic Q&A Assistant")

if "qa_phase" not in st.session_state:
    st.session_state.qa_phase = "rag"  # 'rag' or 'agent'
if "chat_log" not in st.session_state:
    st.session_state.chat_log = []

# Step 1: Student enters the initial academic query
if st.session_state.qa_phase == "rag":
    query = st.text_input("Ask your academic question (e.g., 'Explain the basics of quadratic equations'):")

    if query:
        with st.spinner("Getting accurate info from EduMentor's knowledge base..."):
            rag_response = run_rag_pipeline(query)
            st.session_state.chat_log.append(("Student", query))
            st.session_state.chat_log.append(("RAG System", rag_response))
            st.session_state.last_rag_answer = rag_response
            st.session_state.qa_phase = "agent"

# Step 2: Student enters follow-up/cross question
elif st.session_state.qa_phase == "agent":
    follow_up = st.text_input("Ask a follow-up question to the AI Tutor:")

    if follow_up:
        with st.spinner("AI Tutor is responding..."):
            # Combine previous answer + follow-up query for agent
            prompt = f"""You previously answered: "{st.session_state.last_rag_answer}"

Now the student is asking a follow-up: "{follow_up}"

Continue the conversation accordingly."""
            agent_response = run_agent(prompt)
            st.session_state.chat_log.append(("Student", follow_up))
            st.session_state.chat_log.append(("AI Tutor", agent_response))

# Chat Display
st.markdown("---")
for role, msg in st.session_state.chat_log:
    if role == "Student":
        st.markdown(f"**🧑 You**: {msg}")
    elif role == "RAG System":
        st.markdown(f"**📘 RAG Answer**: {msg}")
    elif role == "AI Tutor":
        st.markdown(f"**🤖 AI Tutor**: {msg}")

# Reset button
if st.button("🔄 Start Over"):
    st.session_state.qa_phase = "rag"
    st.session_state.chat_log = []
    st.session_state.last_rag_answer = ""

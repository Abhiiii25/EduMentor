import streamlit as st
from ai_agents.agent_executor import run_agent

st.set_page_config(page_title="EduMentor Tutor", layout="wide")
st.title("🧠 EduMentor – AI Tutor Assistant")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

query = st.text_input("Ask your AI Tutor (e.g., 'Explain quadratic equations'):")

if query:
    with st.spinner("Thinking..."):
        response = run_agent(query)
        st.session_state.chat_history.append(("Student", query))
        st.session_state.chat_history.append(("AI Tutor", response))

# Chat Display
for role, message in st.session_state.chat_history:
    if role == "Student":
        st.markdown(f"**🧑 You**: {message}")
    else:
        st.markdown(f"**🤖 AI Tutor**: {message}")

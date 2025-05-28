# import streamlit as st
# import os
# import subprocess
# from rag_engine.combine_rag_pipeline import run_rag_pipeline


# st.set_page_config(page_title="EduMentor", layout="wide")

# st.sidebar.title("EduMentor")
# page = st.sidebar.selectbox("Choose Module", ["📘 Knowledge Base Q&A", "🧠 AI Tutor Agent"])

# if page == "📘 Knowledge Base Q&A":
#     # Import and render your original RAG interface
    
#     run_rag_pipeline.render()

# elif page == "🧠 AI Tutor Agent":
#     # Call the agent interface directly
#     exec(open("ai_agents/streamlit_app.py").read())


# # streamlit_app.py
# import streamlit as st

# st.set_page_config(page_title="EduMentor Platform", layout="wide")
# st.title("🎓 Welcome to EduMentor – AI Learning Assistant")

# st.markdown("""
# Select a page from the sidebar:
# - **📘 RAG + AI Tutor**: Ask a question and get grounded + interactive answers.
# """)









# app.py

import streamlit as st

st.set_page_config(page_title="EduMentor AI", layout="wide")

st.title("📘 Welcome to EduMentor AI")
st.markdown("""
## 🚀 An AI-Powered Personalized Learning Platform

EduMentor provides:

- 🎓 Student Dashboard: Academic analytics, real-time risk prediction, and personalized AI tutoring.
- 👩‍🏫 Teacher Dashboard: At-risk student tracking and insights.
- 📚 AI Tutor: Ask questions and get help from your curriculum-aligned knowledge base.

Use the **sidebar** to select the dashboard you want to explore.
""")

st.success("Please use the sidebar to navigate to the Student or Teacher dashboard.")

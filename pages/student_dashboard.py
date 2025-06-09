# pages/1_Student_Dashboard.py

import streamlit as st
import pandas as pd
import joblib
from rag_engine.load_vectorstore import retrieve_documents
from ai_agents.agent_utils import run_student_agent
from utils.email_alerts import send_email_alert

# Load dataset
df = pd.read_csv("data/edu_mentor_GENAI.csv")

# Load ML models
classifier = joblib.load("ml_models/risk_classifier.pkl")
regressor = joblib.load("ml_models/risk_regressor.pkl")

st.set_page_config(page_title="Student Dashboard", layout="wide")
st.title("🎓 Student Dashboard")

# Create student dropdown with name + email
df['dropdown'] = df['student_name'] + " (" + df['email_id'] + ")"
selected_student = st.selectbox("Select Student", df['dropdown'].unique())
email_id = selected_student.split("(")[-1].replace(")", "").strip()

# Filter selected student's data
student_data = df[df['email_id'] == email_id].iloc[0]

# Display student info
st.markdown(f"### 👋 Welcome, **{student_data['student_name']}**")

# Step 1: Academic Overview
st.subheader("📊 Academic Overview")
col1, col2 = st.columns(2)
with col1:
    st.metric("📘 Math Grade", f"{student_data['math_grade']}%")
    st.metric("📗 Science Grade", f"{student_data['science_grade']}%")
    st.metric("📙 History Grade", f"{student_data['history_grade']}%")
    st.metric("📕 English Grade", f"{student_data['english_grade']}%")
with col2:
    st.metric("✅ Assignment Completion", f"{student_data['assignment_completion']}%")
    st.metric("📈 Engagement Score", f"{student_data['engagement_score']}%")
    st.metric("📅 Attendance Ratio", f"{student_data['attendance_ratio']}%")
    st.metric("🕒 Avg. Session Duration", f"{student_data['average_session_duration_minutes']} min")

# Step 2: ML Risk Prediction
# Drop only non-feature columns
drop_cols = ['student_id', 'student_name', 'email_id', 'password']
available_cols = [col for col in drop_cols if col in student_data.index]
features = student_data.drop(available_cols)
features_df = pd.DataFrame([features])

# Handle missing columns expected by the ML pipeline
expected_cols = classifier.named_steps['preprocessor'].feature_names_in_
missing_cols = set(expected_cols) - set(features_df.columns)
for col in missing_cols:
    features_df[col] = ""  # or 0 / np.nan depending on model expectations

# Reorder to match expected column order (not strictly necessary but clean)
features_df = features_df[list(expected_cols)]

# Predict risk
predicted_class = classifier.predict(features_df)[0]
predicted_score = regressor.predict(features_df)[0]

# Send email alert if student is at risk
if predicted_class == 1:
    send_email_alert(
        to_email="abhigaikwad089@gmail.com",  # teacher or admin email
        student_name=student_data["student_name"],
        risk_score=predicted_score
    )

# Display prediction results
risk_label = "At Risk 🚨" if predicted_class == 1 else "Not At Risk ✅"
risk_color = "red" if predicted_class == 1 else "green"

st.subheader("🤖 Risk Prediction")
st.markdown(
    f"**Predicted Risk Status:** <span style='color:{risk_color}; font-weight:bold'>{risk_label}</span>",
    unsafe_allow_html=True
)
st.markdown(
    f"**Predicted Risk Score:** <span style='color:{risk_color}; font-weight:bold'>{predicted_score:.2f}</span>",
    unsafe_allow_html=True
)

# Step 3: Personalized Suggestions
st.subheader("📌 Personalized Suggestions")
if predicted_class == 1:
    st.warning("You're currently at risk. Here’s what you can do:")
    st.markdown("""
    - 📚 Attend after-school tutoring sessions (Math & Science).
    - ✅ Complete pending assignments.
    - 🧠 Review factoring and quadratic topics.
    - 📅 Increase platform engagement (logins, session time).
    """)
else:
    st.success("You're performing well! Keep it up and stay consistent. 👍")


# # Step 4: Ask AI Tutor (RAG + Agent)
# st.subheader("🤖 Ask Your AI Tutor")
# query = st.text_input("Ask any academic question (e.g., 'I’m struggling with quadratic equations')")
# if st.button("Get Help"):
#     if query:
#         with st.spinner("Thinking..."):
#             response = run_student_agent(query)
#             st.markdown("**📘 Tutor Response:**")
#             st.write(response)
#     else:
#         st.warning("Please enter a question.")

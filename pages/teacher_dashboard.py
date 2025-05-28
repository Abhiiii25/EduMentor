# pages/2_Teacher_Dashboard.py

import streamlit as st
import pandas as pd
import joblib
from utils.email_alerts import send_email_alert


st.set_page_config(page_title="Teacher Dashboard", layout="wide")
st.title("👩‍🏫 Teacher Dashboard")

# Load data
df = pd.read_csv("data/edu_mentor_GENAI.csv")

# Load models
classifier = joblib.load("ml_models/risk_classifier.pkl")
regressor = joblib.load("ml_models/risk_regressor.pkl")

# Drop identity columns for predictions
features_to_use = [
    'student_name', 'email_id', 'std', 'math_grade', 'english_grade',
       'science_grade', 'history_grade', 'overall_grade',
       'assignment_completion', 'engagement_score', 'math_lec_present',
       'science_lec_present', 'history_lec_present', 'english_lec_present',
       'attendance_ratio', 'login_frequency_per_week',
       'average_session_duration_minutes', 'learning_style',
       'content_type_preference', 'completed_lessons', 'practice_tests_taken',
       'lms_test_scores'
]

# Predict risk_score and is_at_risk if not present
if 'risk_score' not in df.columns or 'is_at_risk' not in df.columns:
    X = df[features_to_use]
    df["risk_score"] = regressor.predict(X)
    df["is_at_risk"] = classifier.predict(X)

# Filter at-risk students
at_risk_df = df[df["is_at_risk"] == 1]

st.subheader("🚨 Students At Risk")

if at_risk_df.empty:
    st.success("Great news! No students are currently at risk.")
else:
    st.markdown("Here are the students who need immediate attention:")

    st.dataframe(
        at_risk_df[[
            'student_name', 'email_id', 'std',
            'overall_grade', 'assignment_completion',
            'engagement_score', 'attendance_ratio', 'risk_score'
        ]].sort_values(by="risk_score", ascending=False),
        use_container_width=True
    )
    st.markdown("### 📩 Notify Teachers")



    

    # Optional filter
    with st.expander("🔍 Filter by Grade or Risk Score"):
        grade = st.selectbox("Select Grade", options=["All"] + sorted(df['std'].unique().tolist()))
        threshold = st.slider("Minimum Risk Score", 0, 100, 65)

        filtered = at_risk_df[at_risk_df['risk_score'] >= threshold]
        if grade != "All":
            filtered = filtered[filtered['std'] == grade]

        st.dataframe(filtered, use_container_width=True)

        st.markdown("### 📩 Notify Teachers")
        if st.button("Send Email Alerts for At-Risk Students"):
            for _, row in filtered.iterrows():
                teacher_email = "abhigaikwad089@gmail.com"  # Replace with actual teacher's email
                send_email_alert(teacher_email, row["student_name"], row["risk_score"])
            st.success("Email alerts sent to teachers.")

    st.markdown("### Recommendations for Teachers:")
    st.markdown("""
- **Monitor Attendance**: Check attendance records for these students.
- **Engagement**: Look into engagement scores and consider personalized interventions.
- **Assignments**: Ensure that students are completing their assignments on time.
- **Communication**: Reach out to parents or guardians to discuss the student's performance.
""")

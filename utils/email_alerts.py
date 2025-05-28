import smtplib
from email.message import EmailMessage

def send_email_alert(to_email, student_name, risk_score):
    # Set your email details
    FROM_EMAIL = "abhigaikwad089@gmail.com"  # Replace with your sender email
    FROM_PASSWORD = "phxs gens pepp mexv"   # App-specific password or actual password
    SUBJECT = f"🚨 Alert: {student_name} is At Risk"
    BODY = f"""
    Dear Teacher,

    This is an automated alert from EduMentor.

    Student: {student_name}
    Risk Score: {risk_score:.2f}/100

    Immediate action is advised. Please review their academic progress and offer assistance.

    Regards,
    EduMentor System
    """

    try:
        msg = EmailMessage()
        msg.set_content(BODY)
        msg["Subject"] = SUBJECT
        msg["From"] = FROM_EMAIL
        msg["To"] = to_email

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(FROM_EMAIL, FROM_PASSWORD)
            smtp.send_message(msg)
        print(f"✅ Email sent to {to_email}")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

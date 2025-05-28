<p align="center">
  <img src="assets/banner.png" width="100%" alt="EduMentor Banner"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Streamlit-%23FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/Python-3.10-blue.svg?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/github/license/Abhiiii25/EduMentor?style=for-the-badge"/>
  <img src="https://img.shields.io/github/stars/Abhiiii25/EduMentor?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/AI%20Agent-LangChain-ffce00?style=for-the-badge&logo=OpenAI&logoColor=black"/>
  <img src="https://img.shields.io/badge/RAG-Groq%20LLaMA--3.3-ff69b4?style=for-the-badge"/>
</p>


### ✅ **EduMentor - AI-Powered Student Success Platform**

### 🎓 Empowering Students. Supporting Teachers. Driving Academic Success.

EduMentor is an intelligent education platform designed to **predict student risk**, **personalize learning**, and **support teachers** with insights, alerts, and AI-powered tools.

---

## 🚀 Features

* 📊 **Student Dashboard** with real-time academic insights
* 🤖 **ML-based Risk Prediction** (classification & regression)
* 🎯 **Personalized Suggestions** for improvement
* 🧠 **AI Tutor** with RAG + LangChain Agents for real-time help
* 👩‍🏫 **Teacher Dashboard** to monitor at-risk students
* ✉️ **Automated Email Alerts** for teachers
* 📂 **Knowledge Base Integration** with PDF support

---

## 🛠️ Tech Stack

| Frontend      | Backend             | ML Models                 | AI/NLP                    |
| ------------- | ------------------- | ------------------------- | ------------------------- |
| 🎨 Streamlit  | ⚡ FastAPI (planned) | 🤖 scikit-learn           | 🧠 LangChain + LLaMA 3    |
| 📈 Matplotlib | 📬 SMTP for alerts  | 📊 Classifier + Regressor | 📚 HuggingFace Embeddings |

---

## 📁 Project Structure

```
EduMentor/
│
├── ml_models/               # risk_classifier.pkl, risk_regressor.pkl
├── data/                    # edu_mentor_GENAI.csv
├── pages/                   # Streamlit multipage UI
│   ├── 1_Student_Dashboard.py
│   └── 2_Teacher_Dashboard.py
├── rag_engine/              # Retrieval-Augmented Generation
├── ai_agents/               # LangChain AI Agents & Tools
├── utils/                   # Email alert utils
├── app.py                   # Main Streamlit app
└── README.md
```

---

## 🚦 How It Works

1. Student logs in using `email_id`
2. ML models predict:

   * 🔍 Risk status (classification)
   * 📉 Risk score (regression)
3. Real-time suggestions based on predictions
4. Student queries answered by AI agent (via RAG)
5. Teacher dashboard shows at-risk students
6. 🔔 Email alerts sent to teachers automatically

---

## 🔧 Setup Instructions

1. **Clone the repo**

```bash
git clone https://github.com/Abhiiii25/EduMentor.git
cd EduMentor
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the app**

```bash
streamlit run app.py
```

---

## 📬 Email Alerts Setup

1. Enable **2-Step Verification** in your Gmail.
2. Create an **App Password** and add it to `.env` or environment variable.
3. Check logs to confirm email is sent when a student is flagged `At Risk`.

---

## 📸 Screenshots

![image_alt](https://github.com/Abhiiii25/EduMentor/blob/65e761fd3e1b0a8c8621512cb9e4ba8783725f5e/Screenshot%202025-05-28%20224821.png)

![image_alt](https://github.com/Abhiiii25/EduMentor/blob/04efd8d1ad5c16681376a60606d6ad88cbdb5472/rag-ai-tutor.png)

![image_alt](https://github.com/Abhiiii25/EduMentor/blob/fbcb4088ef5450aea07c65dd0ad03ac42693025d/student-dashboard.png)

![image_alt](https://github.com/Abhiiii25/EduMentor/blob/12d5d2e3ccdec00df83057e505ca2d0a43ee5fb4/teacher-dashboard.png)





---

## 🌟 Contributing

We welcome PRs and ideas! Please open an issue or discussion before making major changes.

---

## 📄 License

MIT License © 2025 [Abhiiii25](https://github.com/Abhiiii25)

---

## 🙌 Special Thanks

* [LangChain](https://www.langchain.com/)
* [Groq LLaMA 3](https://groq.com/)
* [Hugging Face](https://huggingface.co/)
* [Streamlit](https://streamlit.io/)


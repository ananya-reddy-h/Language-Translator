# 🌍 LangChain Translator with OpenAI + LangSmith

A simple Flask web app that translates English text into any language using **LangChain + OpenAI**.  
All LLM runs are logged to **LangSmith** for debugging and monitoring.

---

## 🚀 Features
- Translate text from English into any target language
- Web interface (Flask)
- LangSmith tracing for observability

---

## 🛠 Setup

### 1. Clone and install
```bash
git clone https://github.com/yourusername/translation-app.git
cd translation-app
python -m venv venv
source venv/bin/activate   # (Windows: venv\Scripts\activate)
pip install -r requirements.txt

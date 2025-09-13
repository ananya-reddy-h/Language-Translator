# app.py
import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from translator import get_model, translate_text

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)
model = get_model()

@app.route("/", methods=["GET", "POST"])
def index():
    translated = ""
    if request.method == "POST":
        text = request.form.get("text", "").strip()
        language = request.form.get("language", "French").strip()
        if text:
            translated = translate_text(model, text, language)
    return render_template("index.html", translated=translated)

if __name__ == "__main__":
    app.run(debug=True, port=5000)

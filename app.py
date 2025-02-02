from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Securely load the API key from environment variable
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure the Gemini API
genai.configure(api_key="AIzaSyDdhj9OJ3ibM4I_Q2TI7v3ziT7KQPC7V-k")

@app.route('/')
def home():
    return render_template('index2.html')

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "").strip()

    if not user_input:
        return jsonify({"error": "Invalid input"}), 400

    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(user_input)
        reply = response.text.strip()
        return jsonify({"reply": reply})

    except Exception as e:
        print(str(e))
        return jsonify({"error": "API error", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

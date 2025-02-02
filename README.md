# TechTribe
from flask import Flask, request, jsonify,render_template
import openai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Replace with your actual Opeapp.py
# nAI API key

@app.route('/')
def home():
    return render_template('index2.html')

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")

    prompt = f"You are a medical emergency chatbot. Provide helpful responses for symptoms or first-aid advice. User: {user_input}"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return jsonify({"reply": response["choices"][0]["message"]["content"]})

if __name__ == "__main__":
    app.run(debug=True)


import requests

response = requests.get("https://api.github.com")
print(response.status_code)


url = "http://127.0.0.1:5000"
data = {"message": "I have a severe headache. What should I do?"}
response = requests.post(url, json=data)

print(response)


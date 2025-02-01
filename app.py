from flask import Flask, request, jsonify
import openai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Replace with your actual OpenAI API key
openai.api_key = "your-api-key-here"

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

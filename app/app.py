from flask import Flask, request, jsonify, render_template
import os
from dotenv import load_dotenv
import requests
import logging

# 🔥 START DEBUG
print("🚀 STARTING APP...")

# ✅ Load .env (from project root)
load_dotenv(dotenv_path="../.env")

# ✅ Get API key
API_KEY = os.getenv("OPENROUTER_API_KEY")

if not API_KEY:
    print("❌ ERROR: API KEY NOT FOUND")
else:
    print("✅ API KEY LOADED")

# ✅ Logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

# ✅ Home route (IMPORTANT for UI)
@app.route("/")
def home():
    return render_template("index.html")

# ✅ Health check (DevOps)
@app.route("/health")
def health():
    return {"status": "running"}

# ✅ Chat route
@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    logging.info(f"User: {user_message}")

    try:
        url = "https://openrouter.ai/api/v1/chat/completions"

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost",
            "X-Title": "AI Chatbot"
        }

        data = {
            "model": "openai/gpt-3.5-turbo",
            "messages": [
                {"role": "user", "content": user_message}
            ]
        }

        response = requests.post(url, headers=headers, json=data)

        logging.info(f"STATUS: {response.status_code}")
        logging.info(f"RESPONSE: {response.text}")

        response.raise_for_status()

        reply = response.json()["choices"][0]["message"]["content"]

    except Exception as e:
        logging.error(f"ERROR: {str(e)}")
        reply = "⚠️ Error: Unable to fetch response. Check API key or model."

    return jsonify({"reply": reply})


# ✅ Run Flask properly
if __name__ == "__main__":
    print("🔥 RUNNING FLASK SERVER...")
    app.run(host="0.0.0.0", port=5000, debug=True)
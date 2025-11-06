import os
import requests
from flask import Flask, session, request, jsonify, render_template
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "change-me")

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = "gemini-2.5-flash"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"


@app.route("/")
def home():
    return render_template("chat.html")


# --- Utility functions -------------------------------------------------------

def _get_session_messages():
    return session.setdefault("messages", [])

def _call_gemini(messages):
    if not API_KEY:
        return "(Server misconfigured: GEMINI_API_KEY not set.)"

    contents = [
        {"role": "user" if m["role"] == "user" else "model",
         "parts": [{"text": m["text"]}]}
        for m in messages
    ]
    headers = {"x-goog-api-key": API_KEY, "Content-Type": "application/json"}
    payload = {"contents": contents}

    resp = requests.post(API_URL, headers=headers, json=payload, timeout=45)
    resp.raise_for_status()
    data = resp.json()

    cands = data.get("candidates", [])
    if not cands:
        return "(no candidates)"
    parts = cands[0].get("content", {}).get("parts", [])
    return parts[0].get("text", "(no text)") if parts else "(no parts)"


# --- Routes ------------------------------------------------------------------

@app.route("/")
def index():
    return render_template("chat.html")

@app.get("/api/history")
def history():
    return jsonify({"messages": _get_session_messages()})

@app.post("/api/chat")
def chat():
    data = request.get_json(silent=True) or {}
    prompt = (data.get("prompt") or "").strip()
    if not prompt:
        return jsonify({"error": "prompt is required"}), 400

    messages = _get_session_messages()
    messages.append({"role": "user", "text": prompt})
    session.modified = True

    try:
        reply = _call_gemini(messages)
    except requests.HTTPError as e:
        return jsonify({"error": f"HTTP {e.response.status_code}: {e.response.text[:400]}"}), 502
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    messages.append({"role": "model", "text": reply})
    session.modified = True
    return jsonify({"text": reply})


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)

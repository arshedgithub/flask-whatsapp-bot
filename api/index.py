from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv
import requests
import os

load_dotenv()

DIFY_API_KEY = os.getenv('DIFY_API_KEY')
DIFY_URL = os.getenv('DIFY_URL')

user_sessions = {}

app = Flask(__name__)

@app.route('/')
def home():
    return 'WA-Bot Deployed Successfully!'

@app.route('/whatsapp', methods=["POST"])
def reply_whatsapp():
    from_number = request.values.get('From', '')
    user_input = request.values.get('Body', '').strip()

    resp = MessagingResponse()
    msg = resp.message()

    conversation_id = user_sessions.get(from_number, "")

    payload = {
        "inputs": {},
        "query": user_input,
        "response_mode": "blocking",
        "conversation_id": conversation_id,
        "user": from_number,
        "files": []
    }

    headers = {
        "Authorization": f"Bearer {DIFY_API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(DIFY_URL, headers=headers, json=payload)
        data = response.json()

        new_convo_id = data.get("conversation_id")
        if new_convo_id:
            user_sessions[from_number] = new_convo_id

        answer = data.get("answer", "Sorry! I didn't understand that.")
        msg.body(answer)

    except Exception as e:
        print("Error:", e)
        msg.body("There was an error contacting the AI service.")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
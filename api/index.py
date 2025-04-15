from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/')
def home():
    return 'WA-Bot Deployed Successfully!'

@app.route('/whatsapp', methods=["POST"])
def reply_whatsapp():
    incoming_msg = request.values.get('Body', '').strip().lower()
    resp = MessagingResponse()
    msg = resp.message()

    if incoming_msg in ['hi', 'hello']:
        msg.body("Hello! How can I assist you today?")
    else:
        msg.body("I'm here to help! Please type your question.")

    return str(resp)
    
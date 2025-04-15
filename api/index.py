from flask import Flask
import os
from twilio import Client

app = Flask(__name__)

@app.route('/')
def home():
    return 'WA-Bot Deployed Successfully!'

@app.route('/about')
def about():
    return 'About'

# account_sid = os.getenv('ACCOUNT_SID')
# auth_token = os.getenv('AUTH_TOKEN')

# client = Client(account_sid, auth_token)

# from_wa_number = 'whatsapp:' + os.getenv('TWILIO_NUMBER')
# to_wa_number = 'whatsapp:' + os.getenv('RECIEPTANT_NUMBER')

# client.messages.create(body='Hello Testing WA bot!', to=to_wa_number, from_=from_wa_number)
#!/usr/bin/env python 
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

messaging_service_sid = os.environ['TWILIO_MESSAGING_SERVICE_SID']
destination_number = '+19195923953'

def sendText(message):
    messageToSend = client.messages \
        .create(
            body=message,
            messaging_service_sid=messaging_service_sid,
            to=destination_number
        )
    print(messageToSend.sid)


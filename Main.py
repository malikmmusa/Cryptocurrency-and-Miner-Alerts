#!/usr/bin/env python 
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request, redirect
import EthermineData as ether
import CoinData as coin
import multiprocessing

app = Flask(__name__)

p = multiprocessing.Process(target=coin.getPrices, args=('NA',))

@app.route('/')
def index():
    return 'HOMEPAGE'

@app.route("/sms", methods=['POST'])
def sms_reply():
    receivedMessage = request.form['Body']
    print('BODY ', receivedMessage)
    if receivedMessage.lower() == 'hash':
        message = MessagingResponse()
        message.message(ether.sendStats())
        return str(message)
    else: return 'None'

if __name__ == "__main__":
    p.start()
    app.run(debug=True)
    p.join()
    print('ENDED')
#!/usr/bin/env python 
import time
import SendTextViaSMS as text
import requests
import datetime
import os

def getPrices(prevPayout):
    while True:
        miner = os.getenv('MINER_ID')
        # Get and recieve text updates for desired coin if increases or decreases by 5% in 24hr period
        prices = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Cethereum&vs_currencies=usd').json()
        price_bitcoin = prices.get('bitcoin').get('usd')
        price_ethereum = prices.get('ethereum').get('usd')
        price_24hrs_bitcoin = requests.get('https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=1').json().get('prices')[0][1]
        price_24hrs_ethereum = requests.get('https://api.coingecko.com/api/v3/coins/ethereum/market_chart?vs_currency=usd&days=1').json().get('prices')[0][1]
        if (price_bitcoin / price_24hrs_bitcoin) < 0.95:
            print('CHECKING PRICE')
            message = f'Bitcoin is down 5% to {price_bitcoin} in the last 24 hours.'
            text.sendText(message)

        if (price_ethereum / price_24hrs_ethereum) < 0.95:
            print('CHECKING PRICE')
            message = f'Ethereum is down 5% to {price_ethereum} in the last 24 hours.'
            text.sendText(message)

        # Get and recieve text updates for mining operations and payouts
        payout = requests.get(f'https://api.ethermine.org/miner/:{miner}/payouts').json().get('data')[0]
        if prevPayout == 'NA':
            prevPayout = payout

        payoutAmount = round(payout.get('amount') / 1000000000000000000, 6)
        payoutTime = datetime.datetime.fromtimestamp(payout.get('paidOn')).strftime('%I:%M %p')
        if prevPayout != payout:
            message = f'You have been paid out {payoutAmount} at {payoutTime}'
            text.sendText(message)
            prevPayout = payout

        # Check every 5 minutes seconds for updates
        time.sleep(300)
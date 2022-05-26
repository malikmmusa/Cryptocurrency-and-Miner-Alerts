import requests
import CoinData as coin
import os

miner = os.getenv('MINER_ID')

def sendStats():
    ethermine = requests.get(f'https://api.ethermine.org/miner/:{miner}/dashboard').json().get('data').get('currentStatistics')
    reportedHash = round(ethermine.get('reportedHashrate') / 1000000, 2)
    currentHash = round(ethermine.get('currentHashrate') / 1000000, 2)
    unpaidBalance = round(ethermine.get('unpaid') / 1000000000000000000, 6)
    return ({'reportedHashrate': reportedHash,
        'currentHashrate': currentHash,
        'unpaidBalance': unpaidBalance})

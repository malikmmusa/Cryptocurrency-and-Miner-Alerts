# Cryptocurrency-and-Miner-Alerts
Text alert system that automatically texts updates for changes in crypto prices and mining payouts. Can manually text for current miner status to be sent via text

This program will send automatic text updates for:
- Decreases in prices of ethereum and bitcoin by 5% in the past 24 hours
- Payouts from mining rigs

Additionally, you can manually text 'hash' to your twilio number to recieve live updates on current hashrate, reported hashrate, and the average hashrate of your miner

To use: Add Twilio information and your miner id to .env 

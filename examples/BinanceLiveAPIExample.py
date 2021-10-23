import os
import json

from binance.client import Client

# init

# init coinsDict
coinsDict = {}
with open("files/coins.json", "r") as j:
	data = json.load(j)

for dataElement in data:
	coinsDict[dataElement["symbol"]] = 0

# print(coinsDict)


# API key and secret
LIVE_BINANCE_API_KEY = os.environ.get('live_binance_api_key')
LIVE_BINANCE_SECRET = os.environ.get('live_binance_secret')

api_key = LIVE_BINANCE_API_KEY
api_secret = LIVE_BINANCE_SECRET
client = Client(api_key, api_secret)

# API URLs
LIVE_BINANCE_API_URL = 'https://api.binance.us/api'

client.API_URL = LIVE_BINANCE_API_URL

# get balances for all assets & some account information
# print(client.get_account())

# get balance for a specific asset only (BTC)
# print(client.get_asset_balance(asset='BTC'))

# get latest price from Binance API
BTCSymbol = "BTCUSD"
btc_price = client.get_symbol_ticker(symbol=BTCSymbol)
# print full output (dictionary)
print(btc_price)


# get latest price from Binance API
prices = client.get_symbol_ticker()
# print full output (dictionary)
#print(prices)
# loop through prices
# for price in prices:
#     if price['symbol'] in coinsDict:
#         print('symbol:', price['symbol'])
#         print('price:', price['price'])
#         print('------------')

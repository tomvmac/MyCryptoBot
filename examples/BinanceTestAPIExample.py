import os
import json

from binance.client import Client



# init coinsDict
coinsDict = {}
with open("files/testcoins.json", "r") as j:
	data = json.load(j)

for dataElement in data:
	coinsDict[dataElement["symbol"]] = 0

# print(coinsDict)

# init

# API key and secret
TEST_BINANCE_API_KEY = os.environ.get('test_binance_api_key')
TEST_BINANCE_SECRET = os.environ.get('test_binance_secret')

api_key = TEST_BINANCE_API_KEY
api_secret = TEST_BINANCE_SECRET
client = Client(api_key, api_secret)

# API URLs
TEST_BINANCE_API_URL = 'https://testnet.binance.vision/api'

client.API_URL = TEST_BINANCE_API_URL

# get balances for all assets & some account information
# print(client.get_account())

# get balance for a specific asset only (BTC)
# print(client.get_asset_balance(asset='BTC'))

# get latest price from Binance API
prices = client.get_symbol_ticker()
# print full output (dictionary)
#print(prices)
# loop through prices
for price in prices:
    if price['symbol'] in coinsDict:
        print('symbol:', price['symbol'])
        print('price:', price['price'])
        print('------------')


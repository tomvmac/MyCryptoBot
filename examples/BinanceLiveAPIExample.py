import os
import json

from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceOrderException
from binance.enums import *

def initializeCoinsDict():
    # init coinsDict
    coinsDict = {}
    with open("files/testcoins.json", "r") as j:
        data = json.load(j)

    for dataElement in data:
        coinsDict[dataElement["symbol"]] = 0

    # print(coinsDict)
    return coinsDict

def initializeTestBinanceClient():
    # init

    # API key and secret
    LIVE_BINANCE_API_KEY = os.environ.get('LIVE_BINANCE_API_KEY')
    LIVE_BINANCE_SECRET = os.environ.get('LIVE_BINANCE_SECRET')

    api_key = LIVE_BINANCE_API_KEY
    api_secret = LIVE_BINANCE_SECRET
    client = Client(api_key, api_secret)

    # API URLs
    LIVE_BINANCE_API_URL = 'https://api.binance.com/api'
    # LIVE_BINANCE_API_URL = 'https://api.binance.us/api'




    client.API_URL = LIVE_BINANCE_API_URL
    return client

def getAccountInfo():
    # get balances for all assets & some account information
    return client.get_account()

def getBalance(symbol):
    # get balance for a specific asset only (BTC)
    return client.get_asset_balance(asset=symbol)

def getPrice(symbol):
    # get balance for a specific asset only (BTC)
    return client.get_symbol_ticker(symbol=symbol)

def getPrices():
    # get latest price from Binance API
    prices = client.get_symbol_ticker()
    return prices

def printPrices(prices, coinsDict):
    # loop through prices
    for price in prices:
        if price['symbol'] in coinsDict:
            print('symbol:', price['symbol'])
            print('price:', price['price'])
            print('------------')

def buyMarketOrder(symbol, qty):
    # create a real order if the test orders did not raise an exception

    try:
        order = client.order_market_buy(symbol=symbol,quantity=qty)
        return order

    except BinanceAPIException as e:
        # error handling goes here
        print(e)
    except BinanceOrderException as e:
        # error handling goes here
        print(e)


def sellMarketOrder(symbol, qty):
    # create a real order if the test orders did not raise an exception

    try:
        order = client.order_market_sell(symbol=symbol,quantity=qty)
        return order

    except BinanceAPIException as e:
        # error handling goes here
        print(e)
    except BinanceOrderException as e:
        # error handling goes here
        print(e)


# -------------------------------------------------------------------------------------------------------

# Initialize
coinsDict = initializeCoinsDict()

# Init Client
client = initializeTestBinanceClient()

# Get Account Info
# print(getAccountInfo())

# Get Balance for a symbol
# print("----------------")
# print(getBalance("BTC"))
# print("----------------")

# Get Price
# print(getPrice("BTCUSDT"))

# Get Prices
prices = getPrices()
print(prices)
# printPrices(prices, coinsDict)

# Buy Market Order
# print(buyMarketOrder("BTCUSDT", 0.1))

# Sell Market Order
# print(sellMarketOrder("BTCUSDT", 0.5))
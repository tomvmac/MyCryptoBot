import json
from binance.client import Client
import Constants
import BinanceClient

def loadBinanceCoins():
    # init coinsDict
    coinsDict = {}
    with open(Constants.BINANCE_COINS_JSON_PATH, "r") as j:
        data = json.load(j)

    for dataElement in data:
        coinsDict[dataElement["symbol"]] = 0

    return coinsDict


def getCurrentPrice(symbol):
    client = BinanceClient.getClient()
    return client.get_symbol_ticker(symbol=symbol)

def getCurrentPrices():
    client = BinanceClient.getClient()
    return client.get_symbol_ticker()


def printPrice(price):
    print('symbol:', price['symbol'])
    print('price:', price['price'])

def printPrices(prices, coinsDict):
    for price in prices:
        if price['symbol'] in coinsDict:
            print('symbol:', price['symbol'])
            print('price:', price['price'])
            print('------------')


def processPrices(prices, coinsDict):
    return
    # 2. Loop through each response
    #    a. if symbol exists in coinsDict
    #    b. if price > 0, compare prices, execute buy trade
    #    c. set price to new price from response




import json
from binance.client import Client
import Constants
import BinanceClient

def loadBinanceCoins():
    with open(Constants.BINANCE_COINS_JSON_PATH, "r") as j:
        data = json.load(j)
    j.close()

    return data


def updateBinanceCoinsWithLatestPrices():
    coins = loadBinanceCoins()
    prices = getCurrentPrices()

    # iterate through prices, if price symbol and coin symbol equal, set price
    for price in prices:
        if price["symbol"] in coins:
            coins[price["symbol"]] = {'symbol': price["symbol"], 'price': float(price["price"])}
    # Update coins to file
    with open(Constants.BINANCE_COINS_JSON_PATH, "w") as k:
        json.dump(coins, k)
    k.close()

    return coins

def getCurrentPrice(symbol):
    client = BinanceClient.getClient()
    return client.get_symbol_ticker(symbol=symbol)

def getCurrentPrices():
    client = BinanceClient.getClient()
    return client.get_symbol_ticker()


def printPrice(price):
    print('symbol:', price['symbol'])
    print('price:', price['price'])
    print('\n------------')

def printPrices(prices, coinsDict):
    for price in prices:
        if price['symbol'] in coinsDict:
            print('symbol:', price['symbol'])
            print('price:', price['price'])
            print('\n------------')


def processPrices(prices, coinsDict):
    return
    # 2. Loop through each response
    #    a. if symbol exists in coinsDict
    #    b. if price > 0, compare prices, execute buy trade
    #    c. set price to new price from response



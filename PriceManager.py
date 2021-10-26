import json
from binance.client import Client
import Constants
import BinanceClient
import Trader

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

def hasBuyCriteriaMet(priceItem, coinsDict):
    return


def hasSellCriteriaMet(priceItem, coinsDict):
    return


def generateBuy(priceItem, coinsDict):
    tradeItem = {}
    if hasBuyCriteriaMet((priceItem, coinsDict)):
        # Open Trade
        tradeItem = Trader.createTradeItem(priceItem, coinsDict)
        Trader.openTrade(tradeItem)
    return

def generateSell(priceItem, coinsDict):
    tradeItem = {}
    if hasSellCriteriaMet((priceItem, coinsDict)):
        # Close Trade
        tradeItem = Trader.createTradeItem(priceItem, coinsDict)
        Trader.closeTrade(tradeItem)
    return

def processPrices(prices, coinsDict):
    # Loop through prices and match coinsDict
    for priceItem in prices:
        if priceItem["symbol"] in coinsDict:
            # Generate Buys
            generateBuy(priceItem, coinsDict)
            # Generate Sells
            generateSell(priceItem, coinsDict)
    return



import json
from datetime import datetime, timedelta
from core.api.binance import BinanceClient
from core.util import Constants, Logger
from core import PriceTrends, Trader


def loadBinanceCoins():
    with open(Constants.BINANCE_US_COINS_JSON_PATH, "r") as j:
        data = json.load(j)
    j.close()

    return data


def updateBinanceCoinsWithLatestPrices(strategyConfigs):
    coins = loadBinanceCoins()
    prices = getCurrentPrices()

    # iterate through prices, if price symbol and coin symbol equal, set price
    for price in prices:
        if price["symbol"] in coins:
            coins[price["symbol"]]["price"] = price["price"]
            #  Add to PriceTrends
            priceTrends = coins[price["symbol"]]["priceTrends"]
            priceTrends = PriceTrends.addPriceTrend(priceTrends, {"idx": 0, "price": price["price"]}, strategyConfigs)
            coins[price["symbol"]]["priceTrends"] = priceTrends

    # Update coins to file
    with open(Constants.BINANCE_US_COINS_JSON_PATH, "w") as k:
        json.dump(coins, k)
    k.close()

    return coins

def getCurrentPrice(symbol):
    currentPrice = 0.00
    price = BinanceClient.getPrice(symbol)
    currentPrice = float(price["price"])

    return currentPrice

def getCurrentPrices():
    prices = BinanceClient.getPrices()
    for price in prices:
        price["price"] = float(price["price"])

    return prices


def getHistoricalPrices(symbol, interval):
    # Get historical prices
    yesterday = datetime.today() - timedelta(days=1)
    yesterdayStr = str(yesterday)
    nowStr = str(datetime.now())
    historicalPriceBars = BinanceClient.getHistoricalPrices(symbol, interval, yesterdayStr)
    return historicalPriceBars


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

def hasPriceMetCondition(symbol, condition):

    isConditionMet = False

    # Handle price check condition
    if condition["comparisonType"] == Constants.COMPARISON_TYPE_PRICE_AMOUNT:
        # Handle price amount condition
        isConditionMet = hasPriceAmountMetCondition(symbol, condition)
    elif condition["comparisonType"] == Constants.COMPARISON_TYPE_PRICE_PERCENTAGE:
        # Handle price percentage condition
        isConditionMet = hasPricePercentageMetCondition(symbol, condition)

    return isConditionMet


def hasPriceAmountMetCondition(symbol, condition):

    isConditionMet = False

    # Get price for symbol and compare to condition value
    currentPrice = getCurrentPrice(symbol)

    # Get condition
    if condition["comparator"] == Constants.COMPARISON_TYPE_IS_GREATER_THAN:
        if currentPrice > condition["conditionValue"]:
            isConditionMet = True
    elif condition["comparator"] == Constants.COMPARISON_TYPE_IS_LESS_THAN:
        if currentPrice < condition["conditionValue"]:
            isConditionMet = True

    return isConditionMet



def hasPricePercentageMetCondition(symbol, condition):
    isConditionMet = False

    # Get price for symbol and compare to condition value
    currentPrice = getCurrentPrice(symbol)

    # Get historical prices for symbol based on interval
    historicalPriceBars = getHistoricalPrices(symbol, condition["timeInterval"])

    if len(historicalPriceBars) < 4:
        return False

    secondLastBarIndex = len(historicalPriceBars) - 2
    secondLastBar = historicalPriceBars[secondLastBarIndex]
    secondLastBarClosePrice = float(historicalPriceBars[secondLastBarIndex][4])

    pricePercentageDiff = PriceTrends.percentGainLoss(secondLastBarClosePrice, currentPrice)

    # Get condition
    if condition["comparator"] == Constants.COMPARISON_TYPE_IS_GREATER_THAN:
        if pricePercentageDiff > condition["conditionValue"]:
            isConditionMet = True
    elif condition["comparator"] == Constants.COMPARISON_TYPE_IS_LESS_THAN:
        if pricePercentageDiff < condition["conditionValue"]:
            isConditionMet = True

    return isConditionMet


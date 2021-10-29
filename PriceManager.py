import json
import Constants
import BinanceClient
import Trader
import PriceTrends
import Logger

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
            coins[price["symbol"]]["price"] = price["price"]
            #  Add to PriceTrends
            priceTrends = coins[price["symbol"]]["priceTrends"]
            priceTrends = PriceTrends.addPriceTrend(priceTrends, {"idx": 0, "price": price["price"]})
            coins[price["symbol"]]["priceTrends"] = priceTrends

    # Update coins to file
    with open(Constants.BINANCE_COINS_JSON_PATH, "w") as k:
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
    # Check if symbol is in open trades, if so skip
    openTrades = Trader.loadOpenTrades()
    for openTrade in openTrades:
        if priceItem["symbol"] == openTrade["symbol"]:
            return False

    # Percentage Gain Criteria
    hasPercentageGainMet = False
    prevPrice = coinsDict[priceItem["symbol"]]["price"]
    currPrice = priceItem["price"]

    if PriceTrends.percentGainLoss(prevPrice, currPrice) > Constants.MIN_PERCENTAGE_GAIN_TO_BUY:
        hasPercentageGainMet = True

    # Price Trends should not be downward trending
    isDownTrending = PriceTrends.isDownTrend(coinsDict[priceItem["symbol"]]["priceTrends"])

    if hasPercentageGainMet is True and isDownTrending is False:
        return True

    return False


def hasSellCriteriaMet(priceItem, coinsDict):
    # Check if symbol is in open trades, if so skip
    openTrades = Trader.loadOpenTrades()
    currTrade = {}

    for openTrade in openTrades:
        if priceItem["symbol"] == openTrade["symbol"]:
            currTrade = openTrade

    if len(openTrades) == 0 or currTrade == {}:
        return False

    prevPrice = currTrade["price"]
    currPrice = priceItem["price"]
    percentageGainLoss = 0.0000
    percentageGainLoss = PriceTrends.percentGainLoss(prevPrice, currPrice)

    # Take Profit
    isTakeProfit = False
    if percentageGainLoss >= Constants.TAKE_PROFIT_PERCENTAGE_GAIN:
        isTakeProfit = True

    # Stop Loss
    isStopLoss = False
    if percentageGainLoss <= Constants.STOP_LOSS_PERCENTAGE:
        isStopLoss = True

    # Price Trends should not be downward trending
    isDownTrending = PriceTrends.isDownTrend(coinsDict[priceItem["symbol"]]["priceTrends"])

    # Sell when either Stop Loss or Down Trend is occurring
    if isStopLoss is True or isDownTrending is True or isTakeProfit is True:
        Logger.GetLogger().info("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        Logger.GetLogger().info("Criteria to Sell: " + priceItem["symbol"])
        Logger.GetLogger().info("Buy Price: {x}".format(x=prevPrice))
        Logger.GetLogger().info("Sell Price: {x}".format(x=currPrice))
        Logger.GetLogger().info("PriceTrends - {x}".format(x=coinsDict[priceItem["symbol"]]["priceTrends"]))
        Logger.GetLogger().info("isStopLoss:  {x}".format(x=isStopLoss))
        Logger.GetLogger().info("isDownTrending: {x}".format(x=isDownTrending))
        Logger.GetLogger().info("isTakeProfit: {x}".format(x=isTakeProfit))
        Logger.GetLogger().info("percentageGainLoss: {x}".format(x=percentageGainLoss))
        Logger.GetLogger().info("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        return True

    return False


def generateBuy(priceItem, coinsDict):
    tradeItem = {}
    if hasBuyCriteriaMet(priceItem, coinsDict):
        # Open Trade
        tradeItem = Trader.createBuyTradeItem(priceItem, coinsDict)
        Trader.openTrade(tradeItem)
    return

def generateSell(priceItem, coinsDict):
    tradeItem = {}
    if hasSellCriteriaMet(priceItem, coinsDict):
        # Close Trade
        tradeItem = Trader.createSellTradeItem(priceItem, coinsDict)
        Trader.closeTrade(tradeItem)
    return

def processPrices():
    # Load Binance Coins from file
    coinsDict = loadBinanceCoins()

    # Get Current Prices
    prices = getCurrentPrices()

    # Loop through prices and match coinsDict
    for priceItem in prices:
        if priceItem["symbol"] in coinsDict:
            # Generate Buys
            generateBuy(priceItem, coinsDict)
            # Generate Sells
            generateSell(priceItem, coinsDict)

    # Update coinsDict with latest prices
    updateBinanceCoinsWithLatestPrices()

    return



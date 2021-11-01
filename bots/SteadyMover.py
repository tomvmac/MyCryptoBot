import sched
import time

from core.util import Logger
from core import PriceManager, PriceTrends, Trader

# Strategy Name: Steady Mover
#
# General Strategy:
# Steady Mover is a very conservative strategy that enters a trade only if there has been a slight increase and not downtrending.  It will exit as soon as.

# Buy Signal:
# 1. Recent price increase more than threshold 2% (AND)
# 2. NOT downtrending

# Sell Signal:
# 1. Downtrending (OR)
# 2. Take Profit (OR)
# 3. Stop Loss

# Strategy Configs:
# Scheduling Parameters
SCHEDULE_EXECUTION_INTERVAL_IN_MINUTES = 15
SCHEDULE_EXECUTION_INTERVAL_IN_SECONDS = SCHEDULE_EXECUTION_INTERVAL_IN_MINUTES * 60
SCHEDULE_SLEEP_INTERVAL_IN_SECONDS = 1

# Trading
TRADING_SOURCE_CURRENCY_SYMBOL = "USD"
TRADING_UNIT_AMOUNT = 100

# Pricing Criteria
PRICE_TRENDS_SIZE = 10
PRICE_TRENDS_MIN_CONSECUTIVE_ITEMS = 3
PRICE_TRENDS_DOWNTREND_PERCENTAGE_THRESHOLD = -0.5
MIN_PERCENTAGE_GAIN_TO_BUY = 2
TAKE_PROFIT_PERCENTAGE_GAIN = 15
STOP_LOSS_PERCENTAGE = -1

strategyConfigs = {}
strategyConfigs["TRADING_SOURCE_CURRENCY_SYMBOL"] = TRADING_SOURCE_CURRENCY_SYMBOL
strategyConfigs["TRADING_UNIT_AMOUNT"] = TRADING_UNIT_AMOUNT
strategyConfigs["PRICE_TRENDS_SIZE"] = PRICE_TRENDS_SIZE
strategyConfigs["PRICE_TRENDS_MIN_CONSECUTIVE_ITEMS"] = PRICE_TRENDS_MIN_CONSECUTIVE_ITEMS
strategyConfigs["PRICE_TRENDS_DOWNTREND_PERCENTAGE_THRESHOLD"] = PRICE_TRENDS_DOWNTREND_PERCENTAGE_THRESHOLD
strategyConfigs["MIN_PERCENTAGE_GAIN_TO_BUY"] = MIN_PERCENTAGE_GAIN_TO_BUY
strategyConfigs["TAKE_PROFIT_PERCENTAGE_GAIN"] = TAKE_PROFIT_PERCENTAGE_GAIN
strategyConfigs["STOP_LOSS_PERCENTAGE"] = STOP_LOSS_PERCENTAGE


def hasBuySignal(priceItem, coinsDict):
    # Check if symbol is in open trades, if so skip
    openTrades = Trader.loadOpenTrades()
    for openTrade in openTrades:
        if priceItem["symbol"] == openTrade["symbol"]:
            return False

    # Percentage Gain Criteria
    hasPercentageGainMet = False
    prevPrice = coinsDict[priceItem["symbol"]]["price"]
    currPrice = priceItem["price"]

    if PriceTrends.percentGainLoss(prevPrice, currPrice) > MIN_PERCENTAGE_GAIN_TO_BUY:
        hasPercentageGainMet = True

    # Price Trends should not be downward trending
    isDownTrending = PriceTrends.isDownTrend(coinsDict[priceItem["symbol"]]["priceTrends"], strategyConfigs)

    if hasPercentageGainMet is True and isDownTrending is False:
        return True

    return False


def hasSellSignal(priceItem, coinsDict):
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
    if percentageGainLoss >= TAKE_PROFIT_PERCENTAGE_GAIN:
        isTakeProfit = True

    # Stop Loss
    isStopLoss = False
    if percentageGainLoss <= STOP_LOSS_PERCENTAGE:
        isStopLoss = True

    # Price Trends should not be downward trending
    isDownTrending = PriceTrends.isDownTrend(coinsDict[priceItem["symbol"]]["priceTrends"], strategyConfigs)

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
    if hasBuySignal(priceItem, coinsDict):
        # Open Trade
        tradeItem = Trader.createBuyTradeItem(priceItem, coinsDict, strategyConfigs)
        Trader.openTrade(tradeItem, strategyConfigs)
    return

def generateSell(priceItem, coinsDict):
    tradeItem = {}
    if hasSellSignal(priceItem, coinsDict):
        # Close Trade
        tradeItem = Trader.createSellTradeItem(priceItem, coinsDict)
        Trader.closeTrade(tradeItem, strategyConfigs)
    return

def execute():
    # Load Binance Coins from file
    coinsDict = PriceManager.loadBinanceCoins()

    # Get Current Prices
    prices = PriceManager.getCurrentPrices()

    # Loop through prices and match coinsDict
    for priceItem in prices:
        if priceItem["symbol"] in coinsDict:
            # Generate Buys
            generateBuy(priceItem, coinsDict)
            # Generate Sells
            generateSell(priceItem, coinsDict)

    # Update coinsDict with latest prices
    PriceManager.updateBinanceCoinsWithLatestPrices(strategyConfigs)

    return




# ---------------------------------------------------------------------------------------------------------------------------------------------------------------

# Schedule executions

scheduler = sched.scheduler(time.time, time.sleep)

while True:
    scheduler.enter(SCHEDULE_EXECUTION_INTERVAL_IN_SECONDS, SCHEDULE_SLEEP_INTERVAL_IN_SECONDS, execute)
    scheduler.run()
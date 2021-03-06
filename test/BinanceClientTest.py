from core.api.binance import BinanceClient
from datetime import datetime, timedelta

# Get Account Info
# print(BinanceClient.getAccountInfo())

# Get Balance for a symbol
# print("----------------")
# print("Get Balance: ")
# print(BinanceClient.getBalance("BTC"))
# print("----------------")

# Get Price
print("----------------")
print("Get Price: ")
print(BinanceClient.getPrice("BTCUSDT"))
print("----------------")

# Get Prices
print("----------------")
print("Get Prices: ")
binanceCoins = BinanceClient.getPrices()
binanceCoins.sort(key=lambda x: x.get('symbol'))
print(binanceCoins)

# filter
# filtered = filter(lambda c: 'USDT' in c['symbol'], binanceCoins)
# filteredBinanceCoins = binanceCoins(filtered)
#
# print(filteredBinanceCoins)
# print("----------------")




# Buy Market Order
# print(BinanceClient.buyMarketOrder("ONEUSD", 500))

# Sell Market Order
# print(BinanceClient.sellMarketOrder("USDTUSD", 50))

# Get historical prices
# yesterday = datetime.today() - timedelta(days = 1)
# yesterdayStr = str(yesterday)
# nowStr = str(datetime.now())
# historicalPriceBars = BinanceClient.getHistoricalPrices("BTCUSD", "4h", yesterdayStr)
# print("-----------------------")
# print("historical prices:")
# print(historicalPriceBars)
#
# # latest closing price
# firstBarIndex = 0
# firstBar = historicalPriceBars[0]
# firstBarClosePrice = historicalPriceBars[0][4]
# # print(firstBar)
# print("First Bar Close Price:", firstBarClosePrice)
#
# midBarIndex = int(len(historicalPriceBars) / 2)
# # print("Mid Bar Index" , midBarIndex)
# midBar = historicalPriceBars[midBarIndex]
# midBarClosePrice = historicalPriceBars[midBarIndex][4]
# print("Mid Bar Close Price", midBarClosePrice)
#
# lastBarIndex = len(historicalPriceBars)
# lastBar = historicalPriceBars[lastBarIndex-1]
# lastBarClosePrice = historicalPriceBars[lastBarIndex-1][4]
# print("Last Bar Close Price", lastBarClosePrice)

# get date from timestamp
# timestampStart = 1545730073
# timestampEnd = 1545730073
#
# print(datetime.fromtimestamp(timestampStart))
# print(datetime.fromtimestamp(timestampEnd))

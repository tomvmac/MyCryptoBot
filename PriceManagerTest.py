import PriceManager

# Load Binance Coins from file
# coinsDict = PriceManager.loadBinanceCoins()
# print(coinsDict)

# Load Current Price
print(PriceManager.getCurrentPrice("BTCUSD"))

# Load Current Prices
prices = PriceManager.getCurrentPrices()
print(prices)

# Update Current Prices to CoinsDict
# PriceManager.updateBinanceCoinsWithLatestPrices()

# Process Prices
# PriceManager.processPrices()
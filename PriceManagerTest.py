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

# Sell Criteria
# Scenario: Gain 20%
# priceItem = {"symbol": "AAVEUSD","price": 345.44}
# coinsDict = {"AAVEUSD": {"symbol": "AAVEUSD","price": 343.44, "priceTrends": [{"idx": 0,"price": 342.07},{"idx": 1,"price": 342.07},{"idx": 2,"price": 341.87},{"idx": 3,"price": 344.07},{"idx": 4,"price": 345.07},{"idx": 5,"price": 343.07}]}}
# hasSellCriteriaMet = PriceManager.hasSellCriteriaMet(priceItem, coinsDict)
# print(hasSellCriteriaMet)


# Scenario: Stop Loss 20%
# priceItem = {"symbol": "AAVEUSD","price": 245.44}
# coinsDict = {"AAVEUSD": {"symbol": "AAVEUSD","price": 343.44, "priceTrends": [{"idx": 0,"price": 342.07},{"idx": 1,"price": 342.07},{"idx": 2,"price": 341.87},{"idx": 3,"price": 344.07},{"idx": 4,"price": 345.07},{"idx": 5,"price": 243.07}]}}
# hasSellCriteriaMet = PriceManager.hasSellCriteriaMet(priceItem, coinsDict)
# print(hasSellCriteriaMet)

# Scenario: Stop Loss 1.3%
# priceItem = {"symbol": "AAVEUSD","price": 282.50}
# coinsDict = {"AAVEUSD": {"symbol": "AAVEUSD","price": 343.44, "priceTrends": [{"idx": 0,"price": 342.07},{"idx": 1,"price": 342.07},{"idx": 2,"price": 341.87},{"idx": 3,"price": 344.07},{"idx": 4,"price": 345.07},{"idx": 5,"price": 290.07}]}}
# hasSellCriteriaMet = PriceManager.hasSellCriteriaMet(priceItem, coinsDict)
# print(hasSellCriteriaMet)


# Scenario: Gain 10%, Sell due to Downtrend
# priceItem = {"symbol": "AAVEUSD","price": 325.44}
# coinsDict = {"AAVEUSD": {"symbol": "AAVEUSD","price": 336.44, "priceTrends": [{"idx": 0,"price": 342.07},{"idx": 1,"price": 342.07},{"idx": 2,"price": 342.87},{"idx": 3,"price": 340.07},{"idx": 4,"price": 338.07},{"idx": 5,"price": 336.07}]}}
# hasSellCriteriaMet = PriceManager.hasSellCriteriaMet(priceItem, coinsDict)
# print(hasSellCriteriaMet)

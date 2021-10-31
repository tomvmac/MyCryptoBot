from core import PriceManager

# Load Binance Coins from file
coinsDict = PriceManager.loadBinanceCoins()
print(coinsDict)

# Load Current Price
print(PriceManager.getCurrentPrice("BTCUSD"))

# Load Current Prices
prices = PriceManager.getCurrentPrices()
print(prices)

# Update Current Prices to CoinsDict
# PriceManager.updateBinanceCoinsWithLatestPrices()

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


# Scenario: Gain 10%, Sell due to Downtrend -  MANA
# priceItem = {"symbol": "MANAUSD","price": 1.3112}
# coinsDict = {"MANAUSD":{"symbol":"MANAUSD","price":1.3112,"priceTrends":[{"idx":0,"price":0.9971},{"idx":1,"price":0.9971},{"idx":2,"price":0.9834},{"idx":3,"price":0.9834},{"idx":4,"price":1.0185},{"idx":5,"price":1.0185},{"idx":6,"price":1.2215},{"idx":7,"price":1.2215},{"idx":8,"price":1.3112},{"idx":9,"price":1.3112}]}}
# hasSellCriteriaMet = PriceManager.hasSellCriteriaMet(priceItem, coinsDict)
# print(hasSellCriteriaMet)

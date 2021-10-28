import BinanceClient

# Get Account Info
print(BinanceClient.getAccountInfo())

# Get Balance for a symbol
print("----------------")
print("Get Balance: ")
print(BinanceClient.getBalance("BTC"))
print("----------------")

# Get Price
print("----------------")
print("Get Price: ")
print(BinanceClient.getPrice("BTCUSD"))
print("----------------")

# Get Prices
print("----------------")
print("Get Prices: ")
print(BinanceClient.getPrices())
print("----------------")


# Buy Market Order
# print(buyMarketOrder("BTCUSDT", 0.1))

# Sell Market Order
# print(sellMarketOrder("BTCUSDT", 0.5))
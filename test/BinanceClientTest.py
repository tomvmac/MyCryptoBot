from core.api.binance import BinanceClient

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
# print(BinanceClient.buyMarketOrder("ONEUSD", 500))

# Sell Market Order
# print(BinanceClient.sellMarketOrder("USDTUSD", 50))
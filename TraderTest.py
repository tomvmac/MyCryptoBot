import Trader
import PriceManager

trade1 = {"symbol": "AAVEUSD", "type": "BUY", "tradeDate": "", "tradeTime": "", "status": "OPEN", "price": 286.20, "qty": 1}

# Open Trades
# print(Trader.openTrade(trade1))


# Close Trades
closeTrade = {"symbol": "AAVEUSD", "type": "BUY", "tradeDate": "10/25/2021", "tradeTime": "14:57:52", "status": "OPEN", "price": 286.20, "qty": 1}
print(Trader.closeTrade(closeTrade))

# --------------------------------------------------------------------------------------------------------------------------------------------------

# Create Buy TradeItem
# coinsDict = PriceManager.loadBinanceCoins()
# priceItem = {"symbol": "AAVEUSD", "price": 338.00}
# tradeItem = Trader.createBuyTradeItem(priceItem, coinsDict)
# print(tradeItem)

# Open Trade based on TradeItem
# tradeItem = Trader.openTrade(tradeItem)
# print(tradeItem)

# --------------------------------------------------------------------------------------------------------------------------------------------------

# Close newly created trade
# coinsDict = PriceManager.loadBinanceCoins()
# priceItem = {"symbol": "AAVEUSD", "price": 338.00}
# tradeItemNew = Trader.createSellTradeItem(priceItem, coinsDict)
# print(tradeItemNew)
# print(Trader.closeTrade(tradeItemNew))
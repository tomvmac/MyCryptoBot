import Trader
import PriceManager

trade1 = {"symbol": "CRVUSD", "type": "BUY", "tradeDate": "", "tradeTime": "", "status": "OPEN", "price": 4.00, "qty": 10}

# Open Trades
# print(Trader.openTrade(trade1))


# Close Trades
closeTrade = {"symbol": "CRVUSD", "type": "BUY", "tradeDate": "10/25/2021", "tradeTime": "14:57:52", "status": "OPEN", "price": 4.82, "qty": 10}
print(Trader.closeTrade(closeTrade))

# --------------------------------------------------------------------------------------------------------------------------------------------------

# Create TradeItem
# coinsDict = PriceManager.loadBinanceCoins()
# priceItem = {"symbol": "AAVEUSD", "price": 338.00}
# tradeItem = Trader.createTradeItem(priceItem, coinsDict)
# print(tradeItem)

# Open Trade based on TradeItem
# tradeItem = Trader.openTrade(tradeItem)
# print(tradeItem)

# --------------------------------------------------------------------------------------------------------------------------------------------------

# Close newly created trade
# tradeItemNew = {}
# tradeItemNew = Trader.getOpenTrade("AAVEUSD")
# print(tradeItemNew)
# print(Trader.closeTrade(tradeItemNew))
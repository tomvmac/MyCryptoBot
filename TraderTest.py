import Trader

trade1 = {"symbol": "ETHUSD", "type": "BUY", "tradeDate": "", "tradeTime": "", "status": "OPEN", "price": 4000, "qty": 10}
trade2 = {"symbol": "CRVUSD", "type": "BUY", "tradeDate": "", "tradeTime": "", "status": "OPEN", "price": 150, "qty": 10}

# Open Trades
print(Trader.openTrade(trade1))
print(Trader.openTrade(trade2))


# Close Trades
closeTrade = {"symbol": "CRVUSD", "type": "BUY", "tradeDate": "10/25/2021", "tradeTime": "14:57:52", "status": "OPEN", "price": 180, "qty": 10}
print(Trader.closeTrade(closeTrade))

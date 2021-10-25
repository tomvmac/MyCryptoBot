import Trader

trade1 = {"symbol": "ETHUSD", "type": "BUY", "tradeDate": "", "tradeTime": "", "status": "OPEN", "price": 4000, "qty": 10}
trade2 = {"symbol": "CRVUSD", "type": "BUY", "tradeDate": "", "tradeTime": "", "status": "OPEN", "price": 150, "qty": 10}


print(Trader.openTrade(trade1))
print(Trader.openTrade(trade2))



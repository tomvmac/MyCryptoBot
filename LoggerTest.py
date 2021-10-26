import Logger
import time

trade1 = {"symbol": "ETHUSD", "type": "BUY", "tradeDate": "", "tradeTime": "", "status": "OPEN", "price": 4000, "qty": 10}

Logger.GetLogger().info("This is the first message {x}".format(x=trade1))

time.sleep(3)
Logger.GetLogger().info("This is the second message")

time.sleep(5)
Logger.GetLogger().info("This is the final message")

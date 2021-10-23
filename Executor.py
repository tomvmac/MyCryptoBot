import sched
import time
import PriceManager

def initialize():
    # Initialize variables
    activeCoins = PriceManager.loadBinanceCoins()

def executeProcess():
    # Get Prices
    # prices = PriceManager.getCurrentPrices()
    # PriceManager.printPrices(prices, activeCoins)

    # Get BTC Price
    price = PriceManager.getCurrentPrice("BTCUSD")
    PriceManager.printPrice(price)


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------

# Schedule executions

scheduler = sched.scheduler(time.time, time.sleep)

while True:
    scheduler.enter(3, 1,executeProcess)
    scheduler.run()
import sched
import time

import Constants
import PriceManager


def executeProcess():
    # Get BTC Price
    price = PriceManager.getCurrentPrice("BTCUSD")
    PriceManager.printPrice(price)


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------

# Schedule executions

scheduler = sched.scheduler(time.time, time.sleep)

while True:
    scheduler.enter(Constants.SCHEDULE_EXECUTION_INTERVAL_IN_SECONDS, Constants.SCHEDULE_SLEEP_INTERVAL_IN_SECONDS,executeProcess)
    scheduler.run()
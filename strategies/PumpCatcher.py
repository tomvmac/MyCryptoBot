import sched
import time

from core.util import Constants
from core import PriceManager


def executeProcess():
    # Get BTC Price
    # price = PriceManager.getCurrentPrice("BTCUSD")
    # PriceManager.printPrice(price)

    PriceManager.processPrices()


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------

# Schedule executions

scheduler = sched.scheduler(time.time, time.sleep)

while True:
    scheduler.enter(Constants.SCHEDULE_EXECUTION_INTERVAL_IN_SECONDS, Constants.SCHEDULE_SLEEP_INTERVAL_IN_SECONDS, executeProcess)
    scheduler.run()
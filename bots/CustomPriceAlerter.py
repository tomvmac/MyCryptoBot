import sched
import time
import json

from core.util import SmsSender
from core.util import Constants
from core import PriceManager
from core.util import Logger

# Scheduling Parameters
SCHEDULE_EXECUTION_INTERVAL_IN_MINUTES = 5
SCHEDULE_EXECUTION_INTERVAL_IN_SECONDS = SCHEDULE_EXECUTION_INTERVAL_IN_MINUTES * 60
SCHEDULE_SLEEP_INTERVAL_IN_SECONDS = 1

def alertPrices():
    # Iterate through AlertCoins.json
    alertCoins = []
    alertMessage = ""
    with open(Constants.BINANCE_COINS_JSON_PATH, "r") as j:
        alertCoins = json.load(j)
    j.close()

    # Process each coin and each condition
    for alertCoin in alertCoins:
        for condition in alertCoin["conditions"]:
            if PriceManager.hasPriceMetCondition(alertCoin["symbol"], condition):
                alertMessage = alertCoin["symbol"] + " " + condition["comparisonType"] + " " + condition["comparator"] + " " + str(condition["conditionValue"])
                SmsSender.sendMsg(alertMessage)

    return


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------

# Schedule executions

# scheduler = sched.scheduler(time.time, time.sleep)
#
# while True:
#     scheduler.enter(SCHEDULE_EXECUTION_INTERVAL_IN_SECONDS, SCHEDULE_SLEEP_INTERVAL_IN_SECONDS, alertPrices)
#     scheduler.run()



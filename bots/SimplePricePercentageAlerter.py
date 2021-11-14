import sched
import time
import json

from core.util import SmsSender
from core.util import Constants
from core import PriceManager
from core.util import Logger
from core.util import DateTimeUtils

# Scheduling Parameters
SCHEDULE_EXECUTION_INTERVAL_IN_MINUTES = 15
SCHEDULE_EXECUTION_INTERVAL_IN_SECONDS = SCHEDULE_EXECUTION_INTERVAL_IN_MINUTES * 60
SCHEDULE_SLEEP_INTERVAL_IN_SECONDS = 1

pricePercentCondition = {
        "comparisonType": "PRICE_PERCENTAGE",
        "comparator": "IS_GREATER_THAN",
        "conditionValue": 3,
        "timeInterval": "15m"
}

def alertPrices():
    # Iterate through AlertCoins.json
    coins = []
    alertMessage = ""

    coins = PriceManager.getCurrentPrices()

    # sort symbols
    coins.sort(key=lambda x: x.get('symbol'))

    # Process each coin and each condition
    for coin in coins:
        alertMessage = "\r\n\r\n Coin Alert on " + str(DateTimeUtils.getCurrentDate()) + " at " + str(DateTimeUtils.getCurrentTime()) + ": " + coin["symbol"] + " " + pricePercentCondition["comparisonType"] + " " + pricePercentCondition["comparator"] + " " + str(pricePercentCondition["conditionValue"]) + " within " + pricePercentCondition["timeInterval"]

        if 'USDT' in coin['symbol']:
            if PriceManager.hasPriceMetCondition(coin, pricePercentCondition):
                SmsSender.sendMsg(alertMessage)
                Logger.GetLogger().info(alertMessage)

    return


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------

# Schedule executions

scheduler = sched.scheduler(time.time, time.sleep)

while True:
    scheduler.enter(SCHEDULE_EXECUTION_INTERVAL_IN_SECONDS, SCHEDULE_SLEEP_INTERVAL_IN_SECONDS, alertPrices)
    scheduler.run()



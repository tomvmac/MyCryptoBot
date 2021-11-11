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

pricePercentCondition = {
        "comparisonType": "PRICE_PERCENTAGE",
        "comparator": "IS_GREATER_THAN",
        "conditionValue": 2,
        "timeInterval": "15m"
}

def alertPrices():
    # Iterate through AlertCoins.json
    alertCoins = []
    alertMessage = ""
    with open(Constants.BINANCE_COINS_JSON_PATH, "r") as j:
        alertCoins = json.load(j)
    j.close()

    # sort symbols
    alertCoins.sort(key=lambda x: x.get('symbol'))

    # Process each coin and each condition
    for alertCoin in alertCoins:
        if 'USDT' in alertCoin['symbol']:
            if PriceManager.hasPriceMetCondition(alertCoin["symbol"], pricePercentCondition):
                alertMessage = alertCoin["symbol"] + " " + pricePercentCondition["comparisonType"] + " " + pricePercentCondition["comparator"] + " " + str(pricePercentCondition["conditionValue"])
                SmsSender.sendMsg(alertMessage)

    return


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------

# Schedule executions

scheduler = sched.scheduler(time.time, time.sleep)

while True:
    scheduler.enter(SCHEDULE_EXECUTION_INTERVAL_IN_SECONDS, SCHEDULE_SLEEP_INTERVAL_IN_SECONDS, alertPrices)
    scheduler.run()



import json
import Constants
import GeneralUtils


def openTrade(trade):
    # Update trade with today's date as transaction date and current time
    trade["tradeDate"] = GeneralUtils.getCurrentDate()
    trade["tradeTime"] = GeneralUtils.getCurrentTime()

    # Load OpenTrades.json
    openTrades = {}
    isTradeExists = False
    with open(Constants.OPEN_TRADES_JSON_PATH, "r") as j:
        openTrades = json.load(j)
    j.close()

    # Check to see if symbol already exist in openTrades, if so, don't add the trade.
    for openTrade in openTrades:
        if openTrade["symbol"] == trade["symbol"]:
            isTradeExists = True

    if isTradeExists == False:
        # Add trade to Open Trades
        openTrades.append(trade)


    with open(Constants.OPEN_TRADES_JSON_PATH, "w") as k:
        json.dump(openTrades, k)
    k.close()

    return openTrades


def closeTrade():
    # Close the Buy Trade
    # 1. Copy Buy Trade to Closed Trades
    # 2. Add Sell Trade to Closed Trades
    # 3. Remove Buy Trade from Open Trades
    return



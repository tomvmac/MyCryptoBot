import json
import Constants
import DateTimeUtils
import Logger
import WalletManager


def loadOpenTrades():
    openTrades = {}
    with open(Constants.OPEN_TRADES_JSON_PATH, "r") as j:
        openTrades = json.load(j)
    j.close()
    return openTrades

def getOpenTrade(symbol):
    openTrades = []
    with open(Constants.OPEN_TRADES_JSON_PATH, "r") as j:
        openTrades = json.load(j)
    j.close()

    for trade in openTrades:
        if trade["symbol"] == symbol:
            return trade

    return

def loadClosedTrades():
    closedTrades = {}
    with open(Constants.CLOSED_TRADES_JSON_PATH, "r") as j:
        closedTrades = json.load(j)
    j.close()
    return closedTrades

def openTrade(trade):
    # Update trade with today's date as transaction date and current time
    trade["status"] = "OPEN"
    trade["type"] = "BUY"
    trade["tradeDate"] = DateTimeUtils.getCurrentDate()
    trade["tradeTime"] = DateTimeUtils.getCurrentTime()

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

    Logger.GetLogger().info("Open Trade - {x}".format(x=trade))

    # Update Wallet
    wallet = WalletManager.loadWallet()

    # Add open trade to
    walletItemTrade = {}
    walletItemTrade["symbol"] = trade["symbol"]
    walletItemTrade["price"] = trade["price"]
    walletItemTrade["qty"] = trade["qty"]
    walletItemTrade["balance"] = 0
    WalletManager.updateWalletItem(wallet, walletItemTrade)

    # Deduct from Source Currency wallet
    tradeQtyInSourceCurrency = trade["qty"] * trade["price"]
    walletItemSourceCurrency = {}
    walletItemSourceCurrency["symbol"] = Constants.TRADING_SOURCE_CURRENCY_SYMBOL
    walletItemSourceCurrency["price"] = 1
    walletItemSourceCurrency["qty"] = -1 * tradeQtyInSourceCurrency
    walletItemSourceCurrency["balance"] = 0
    WalletManager.updateWalletItem(wallet, walletItemSourceCurrency)

    return openTrades


def closeTrade(trade):
    openTrades = {}
    closedTrades = {}
    previousBuyTrade = {}
    previousBuyTradeIdx = 0

    # Update trade with today's date as transaction date and current time
    trade["tradeDate"] = DateTimeUtils.getCurrentDate()
    trade["tradeTime"] = DateTimeUtils.getCurrentTime()
    trade["type"] = "SELL"
    trade["status"] = "CLOSED"

    # Load open and closed trades
    with open(Constants.OPEN_TRADES_JSON_PATH, "r") as j:
        openTrades = json.load(j)
    j.close()

    with open(Constants.CLOSED_TRADES_JSON_PATH, "r") as k:
        closedTrades = json.load(k)
    k.close()

    # Add Sell Trade to Closed Trades
    closedTrades.append(trade)

    # Find the Buy Trade
    for openTrade in openTrades:
        if openTrade["symbol"] == trade["symbol"]:
            previousBuyTrade = openTrade
            break

        previousBuyTradeIdx += 1

    # Copy Buy Trade to Closed Trades
    previousBuyTrade["status"] = "CLOSED"
    closedTrades.append(previousBuyTrade)

    # Remove Buy Trade from Open Trades
    del openTrades[previousBuyTradeIdx]


    # Write open & close trades
    with open(Constants.OPEN_TRADES_JSON_PATH, "w") as l:
        json.dump(openTrades, l)
    l.close()

    with open(Constants.CLOSED_TRADES_JSON_PATH, "w") as m:
        json.dump(closedTrades, m)
    m.close()

    # Update Wallet
    wallet = WalletManager.loadWallet()
    # Add close trade to
    walletItemTrade = {}
    walletItemTrade["symbol"] = trade["symbol"]
    walletItemTrade["price"] = trade["price"]
    walletItemTrade["qty"] = -1 * trade["qty"]
    walletItemTrade["balance"] = 0
    WalletManager.updateWalletItem(wallet, walletItemTrade)

    # Deduct from Source Currency wallet
    tradeQtyInSourceCurrency = trade["qty"] * trade["price"]
    walletItemSourceCurrency = {}
    walletItemSourceCurrency["symbol"] = Constants.TRADING_SOURCE_CURRENCY_SYMBOL
    walletItemSourceCurrency["price"] = 1
    walletItemSourceCurrency["qty"] = tradeQtyInSourceCurrency
    walletItemSourceCurrency["balance"] = 0
    WalletManager.updateWalletItem(wallet, walletItemSourceCurrency)



    Logger.GetLogger().info("Close Trade - {x}".format(x=trade))

    return closedTrades

def createTradeItem(priceItem, coinsDict):
    tradeItem = {}
    tradeItem["symbol"] = priceItem["symbol"]
    tradeItem["price"] = coinsDict[priceItem["symbol"]]["price"]

    # Calculate Qty
    qty = Constants.TRADING_UNIT_AMOUNT / coinsDict[priceItem["symbol"]]["price"]
    tradeItem["qty"] = qty

    return tradeItem

import json
import Constants


def writeToFile(data, fileName):
    with open(fileName, "w") as k:
        json.dump(data, k)
    k.close()

def truncateFile(fileName):
    with open(fileName, "w") as k:
        k.truncate(0)
    k.close()


def initializeFiles():
    # Clear Log Files
    truncateFile(Constants.APP_LOG_FILE_PATH)

    # Open Trades
    openTrades = []
    writeToFile(openTrades, Constants.OPEN_TRADES_JSON_PATH)

    # Closed Trades
    closedTrades = []
    writeToFile(closedTrades, Constants.CLOSED_TRADES_JSON_PATH)

    # Wallet
    wallet = [{"symbol": "USD", "price": 1, "qty": 10000, "balance": 10000}]
    writeToFile(wallet, Constants.WALLET_JSON_PATH)



import json
import Constants
import PriceManager

def loadWallet():
    wallet = {}
    with open(Constants.WALLET_JSON_PATH, "r") as j:
        wallet = json.load(j)
    j.close()

    # Get latest prices
    coins = PriceManager.updateBinanceCoinsWithLatestPrices()

    for item in wallet:
        if item["symbol"] in coins:
            item["price"] = coins[item["symbol"]]["price"]
            item["balance"] = item["price"] * item["qty"]

    return wallet

def updateWalletItem(wallet, itemToUpdate):
    # loop through wallet, if itemExists, add it, and return

    # add item after loop, assuming it was not there


    return


def deleteWalletItem(wallet, itemToDelete):
    itemIndex = 0
    for item in wallet:
        if item["symbol"] == itemToDelete["symbol"]:
            del wallet[itemIndex]
            # Remove from json file
            with open(Constants.WALLET_JSON_PATH, "w") as k:
                json.dump(wallet, k)
            k.close()
            return wallet
        itemIndex += 1

    return wallet

# ---------------------------------------------------------------------------------
# driver code
wallet = loadWallet()
print(wallet)

# delete item from wallet
item = {}
item["symbol"] = "BNBUSD"
wallet = deleteWalletItem(wallet, item)
print(wallet)
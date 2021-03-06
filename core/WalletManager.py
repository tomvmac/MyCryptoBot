import json

from core import PriceManager
from core.util import Constants, Logger


def loadWallet(strategyConfigs):
    wallet = {}
    with open(Constants.WALLET_JSON_PATH, "r") as j:
        wallet = json.load(j)
    j.close()

    # Get latest prices
    coins = PriceManager.updateBinanceCoinsWithLatestPrices(strategyConfigs)

    for item in wallet:
        if item["symbol"] in coins:
            item["price"] = coins[item["symbol"]]["price"]
        item["balance"] = item["price"] * item["qty"]

    return wallet

def getTotalWalletBalance(strategyConfigs):
    totalWalletBalance = 0

    with open(Constants.WALLET_JSON_PATH, "r") as j:
        wallet = json.load(j)
    j.close()

    # Get latest prices
    coins = PriceManager.updateBinanceCoinsWithLatestPrices(strategyConfigs)

    for item in wallet:
        if item["symbol"] == "USD":
            totalWalletBalance += item["price"] * item["qty"]

        if item["symbol"] in coins:
            item["price"] = coins[item["symbol"]]["price"]
            totalWalletBalance += item["price"] * item["qty"]

    return totalWalletBalance

def updateWalletItem(wallet, itemToUpdate):
    isItemInWallet = False

    # Loop through wallet, if itemExists, update, and return
    # itemToUpdate = {"symbol": "USD", "qty": "100"}
    for item in wallet:
        if item["symbol"] == itemToUpdate["symbol"]:
            isItemInWallet = True
            item["qty"] = itemToUpdate["qty"]

    # Add item after loop, assuming it was not there
    if isItemInWallet == False:
       wallet.append(itemToUpdate)

    # update Wallet.json file
    with open(Constants.WALLET_JSON_PATH, "w") as k:
        json.dump(wallet, k)
    k.close()

    Logger.GetLogger().info("Update Wallet Item - {x}".format(x=itemToUpdate))

    return wallet


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

    Logger.GetLogger().info("Update Wallet Item - {x}".format(x=itemToDelete))

    return wallet

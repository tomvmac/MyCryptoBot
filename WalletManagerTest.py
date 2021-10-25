import WalletManager

# Load wallet from file and fill in price and balance
wallet = WalletManager.loadWallet()
print(wallet)

# Delete item from wallet and save to wallet json file
# item = {}
# item["symbol"] = "BNBUSD"
# wallet = WalletManager.deleteWalletItem(wallet, item)
# print(wallet)


# Update item on wallet
# itemToUpdate = {"symbol": "USD", "qty": 100.10}
itemToUpdate = {"symbol": "ETCUSD", "qty": 5005}
wallet = WalletManager.updateWalletItem(wallet, itemToUpdate)
print(wallet)
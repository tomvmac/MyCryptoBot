import WalletManager

# Load wallet from file and fill in price and balance
wallet = WalletManager.loadWallet()
print(wallet)

# Delete item from wallet and save to wallet json file
# item = {}
# item["symbol"] = "BNBUSD"
# wallet = WalletManager.deleteWalletItem(wallet, item)
# print(wallet)

# Get Total Balance
print(WalletManager.getTotalWalletBalance())



# Update item on wallet
itemToUpdate1 = {
    "symbol": "USD",
    "price": 1,
    "qty": -1000,
    "balance": 500
  }

itemToUpdate2 = {
    "symbol": "BNBUSD",
    "price": 483.8602,
    "qty": 2,
    "balance": 483.8602
  }
# wallet = WalletManager.updateWalletItem(wallet, itemToUpdate1)
# wallet = WalletManager.updateWalletItem(wallet, itemToUpdate2)
# print(wallet)
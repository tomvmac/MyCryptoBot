import WalletManager

# Load wallet from file and fill in price and balance
wallet = WalletManager.loadWallet()
print(wallet)

# Delete item from wallet and save to wallet json file
item = {}
item["symbol"] = "BNBUSD"
wallet = WalletManager.deleteWalletItem(wallet, item)
print(wallet)


# Update item on wallet
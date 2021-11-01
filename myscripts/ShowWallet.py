from core import WalletManager
import MyConfigs

# Get Total Balance
print("Wallet Balance:", WalletManager.getTotalWalletBalance(MyConfigs.getStrategyConfigs()))
print("Wallet Details:")
print("------------------------------------------------------------------------------------")
# Load wallet from file and fill in price and balance
wallet = WalletManager.loadWallet(MyConfigs.getStrategyConfigs())
print(wallet)



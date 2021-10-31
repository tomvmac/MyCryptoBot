import os

# API
# LIVE
LIVE_BINANCE_API_KEY = os.environ.get('LIVE_BINANCE_API_KEY')
LIVE_BINANCE_SECRET = os.environ.get('LIVE_BINANCE_SECRET')
LIVE_BINANCE_API_URL = 'https://api.binance.us/api'
# TEST
TEST_BINANCE_API_KEY = os.environ.get('TEST_BINANCE_API_KEY')
TEST_BINANCE_SECRET = os.environ.get('TEST_BINANCE_SECRET')
TEST_BINANCE_API_URL = 'https://testnet.binance.vision/api'

# File Paths
BINANCE_COINS_JSON_PATH = "../data/BinanceCoins.json"
WALLET_JSON_PATH = "../data/Wallet.json"
OPEN_TRADES_JSON_PATH = "../data/OpenTrades.json"
CLOSED_TRADES_JSON_PATH = "../data/ClosedTrades.json"

# Log Files
APP_LOG_FILE_PATH = "../logs/app.log"

# Date and Time Configs
TIME_ZONE_EDT = "America/New_York"
DATE_FORMAT = "%m/%d/%Y"
TIME_FORMAT = "%H:%M:%S"



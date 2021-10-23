import os

# API
# LIVE
LIVE_BINANCE_API_KEY = os.environ.get('live_binance_api_key')
LIVE_BINANCE_SECRET = os.environ.get('live_binance_secret')
LIVE_BINANCE_API_URL = 'https://api.binance.us/api'
# TEST
TEST_BINANCE_API_KEY = os.environ.get('test_binance_api_key')
TEST_BINANCE_SECRET = os.environ.get('test_binance_secret')
TEST_BINANCE_API_URL = 'https://testnet.binance.vision/api'

# File Paths
BINANCE_COINS_JSON_PATH = "data/BinanceCoins.json"


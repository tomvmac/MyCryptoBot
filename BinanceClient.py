from binance.client import Client
import Constants

def getClient():
    client = Client(Constants.LIVE_BINANCE_API_KEY, Constants.LIVE_BINANCE_SECRET)
    client.API_URL = Constants.LIVE_BINANCE_API_URL
    return client




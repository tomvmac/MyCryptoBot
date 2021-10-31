from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceOrderException

from core.util import Constants

client = Client(Constants.LIVE_BINANCE_API_KEY, Constants.LIVE_BINANCE_SECRET)
client.API_URL = Constants.LIVE_BINANCE_API_URL

def getAccountInfo():
    # get balances for all assets & some account information
    return client.get_account()

def getBalance(symbol):
    # get balance for a specific asset only (BTC)
    return client.get_asset_balance(asset=symbol)

def getPrice(symbol):
    # get balance for a specific asset only (BTC)
    return client.get_symbol_ticker(symbol=symbol)

def getHistoricalPrices(symbol, interval, startTimestamp):
    # valid intervals - 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M

    # get timestamp of earliest date data is available
    #timestamp = client._get_earliest_valid_timestamp(symbol, interval)

    # request historical candle (or klines) data
    bars = client.get_historical_klines(symbol, interval, startTimestamp, limit=100)

    return bars

def getPrices():
    # get latest price from Binance API
    prices = client.get_symbol_ticker()
    return prices

def buyMarketOrder(symbol, qty):
    # create a real order if the test orders did not raise an exception

    try:
        order = client.order_market_buy(symbol=symbol,quantity=qty)
        return order

    except BinanceAPIException as e:
        # error handling goes here
        print(e)
    except BinanceOrderException as e:
        # error handling goes here
        print(e)


def sellMarketOrder(symbol, qty):
    # create a real order if the test orders did not raise an exception

    try:
        order = client.order_market_sell(symbol=symbol,quantity=qty)
        return order

    except BinanceAPIException as e:
        # error handling goes here
        print(e)
    except BinanceOrderException as e:
        # error handling goes here
        print(e)




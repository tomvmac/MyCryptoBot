# MyCryptoBot
MyCryptoBot is a automated bot used for crypto price check and trading

## Summary
This is a project that uses Python to retrieve crypto currency pricing from Binance API and execute buy/sell trades based on pricing scenarios.

## Software Installation
1. Install Python 3.x and Pip3 from https://www.python.org/

## Python Module Installation
###Binance Python Client 
```
> pip install python-binance
```

###Schedule 
```
> pip install schedule
```

## Configuration
The following environment variables are required.  Test env variables are ONLY required to connect to test Binance.
```
TEST_BINANCE_API_KEY
TEST_BINANCE_SECRET
LIVE_BINANCE_API_KEY
LIVE_BINANCE_SECRET
```


## Key Components

|  Component | Description   | 
|---|---|
|  Constants | Provides constants for configurable settings such as keys, secrets, urls, file paths, etc.    |
|  Executor  | Performs the execution of the entire process including initialization, scheduling, and execution.  |  
|  PriceManager | Checks prices of each coin and determines to trade or not and updates the last prices on file.  |   
|  Trader | Executes trades (open/close) and records the details of each trade.  |  
|  WalletManager | Provides wallet management for quantity of coins available in the wallet.   |  
 


## Resources

### Binance Official API Guide
https://github.com/binance-us/binance-official-api-docs/blob/master/rest-api.md#general-api-information

### Python Binance Client
https://algotrading101.com/learn/binance-python-api-guide/



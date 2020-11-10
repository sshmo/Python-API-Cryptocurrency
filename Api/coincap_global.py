# Ian Annase
# Mastering The CoinMarketCap API with Python3
# Updated by Shabbir Mousavi 2020

import dateutil.parser
from datetime import datetime
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

convert = 'USD'

url = 'https://sandbox-api.coinmarketcap.com/v1/global-metrics/quotes/latest'
parameters = {
    # 'start':'1',
    # 'limit':'10',
    'convert': convert
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c',
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    results = response.json()
    # print(json.dumps(results, sort_keys=True, indent=4))
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

active_cryptocurrencies = results['data']["active_cryptocurrencies"]
active_exchanges = results['data']["active_exchanges"]
active_market_pairs = results['data']["active_market_pairs"]
bitcoin_dominance = results['data']["btc_dominance"]
ethereum_dominance = results['data']["eth_dominance"]

# from https://stackoverflow.com/a/15228038
last_updated = dateutil.parser.isoparse(results['data']["last_updated"])

global_cap = int(results['data']["quote"][convert]["total_market_cap"])
global_volume = int(results['data']["quote"][convert]["total_volume_24h"])

active_currencies_string = f'{active_cryptocurrencies:,}'
active_markets_string = f'{active_market_pairs:,}'
global_cap_string = f'{global_cap:,}'
global_volume_string = f'{global_volume:,}'
date = (
    str(last_updated.year)
    + "-"
    + str(last_updated.month).zfill(2)
    + "-"
    + str(last_updated.day).zfill(2)
)

print()

print(
    'There are currently',
    active_currencies_string,
    'active cryptocurrecies and',
    active_markets_string,
    'active markets.',
)

print(
    'The global cap of all cryptos is',
    global_cap_string,
    'and the 24h global volume is',
    global_volume_string + '.',
)

print(
    'Bitcoin\'s total percentage of the global cap is',
    str(bitcoin_dominance) + '%.',
)

print()

print('This information was last updated on', date + '.')

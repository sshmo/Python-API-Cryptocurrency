# Ian Annase
# Mastering The CoinMarketCap API with Python3
# Updated by Shabbir Mousavi 2020

import json
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import dateutil.parser


convert = 'USD'  # JPY

url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
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
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)


data = results['data']
#print(json.dumps(data, indent=4))

print()

print(
    f'{"Rank":<4}',
    f'{"Name":<23}',
    f'{"Symbol":<6}',
    f'{"Date added":<10}',
)

for currency in data:
    currency_id = currency['id']
    rank = currency['cmc_rank']
    name = currency['name']
    symbol = currency['symbol']
    date_added = dateutil.parser.isoparse(currency['date_added'])
    date = (
        str(date_added.year)
        + "-"
        # from https://stackoverflow.com/a/3371180
        + str(date_added.month).zfill(2)
        + "-"
        + str(date_added.day).zfill(2)
    )
    print(
        f'{rank:<4}',
        f'{name:<23}',
        f'{symbol:<6}',
        f'{date:<10}',
    )
print()

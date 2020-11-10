# Ian Annase
# Mastering The CoinMarketCap API with Python3
# Updated by Shabbir Mousavi 2020

import json
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

convert = 'USD'

url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
url_end = '?symbol='

while True:

    print()
    choice = input("Enter the ticker symbol of a cryptocurrency: ")
    choice = choice.upper()

    parameters = {
    'convert': convert
    }

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c',
    }

    session = Session()
    session.headers.update(headers)
    choice_url = url + url_end + choice

    try:
        response = session.get(choice_url, params=parameters)
        results = response.json()
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

    #print(json.dumps(results, sort_keys=True, indent=4))

    currency = results['data'][choice]
    rank = currency['cmc_rank']
    name = currency['name']
    symbol = currency['symbol']
    circulating_supply = int(currency['circulating_supply'])
    total_supply = int(currency['total_supply'])

    quote = currency['quote'][convert]
    market_cap = quote['market_cap']
    hour_change = quote['percent_change_1h']
    day_change = quote['percent_change_24h']
    week_change = quote['percent_change_7d']
    price = quote['price']
    volume = quote['volume_24h']

    volume_string = f'{volume:,.2f}'
    market_cap_string = f'{market_cap:,.2f}'
    circulating_supply_string = f'{circulating_supply:,}'
    total_supply_string = f'{total_supply:,}'

    print(str(rank) + ': ' + name + ' (' + symbol + ')')
    print('Market cap: \t\t$' + market_cap_string)
    print('Price: \t\t\t$' + f'{price:0.2f}')
    print('24h Volume: \t\t$' + volume_string)
    print('Hour change: \t\t' + f'{hour_change:0.3f}' + '%')
    print('Day change: \t\t' + f'{day_change:0.3f}' + '%')
    print('Week change: \t\t' + f'{week_change:0.3f}' + '%')
    print('Circulating supply: \t' + circulating_supply_string)
    print('Percentage of coins in circulation: ' + str(int(circulating_supply / total_supply * 100)))
    print()

    choice = input('Again? (y/n): ')

    if choice == 'n':
        break
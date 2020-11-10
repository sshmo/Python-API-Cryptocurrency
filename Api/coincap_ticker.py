# Ian Annase
# Mastering The CoinMarketCap API with Python3
# Updated by Shabbir Mousavi 2020

import json
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

convert = 'USD'

while True:

    url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

    parameters = {
        'start': '1',
        'limit': '10',
        'convert': convert
    }

    choice = input("Do you want to enter any custom parameters? (y/n): ")

    if choice == 'y':
        limit = input('What is the custom limit?: ')
        start = input('What is the custom start number?: ')
        sort = input(
            'What do you want to sort by?:\n some valid values:\n "market_cap" "name" "symbol" "date_added" "market_cap" "price"\n "circulating_supply" "total_supply" "max_supply" "num_market_pairs"\n'
        )
        convert = input('What is your local currency?:\n(pass a comma-separated list of cryptocurrencies.)\n'
                        )

        parameters = {
            'start': start,
            'limit': limit,
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

    #print(json.dumps(results, indent=4))

    data = results['data']

    print()
    for currency in data:
        
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
        print('Total supply: \t\t' + total_supply_string)
        print('Circulating supply: \t' + circulating_supply_string)
        print('Percentage of coins in circulation: ' +
              str(int(circulating_supply / total_supply * 100)))
        print()

    choice = input('Again? (y/n): ')

    if choice != 'y':
        break

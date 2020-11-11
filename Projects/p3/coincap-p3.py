import json
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from datetime import datetime
import dateutil.parser
from prettytable import PrettyTable
from colorama import Fore, Back, Style

convert = 'USD'

url = 'https://sandbox-api.coinmarketcap.com/v1/global-metrics/quotes/latest'

parameters = {
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

data = results['data']
global_cap = int(data['quote'][convert]['total_market_cap'])
global_cap_string = f'{global_cap:,}'

while True:

    print()
    print('CoinMarketCap Explorer Menu')
    print('The global market cap is $' + global_cap_string)
    print()
    print('1 - Top 100 sorted by rank')
    print('2 - Top 100 sorted by 24 hour change')
    print('3 - Top 100 sorted by 24 hour volume')
    print('0 - Exit')
    print()
    choice = input('What is your choice? (1-3): ')

    ticker_url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

    if choice == '1':
        ticker_url += '?start=1&limit=100'
    if choice == '2':
        ticker_url += '?start=1&limit=100&sort=percent_change_24h'
    if choice == '3':
        ticker_url += '?start=1&limit=100&sort=volume_24h'
    if choice == '0':
        break


    try:
        response = session.get(ticker_url, params=parameters)
        results = response.json()
        # print(json.dumps(results, sort_keys=True, indent=4))
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

    data = results['data']

    table = PrettyTable(
        ['Rank', 'Asset', 'Price', 'Market Cap', 'Volume', '1h', '24h', '7d'])

    print()
    for currency in data:
        rank = currency['cmc_rank']
        name = currency['name']
        symbol = currency['symbol']
        quote = currency['quote'][convert]
        market_cap = quote['market_cap']
        hour_change = quote['percent_change_1h']
        day_change = quote['percent_change_24h']
        week_change = quote['percent_change_7d']
        price = quote['price']
        volume = quote['volume_24h']

        if hour_change is not None:
            if hour_change > 0:
                hour_change = Back.GREEN + \
                    str(hour_change) + '%' + Style.RESET_ALL
            else:
                hour_change = Back.RED + \
                    str(hour_change) + '%' + Style.RESET_ALL

        if day_change is not None:
            if day_change > 0:
                day_change = Back.GREEN + \
                    str(day_change) + '%' + Style.RESET_ALL
            else:
                day_change = Back.RED + str(day_change) + '%' + Style.RESET_ALL

        if week_change is not None:
            if week_change > 0:
                week_change = Back.GREEN + \
                    str(week_change) + '%' + Style.RESET_ALL
            else:
                week_change = Back.RED + \
                    str(week_change) + '%' + Style.RESET_ALL

        if volume is not None:
            volume_string = '{:,}'.format(volume)

        if market_cap is not None:
            market_cap_string = '{:,}'.format(market_cap)

        table.add_row([rank,
                       name + ' ( ' + symbol + ')',
                       '$' + str(price),
                       '$' + str(market_cap),
                       '$' + volume_string,
                       str(hour_change),
                       str(day_change),
                       str(week_change)])

    print()
    print(table)
    print()

    choice = input('Again? (y/n): ')

    if choice == 'n':
        break

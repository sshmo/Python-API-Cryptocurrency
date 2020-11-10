import json
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from datetime import datetime
import dateutil.parser
from prettytable import PrettyTable
from colorama import Fore, Back, Style

convert = 'USD'

url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
url_end = '?symbol='


print()
print('MY PORTFOLIO')
print()

portfolio_value = 0.00
last_updated = 0

table = PrettyTable(['Asset', 'Amount Owned', convert +
                     ' Value', 'Price', '1h', '24h', '7d'])

with open('portfolio.txt') as inp:
    for line in inp:
        symbol, amount = line.split()
        symbol = symbol.upper()

        symbol_url = url + url_end + symbol

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
            response = session.get(symbol_url, params=parameters)
            results = response.json()
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)

        #print(json.dumps(results, sort_keys=True, indent=4))

        currency = results['data'][symbol]
        rank = currency['cmc_rank']
        name = currency['name']
        last_updated = dateutil.parser.isoparse(currency['last_updated'])
        symbol = currency['symbol']

        quote = currency['quote'][convert]
        hour_change = quote['percent_change_1h']
        day_change = quote['percent_change_24h']
        week_change = quote['percent_change_7d']
        price = quote['price']

        value = float(price) * float(amount)

        if hour_change > 0:
            hour_change = Back.GREEN + f'{hour_change:.3f}' + '%' + Style.RESET_ALL
        else:
            hour_change = Back.RED + f'{hour_change:.3f}' + '%' + Style.RESET_ALL

        if day_change > 0:
            day_change = Back.GREEN + f'{day_change:.3f}' + '%' + Style.RESET_ALL
        else:
            day_change = Back.RED + f'{day_change:.3f}' + '%' + Style.RESET_ALL

        if week_change > 0:
            week_change = Back.GREEN + f'{week_change:.3f}' + '%' + Style.RESET_ALL
        else:
            week_change = Back.RED + f'{week_change:.3f}' + '%' + Style.RESET_ALL

        portfolio_value += value

        value_string = '{:,}'.format(round(value, 2))

        table.add_row([name + ' (' + symbol + ')',
                       amount,
                       '$' + value_string,
                       '$' + f'{price:.2f}',
                       str(hour_change),
                       str(day_change),
                       str(week_change)])

print(table)
print()

portfolio_value_string = '{:,}'.format(round(portfolio_value, 2))
last_updated_string = last_updated.strftime('%B %d, %Y at %I:%M%p')

print('Total Portfolio Value: ' + Back.GREEN +
      '$' + portfolio_value_string + Style.RESET_ALL)
print()
print('API Results Last Updated on ' + last_updated_string)
print()
import json
import time
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from datetime import datetime
import dateutil.parser
import subprocess

convert = 'USD'

url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
url_end = '?symbol='


print()
print('ALERTS TRACKING...')
print()

already_hit_symbols = []

while True:
    with open('alerts.txt') as inp:
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
            name = currency['name']
            last_updated = dateutil.parser.isoparse(currency['last_updated'])
            symbol = currency['symbol']
            quote = currency['quote'][convert]
            price = quote['price']

            if float(price) >= float(amount) and symbol not in already_hit_symbols:

                message = f"{name} hit {amount}!!!"
                # from https://askubuntu.com/a/108774
                subprocess.Popen(['notify-send', message])

                last_updated_string = last_updated.strftime(
                    '%B %d, %Y at %I:%M%p')
                print(name + ' hit ' + amount + ' on ' + last_updated_string)
                already_hit_symbols.append(symbol)

    print('...')
    time.sleep(3)

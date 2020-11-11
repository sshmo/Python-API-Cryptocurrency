import math
import json
import locale
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from prettytable import PrettyTable

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')


global_url = 'https://sandbox-api.coinmarketcap.com/v1/global-metrics/quotes/latest'
ticker_url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c',
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(global_url)
    results = response.json()
    # print(json.dumps(results, sort_keys=True, indent=4))
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

data = results['data']

global_cap = int(data['quote']['USD']['total_market_cap'])

table = PrettyTable(['Name', 'Ticker', '% of total global cap', 'Current', '7.7T (Gold)', '36.8T (Narrow Money)',
                     '73T (World Stock Markets)', '90.4T (Broad Money)', '217T (Real Estate)', '544T (Derivatives)'])

try:
    response = session.get(ticker_url)
    results = response.json()
    # print(json.dumps(results, sort_keys=True, indent=4))
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

data = results['data']

for currency in data:
    name = currency['name']
    ticker = currency['symbol']
    percentage_of_global_cap = float(
        currency['quote']['USD']['market_cap']) / float(global_cap)

    current_price = round(float(currency['quote']['USD']['price']), 2)
    available_supply = float(currency['total_supply'])

    # https://www.visualcapitalist.com/all-of-the-worlds-money-and-markets-in-one-visualization-2020/
    trillion7price = round(
        7700000000000 * percentage_of_global_cap / available_supply, 2)
    trillion36price = round(
        36000000000000 * percentage_of_global_cap / available_supply, 2)
    trillion73price = round(
        73000000000000 * percentage_of_global_cap / available_supply, 2)
    trillion90price = round(
        90400000000000 * percentage_of_global_cap / available_supply, 2)
    trillion217price = round(
        217000000000000 * percentage_of_global_cap / available_supply, 2)
    trillion544price = round(
        544000000000000 * percentage_of_global_cap / available_supply, 2)

    percentage_of_global_cap_string = str(
        round(percentage_of_global_cap*100, 2)) + '%'
    current_price_string = '$' + str(current_price)
    trillion7price_string = '$' + locale.format('%.2f', trillion7price, True)
    trillion36price_string = '$' + locale.format('%.2f', trillion36price, True)
    trillion73price_string = '$' + locale.format('%.2f', trillion73price, True)
    trillion90price_string = '$' + locale.format('%.2f', trillion90price, True)
    trillion217price_string = '$' + \
        locale.format('%.2f', trillion217price, True)
    trillion544price_string = '$' + \
        locale.format('%.2f', trillion544price, True)

    table.add_row([name,
                   ticker,
                   percentage_of_global_cap_string,
                   current_price_string,
                   trillion7price_string,
                   trillion36price_string,
                   trillion73price_string,
                   trillion90price_string,
                   trillion217price_string,
                   trillion544price_string])

print()
print(table)
print()

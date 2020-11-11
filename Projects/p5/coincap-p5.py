import xlsxwriter
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

start = 1
f = 1

crypto_workbook = xlsxwriter.Workbook('cryptocurrencies.xlsx')
crypto_sheet = crypto_workbook.add_worksheet()

crypto_sheet.write('A1', 'Name')
crypto_sheet.write('B1', 'Symbol')
crypto_sheet.write('C1', 'Market Cap')
crypto_sheet.write('D1', 'Price')
crypto_sheet.write('E1', '24H Volume')
crypto_sheet.write('F1', 'Hour Change')
crypto_sheet.write('G1', 'Day Change')
crypto_sheet.write('H1', 'Week Change')

for i in range(10):
    ticker_url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=' + \
        str(start)

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c',
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(ticker_url)
        results = response.json()
        # print(json.dumps(results, sort_keys=True, indent=4))
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

    data = results['data']

    for currency in data:
        rank = currency['cmc_rank']
        name = currency['name']
        symbol = currency['symbol']
        quote = currency['quote']['USD']
        market_cap = quote['market_cap']
        hour_change = quote['percent_change_1h']
        day_change = quote['percent_change_24h']
        week_change = quote['percent_change_7d']
        price = quote['price']
        volume = quote['volume_24h']

        crypto_sheet.write(f, 0, name)
        crypto_sheet.write(f, 1, symbol)
        crypto_sheet.write(f, 2, str(market_cap))
        crypto_sheet.write(f, 3, str(price))
        crypto_sheet.write(f, 4, str(volume))
        crypto_sheet.write(f, 5, str(hour_change))
        crypto_sheet.write(f, 6, str(day_change))
        crypto_sheet.write(f, 7, str(week_change))

        f += 1

    start += 100

crypto_workbook.close()

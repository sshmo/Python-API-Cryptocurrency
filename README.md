# Python-API-Cryptocurrency

(*This project is an updated version of: ['Python-And-Cryptocurrencies-2018'](https://github.com/phennaux/Python-and-cryptocurrencies) created by Philippe Hennaux that was entirely made thanks to an Udemy course created by Ian Annase ['Python & Cryptocurrency: Build 5 Real World Applications-2018'](https://www.udemy.com/coinmarketcap/) The Public API that was used in 2018 version of the cource, was changed to ['Professional API'](https://coinmarketcap.com/api/) in 2018. Since then a lot of changes has occured.*)


In this project we use the __*sandbox version*__  of ['CoinMarketCap'](https://coinmarketcap.com) API with the corresponding sandbox API key to retrieve data from ['CoinMarketCap'](https://coinmarketcap.com).

The CoinMarketCap API is a suite of high-performance RESTful JSON endpoints. ['See documentation'](https://coinmarketcap.com/api/documentation/v1/#)

This Python project has 5 sub-projects using sample cryptocurrency data from ['sandbox-api.coinmarketcap.com'](https://sandbox-api.coinmarketcap.com).


__*For obtaining live results*__, replace the url and API key in each python file as following:

1. replace:

    'sandbox-api.coinmarketcap.com' 
    with 
    'pro-api.coinmarketcap.com'

2. replace: 

    'X-CMC_PRO_API_KEY': 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c' 
    with
    'X-CMC_PRO_API_KEY': 'your API key'


The libraries used in this project are:

- **Prettytables** In order to display data into a table.
- **Colorama** In order to add colors to a table.
- **Requests** In order to request files, in this case JSON files.
- **json** In order to convert json files to readable python objects.
- **Datetime** In order to get the date and display it.
- **python-dateutil** In order to convert iso-date to datetime format.
- **autopep8** In order to convert python files to pep8 style.
- **xlsxwriter** In order to save python output to Excel file.


With these libraries and the CoinMarketCap API the projects that the course proposed to build are:

1. ***A Cryptocurrency Portfolio App***

    Track all of your crypto assets with ease. See the total value of all your crypto assets combined along with detailed information about each one. Positive and negative values are color coated green and red.

2. ***A Real-Time Price Alert App***

    Get notified when cryptocurrencies hit certain prices in USD. You can keep this program running in the background. Your computer will shout things like, 'Litecoin hit $1200!'.

3. ***A Top 100 Cryptocurreny Ranking App***

    Sort by rank, daily percentage change, or daily volume. Positive and negative values are color coated green and red.

4. ***Predict The Future Values of the Top 100 Cryptocurrencies***

    Explore what the price of cryptocurrencies will be if the global market cap hits certain levels (such as world stock market levels)

5. ***Store Real-Time Information on 1000 Cryptocurrencies in Excel using Python***

    Learn to store cryptocurrency information inside of excel workbooks using Python.

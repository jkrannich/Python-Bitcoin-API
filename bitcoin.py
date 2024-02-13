import requests

api_key = 'INSERT API KEY'  # API key excluded for security reasons

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

parameters = {
    'start':'1',
    'limit':'1',
    'convert':'USD'
}

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': api_key,
}

response = requests.get(url, headers=headers, params=parameters)

if response.status_code == 200:
    data = response.json()

    bitcoin_price = data['data'][0]['quote']['USD']['price']

    print(f'The current price of Bitcoin is ${bitcoin_price:.2f} USD.')
else:
    print(f'Error: {response.status_code} - {response.text}')

import requests

amount = int(input('Enter an amount of pounds: '))

response = requests.get('https://api.exchangerate-api.com/v4/latest/GBP')
exchange_rate = response.json()['rates']
usd_rate = exchange_rate['USD']
usd_amount = amount * usd_rate

us_dollars = usd_amount

print(f'{amount:.2f} GBP is equivalent to {us_dollars:.2f} USD')
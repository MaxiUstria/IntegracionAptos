import requests

r = requests.get(
    'https://api.mercadolibre.com/sites/MLU/search?category=MLU6393&q=%punta%20ballena%')
print(r.text)

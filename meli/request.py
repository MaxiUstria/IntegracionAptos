import requests
import sys
import json

brand = sys.argv[1]
r = requests.get(
    "https://api.mercadolibre.com/sites/MLU/search?q={}&condition=new".format(brand))
itemsQuantity = json.loads(r.text)['paging']["total"]
items = []
offset = 0
while len(items) < itemsQuantity and len(items) <= 1000:
    for item in json.loads(r.text)['results']:
        item = {
            "id": item["id"],
            "nombre": item['title'],
            "precio": item['price'],
            "moneda": item['currency_id'],
            "link": item['permalink'],
            "foto": item['thumbnail'],
            "domain": item["domain_id"]
        }
        items.append(item)
    offset = offset + 50
    r = requests.get(
    "https://api.mercadolibre.com/sites/MLU/search?q={}&condition=new&offset={}".format(brand, offset))
print(len(items))
import requests
import sys
import json

def meliClient(brand):
    ##brand = sys.argv[1]
    r = requests.get(
        "https://api.mercadolibre.com/sites/MLU/search?q={}&condition=new".format(brand))
    itemsQuantity = json.loads(r.text)['paging']["total"]
    items = []
    offset = 0
    while len(items) < itemsQuantity and len(items) <= 100:
        for item in json.loads(r.text)['results']:
            item = {
                "id": item["id"],
                "name": item['title'],
                "price": item['price'],
                "currency": item['currency_id'],
                "link": item['permalink'],
                "photo": item['thumbnail'],
                "domain": item["domain_id"]
            }
            items.append(item)
        offset = offset + 50
        r = requests.get(
        "https://api.mercadolibre.com/sites/MLU/search?q={}&condition=new&offset={}".format(brand, offset))
    print(len(items))
    return items
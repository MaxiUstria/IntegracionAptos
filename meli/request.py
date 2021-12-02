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
    while len(items) < itemsQuantity and len(items) <= 1000:
        for item in json.loads(r.text)['results']:
            modelo = ""
            for attribute in item["attributes"]:
                if attribute["id"] == "MODEL":
                    modelo = attribute["value_name"]

            category_switcher = {
                "MLU-CELLPHONES": "celulares y tablets",
                "MLU-TABLETS": "celulares y tablets",
                "MLU-SMARTWATCHES" : "Smartwatches y Bandas",
                "MLU-CELLPHONE_COVERS": "Accesorios",
                "MLU-WIRELESS_CHARGERS": "Accesorios",
                "MLU-HEADPHONES": "Perifericos",
                "MLU-REFRIGERATORS": "Electrodomésticos",
                "MLU-MICROWAVES": "Electrodomésticos",
                "MLU-TELEVISIONS": "Televisores",
                "MLU-NOTEBOOKS": "Notebooks",
                "MLU-COMPUTER_MONITORS": "Monitores",
            }

            item = {
                "id": item["id"],
                "name": item['title'],
                "price": item['price'],
                "currency": item['currency_id'],
                "link": item['permalink'],
                "photo": item['thumbnail'],
                "domain": category_switcher.get(item["domain_id"], "Otros"),
                "model": modelo
            }
            items.append(item)
        offset = offset + 50
        r = requests.get(
            "https://api.mercadolibre.com/sites/MLU/search?q={}&condition=new&offset={}".format(brand, offset))
    return items

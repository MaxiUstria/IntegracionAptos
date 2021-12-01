import sqlite3
from meli.request import meliClient
from loi.scraper import loiClient
import sys

brand = sys.argv[1]
conn = sqlite3.connect('brand_items_database')
c = conn.cursor()

c.execute('''
         CREATE TABLE IF NOT EXISTS items
         ([name] TEXT PRIMARY KEY, [category] TEXT, [price] TEXT, [currency] TEXT, [model] TEXT, [photo] TEXT, [description] TEXT)
         ''')

conn.commit()

meliResponse = meliClient(brand)
loiResponse = loiClient(brand)

for loiItem in loiResponse:
    loiItem['model'] = ''
    for meliItem in meliResponse:
        if loiItem["nombreCorto"].lower() in meliItem["name"].lower():
            meliResponse.remove(meliItem)
            loiItem["precio"] = (float(loiItem["precio"]) + float(meliItem['price'])) / 2
            loiItem["model"] = meliItem['model']


for meliItem in meliResponse:
    c.execute("""INSERT OR REPLACE INTO items VALUES(?, ?, ?, ?, ?, ?, ?)""",
              (meliItem["name"], meliItem["domain"], meliItem["price"], meliItem["currency"], meliItem["model"], meliItem["photo"], "",))

for loiItem in loiResponse:
    c.execute("""INSERT OR REPLACE INTO items VALUES(?, ?, ?, ?, ?, ?, ?)""",
              (loiItem["objeto"], loiItem["categoria"], loiItem["precio"], loiItem["moneda"], loiItem["model"], loiItem["foto"], loiItem["descripcion"]))

conn.commit()

import sqlite3
from meli.request import meliClient
from loi.scraper import loiClient
import sys

brand = sys.argv[1]
conn = sqlite3.connect('brand_items_database')
c = conn.cursor()

c.execute('''
         CREATE TABLE IF NOT EXISTS items
         ([itemId] TEXT PRIMARY KEY, [name] TEXT, [price] TEXT, [currency] TEXT, [link] TEXT, [photo] TEXT, [domain] TEXT, [platform] TEXT)
         ''')

conn.commit()

meliResponse = meliClient(brand)
loiResponse = loiClient(brand)

for loiItem in loiResponse:
    loiItem['model'] = ''
    for meliItem in meliResponse:
        if loiItem["nombreCorto"].lower() in meliItem["name"].lower():
            meliResponse.remove(meliItem)
            loiItem["precio"] = (loiItem["precio"] + meliItem['price']) / 2
            loiItem["model"] = meliItem['model']


for meliItem in meliResponse:
    c.execute("""INSERT OR REPLACE INTO items VALUES(?, ?, ?, ?, ?, ?, ?, ?)""",
              (meliItem["id"], meliItem["name"], meliItem["price"], meliItem["currency"], meliItem["link"], meliItem["photo"], meliItem["domain"], "meli",))

for loiItem in loiResponse:
    c.execute("""INSERT OR REPLACE INTO items VALUES(?, ?, ?, ?, ?, ?, ?, ?)""",
              (loiItem["nombre"], loiItem["nombreCorto"], loiItem["precio"], loiItem["moneda"], loiItem["link"], "", "", "loi",))

conn.commit()

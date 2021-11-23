import sqlite3
from meli.request import meliClient
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

print(len(meliResponse))
       
for meliItem in meliResponse:     
    c.execute("""INSERT OR REPLACE INTO items VALUES(?, ?, ?, ?, ?, ?, ?, ?)""", (meliItem["id"], meliItem["name"], meliItem["price"], meliItem["currency"], meliItem["link"], meliItem["photo"], meliItem["domain"], "meli",))            

conn.commit()
import requests
import sys
import json

barrio = sys.argv

r = requests.get(
    "https://api.mercadolibre.com/sites/MLU/search?category=MLU6393&q={}".format(barrio))
apartamentos = []
for apto in json.loads(r.text)['results']:
    apartamento = {
        "id": apto["id"],
        "nombre": apto['title'],
        "precio": apto['price'],
        "moneda": apto['currency_id'],
        "dirección": apto['location']['address_line'],
        "foto": apto['thumbnail'],
        "area_total": "",
        "tipo_de_inmueble": "",
        "baños": "",
        "area_cubierta": "",
        "dormitorios": "",
        "estado_apto": ""
    }
    for info in apto['attributes']:
        valor = info['value_name']
        if apto['id'] == 'ITEM_CONDITION':
            apartamento['estado_apto'] = valor
        elif apto['id'] == 'BEDROOMS':
            apartamento['dormitorios'] = valor
        elif apto['id'] == 'COVERED_AREA':
            apartamento['area_cubierta'] = valor
        elif apto['id'] == 'FULL_BATHROOMS':
            apartamento['baños'] = valor
        elif apto['id'] == 'PROPERTY_TYPE':
            apartamento['tipo_de_inmueble'] = valor
        elif apto['id'] == 'TOTAL_AREA':
            apartamento['area_total'] = valor
    apartamentos.append(apartamento)

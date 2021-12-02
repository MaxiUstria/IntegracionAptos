from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def loiClient(brand):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://loi.com.uy/index.php?ctrl=buscar#q={}'.format(brand))
    timeout = 3
    try:
        element_present = EC.presence_of_element_located((By.ID, 'main'))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Timed out waiting for page to load")
    finally:
        print("Page loaded")
        items = driver.find_elements(
            By.XPATH, '//div[@class="ais-hits--item"]')
        objetos = []
        category_switcher = {
            "celulares": "celulares y tablets",
            "tablets": "celulares y tablets",
            "smartwatches": "Smartwatches y Bandas",
            "power-banks": "Accesorios",
            "fundas-y-covers": "Accesorios",
            "varios": "Accesorios",
            "cables-y-cargadores": "Accesorios",
            "soportes-para-celulares": "Accesorios",
            "monitores-planos": "Monitores",
            "monitores-curvos": "Monitores",
            "heladeras": "Electrodomésticos",
            "auriculares-cableados": "Perifericos",
            "parlantes-portatiles": "Perifericos",
            "barras-de-sonido": "Perifericos",
            "parlantes-potenciados": "Perifericos",
            "televisores-hd": "Televisores",
            "televisores-fullhd": "Televisores",
            "televisores-4k": "Televisores",
            "tv-box": "Televisores",
            "clasicas": "Notebooks",
            "gamers": "Notebooks",
            "macbooks": "Notebooks",
        }
        for item in items:
            objeto = {
                'objeto': item.find_element(By.XPATH, './/div[@class="informacion-resultado-de-busqueda"]').find_element(By.XPATH, './/h2').text,
                'descripcion': item.find_element(By.XPATH, './/div[@class="informacion-resultado-de-busqueda"]').find_element(By.XPATH, './/p[@class="resultado-info-descripcion"]').text,
                'precio': item.find_element(By.XPATH, './/div[@class="resultado-info-precio"]').text.split()[1],
                'moneda': item.find_element(By.XPATH, './/div[@class="resultado-info-precio"]').text.split()[0],
                'categoria': category_switcher.get(item.find_element(By.XPATH, './/div[@class="foto-resultado-de-busqueda"]/a').get_attribute('href').split('/')[-2], "Otros"),
                'nombreCorto': item.find_element(By.XPATH, './/div[@class="foto-resultado-de-busqueda"]/a').get_attribute('href').split('/')[-1].replace("-", " "),
                'foto': item.find_element(By.XPATH, './/div[@class="foto-resultado-de-busqueda"]/a/img').get_attribute('src'),
            }
            objetos.append(objeto)
        return objetos

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://loi.com.uy/index.php?ctrl=buscar#q=samsung')
timeout = 3
try:
    element_present = EC.presence_of_element_located((By.ID, 'main'))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print("Timed out waiting for page to load")
finally:
    print("Page loaded")
    items = driver.find_element(By.XPATH,
                                '//main[@class="contenedor-resultados-busqueda"]').find_elements(By.XPATH,
                                                                                                 '//div[@class="hit resultado-de-busqueda"]')
    objetos = []
    for item in items:
        objeto = {
            'objeto': item.find_element(By.XPATH, '//div[@class="informacion-resultado-de-busqueda"]').find_element(By.XPATH, '//h2').text,
            'descripcion': item.find_element(By.XPATH, '//div[@class="informacion-resultado-de-busqueda"]').find_element(By.XPATH, '//p[@class="resultado-info-descripcion"]').text,
            'precio': item.find_element(By.XPATH, '//div[@class="resultado-info-precio"]').text,
        }
        objetos.append(objeto)
    print(objetos)

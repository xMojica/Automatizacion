from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

service = Service("driver/chromedriver.exe")
ciudad = "Medellin"
almacen = "Carulla Laureles"
busqueda = "Python con selenium"

driver = webdriver.Chrome(service=service)
driver.maximize_window()
time.sleep(2)

# abro la pagina
driver.get("https://www.carulla.com/")
time.sleep(2)

# abro el menu hamburguesa
menuHamburguesa = driver.find_element(
    By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div/div/div[1]/div/div/div/button')
menuHamburguesa.click()
time.sleep(3)

# selecciono la categoria vida sana
vidaSana = driver.find_element(
    By.XPATH, '//*[@id="undefined-nivel2-Vida sana"]'
)
time.sleep(1)

# le hago hover a vida sana
hover = ActionChains(driver).move_to_element(vidaSana)
hover.perform()
time.sleep(2)

# abro la ruta de alimentos libre de gluten
driver.get("https://www.carulla.com/vida-sana/alimentos-libres-de-gluten")
time.sleep(8)

# selecciono el input y escribo Medellin
entradaCiudad = driver.find_element(
    By.XPATH, '/html/body/div[10]/div[1]/div/div/div[2]/div[4]/div[1]/div[2]/div/div/div/div[1]/div/div/input'
)
entradaCiudad.send_keys(ciudad)
time.sleep(1)
entradaCiudad.send_keys(Keys.ENTER)
time.sleep(4)

# selecciono el input de almacenes
entradaAlmacen = driver.find_element(
    By.XPATH, '/html/body/div[10]/div[1]/div/div/div[2]/div[4]/div[3]/div[2]/div/div/div/div[1]/div/div/input'
)
entradaAlmacen.click()
entradaAlmacen.send_keys(almacen)
time.sleep(1)
entradaAlmacen.send_keys(Keys.ENTER)
time.sleep(4)

# clickeo confirmar
confirmar = driver.find_element(
    By.XPATH, '/html/body/div[10]/div[1]/div/div/div[2]/div[6]/button'
)
confirmar.click()
time.sleep(10)

# filtrar
driver.get("https://www.carulla.com/cereales-avena-y-granolas/9834/cont-librendegluten-9834?fuzzy=0&initialMap=productClusterIds&initialQuery=9834&map=category-2,productClusterIds,productclusternames&operator=and")
time.sleep(2)

nombrePrimero = driver.find_element(
    By.XPATH, '/html/body/div[2]/div/div[1]/div/div[3]/div/div[11]/section/div[2]/div/div[3]/div/div[2]/div/div/div[6]/div/div/div/div[1]/section/a/article/div[3]/div[2]/div/div/div/div[2]/div/span'
)
precioPrimero = driver.find_element(
    By.XPATH, '/html/body/div[2]/div/div[1]/div/div[3]/div/div[11]/section/div[2]/div/div[3]/div/div[2]/div/div/div[6]/div/div/div/div[1]/section/a/article/div[3]/div[2]/div/div/div/div[4]/div[3]/div/span'
)

nombreSegundo = driver.find_element(
    By.XPATH, '/html/body/div[2]/div/div[1]/div/div[3]/div/div[11]/section/div[2]/div/div[3]/div/div[2]/div/div/div[6]/div/div/div/div[2]/section/a/article/div[3]/div[2]/div/div/div/div[2]/div/span'
)
precioSegundo = driver.find_element(
    By.XPATH, '/html/body/div[2]/div/div[1]/div/div[3]/div/div[11]/section/div[2]/div/div[3]/div/div[2]/div/div/div[6]/div/div/div/div[2]/section/a/article/div[3]/div[2]/div/div/div/div[4]/div[3]/div/span'
)

nombreTercero = driver.find_element(
    By.XPATH, '/html/body/div[2]/div/div[1]/div/div[3]/div/div[11]/section/div[2]/div/div[3]/div/div[2]/div/div/div[6]/div/div/div/div[3]/section/a/article/div[3]/div[2]/div/div/div/div[3]/div/div/div/h3/span'
)
precioTercero = driver.find_element(
    By.XPATH, '/html/body/div[2]/div/div[1]/div/div[3]/div/div[11]/section/div[2]/div/div[3]/div/div[2]/div/div/div[6]/div/div/div/div[3]/section/a/article/div[3]/div[2]/div/div/div/div[4]/div[3]/div/span'
)

nombreCuarto = driver.find_element(
    By.XPATH, '/html/body/div[2]/div/div[1]/div/div[3]/div/div[11]/section/div[2]/div/div[3]/div/div[2]/div/div/div[6]/div/div/div/div[4]/section/a/article/div[3]/div[2]/div/div/div/div[3]/div/div/div/h3/span'
)
precioCuarto = driver.find_element(
    By.XPATH, '/html/body/div[2]/div/div[1]/div/div[3]/div/div[11]/section/div[2]/div/div[3]/div/div[2]/div/div/div[6]/div/div/div/div[4]/section/a/article/div[3]/div[2]/div/div/div/div[4]/div[3]/div/span'
)

print(f"El nombre del primer producto es:"+nombrePrimero.text)
print(f"El precio del primer producto es:"+precioPrimero.text)

print(f"El nombre del segundo producto es:"+nombreSegundo.text)
print(f"El precio del segundo producto es:"+precioSegundo.text)

print(f"El nombre del tercer producto es:"+nombreTercero.text)
print(f"El precio del tercer producto es:"+precioTercero.text)

print(f"El nombre del cuarto producto es:"+nombreCuarto.text)
print(f"El precio del cuarto producto es:"+precioCuarto.text)

time.sleep(2)

# entrar en alguno
elemento = driver.find_element(
    By.XPATH, '/html/body/div[2]/div/div[1]/div/div[3]/div/div[11]/section/div[2]/div/div[3]/div/div[2]/div/div/div[6]/div/div/div/div[2]/section/a/article/div[3]'
)
elemento.click()
time.sleep(5)

# hacer scroll down
scroll = driver.find_element(
    By.TAG_NAME, 'html'
)
scroll.send_keys(Keys.END)
time.sleep(5)

# entrar a yt
youtube = driver.find_element(
    By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div/div[6]/div/div/div[2]/section/div/div[3]/div/div[2]/div/div[1]/div[2]/a[4]'
)
youtube.click()
time.sleep(4)

driver.switch_to.window(driver.window_handles[-1])

# Anexo funcionalidad de buscar un video en yt y reproducirlo
buscador = driver.find_element(
    By.XPATH, '/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input'
)
time.sleep(1)
buscador.click()
time.sleep(1)
buscador.send_keys(busqueda)
buscador.send_keys(Keys.ENTER)
time.sleep(5)

driver.get("https://www.youtube.com/watch?v=0AvX54Rp4sc")
driver.switch_to.window(driver.window_handles[-1])
time.sleep(15)

driver.quit()

#Jose Luis Torres Cardoza
#Salon 952

#Empezamos a describir
#Importamos selenium y webdriver
#Selenium es para la extraccion de datos
#Webdriver es para navegar en internet
import time #Al hacer bots es necesario agregar pausas

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

#Creamos una funcion para entrar a la pagina y navegar entre ella
def Imagenes(busqueda, paginas):
    s = Service(ChromeDriverManager().install())
    opc = Options()
#Aqui es para ajustar el tamaño de la venta que se va abrir
    opc.add_argument("--window-size-1020,1200")
    navegador = webdriver.Chrome(service=s, options=opc)
#Este es el link de la pagina
    navegador.get("https://www.ccmusic.com/")
    time.sleep(10)
    #Este es para encontrar la barra de busqueda y usarla para el producto que queramos
    txtInput = navegador.find_element(By.ID, value="q")
    txtInput.send_keys(busqueda)
    txtInput.submit()

    data = {"titulo":[], "precio":[]}
    #Este for es para navegar en la paginas de la pagina web
    for i in range(paginas):
        time.sleep(3)
        #Tomamos captura de pantalla de prueba
        navegador.save_screenshot(f"imagenesAlbum2/{busqueda}_{i}.png")
        soup = BeautifulSoup(navegador.page_source, "html5lib")
        #Aqui es para buscar todos los cuadros que tienen
        #nombre y precio de una sola pagina
        productos = soup.find_all("div",
                      attrs={"class":"aec-grid-divspan"})

        #Este for es para buscar todos los productos que se van encontrar de nombre y precio
        for i in productos:
            titulo =i.find("a", attrs ={"class": "aec-listlink"})
            precio = i.find("div", attrs ={"class":"aec-custprice"})
            #Aqui estamos llevando la informacion texto
            data["titulo"].append(titulo.text)
            #print(titulo.text)
            if precio:
                data["precio"].append(precio.text)#print(precio.text)
            else:
                data["precio"].append(None)

        btonsiguiente = navegador.find_element(By.CLASS_NAME, "aec-next")
        btonsiguiente.click()

    time.sleep(5)
    navegador.quit()
    #Creamos un dataframe con toda la informacion que hemos recopilado
    df = pd.DataFrame(data)
    df.to_csv("datasets/productosCCMusic.csv")

#Aqui es para buscar la informacion de la barra busqueda y cuantas paginas va a buscar
if __name__ == "__main__":
    busqueda = "Ariana Grande"
    paginas = 3
    Imagenes(busqueda, paginas)
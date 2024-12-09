import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import plotly.express as px
from dash import Dash, dcc, html, callback, Input, Output
import mysql.connector

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
def datacollect2(busqueda, paginas):
    s = Service(ChromeDriverManager().install())
    opc = Options()
    # Aqui es para ajustar el tamaño de la venta que se va abrir
    opc.add_argument("--window-size-1020,1200")
    navegador = webdriver.Chrome(service=s, options=opc)
    # Este es el link de la pagina
    navegador.get("https://www.ccmusic.com/")
    time.sleep(10)
    # Este es para encontrar la barra de busqueda y usarla para el producto que queramos
    txtInput = navegador.find_element(By.ID, value="q")
    txtInput.send_keys(busqueda)
    txtInput.submit()

    data = {"titulo": [], "precio": []}
    # Este for es para navegar en la paginas de la pagina web
    for i in range(paginas):
        time.sleep(3)
        # Tomamos captura de pantalla de prueba
        navegador.save_screenshot(f"imagenesAlbum2/{busqueda}_{i}.png")
        soup = BeautifulSoup(navegador.page_source, "html5lib")
        # Aqui es para buscar todos los cuadros que tienen
        # nombre y precio de una sola pagina
        productos = soup.find_all("div",
                                  attrs={"class": "aec-grid-divspan"})

        # Este for es para buscar todos los productos que se van encontrar de nombre y precio
        for i in productos:
            titulo = i.find("a", attrs={"class": "aec-listlink"})
            precio = i.find("div", attrs={"class": "aec-custprice"})
            # Aqui estamos llevando la informacion texto
            data["titulo"].append(titulo.text)
            # print(titulo.text)
            if precio:
                data["precio"].append(precio.text)  # print(precio.text)
            else:
                data["precio"].append(None)

        btonsiguiente = navegador.find_element(By.CLASS_NAME, "aec-next")
        btonsiguiente.click()

    time.sleep(5)
    navegador.quit()
    # Creamos un dataframe con toda la informacion que hemos recopilado
    df = pd.DataFrame(data)
    df.to_csv("datasets/productosCCMusic2.csv")
def datacollect3(busqueda, paginas):
    s = Service(ChromeDriverManager().install())
    opc = Options()
    # Aqui es para ajustar el tamaño de la venta que se va abrir
    opc.add_argument("--window-size-1020,1200")
    navegador = webdriver.Chrome(service=s, options=opc)
    # Este es el link de la pagina
    navegador.get("https://www.ccmusic.com/")
    time.sleep(10)
    # Este es para encontrar la barra de busqueda y usarla para el producto que queramos
    txtInput = navegador.find_element(By.ID, value="q")
    txtInput.send_keys(busqueda)
    txtInput.submit()

    data = {"titulo": [], "precio": []}
    # Este for es para navegar en la paginas de la pagina web
    for i in range(paginas):
        time.sleep(3)
        # Tomamos captura de pantalla de prueba
        navegador.save_screenshot(f"imagenesAlbum2/{busqueda}_{i}.png")
        soup = BeautifulSoup(navegador.page_source, "html5lib")
        # Aqui es para buscar todos los cuadros que tienen
        # nombre y precio de una sola pagina
        productos = soup.find_all("div",
                                  attrs={"class": "aec-grid-divspan"})

        # Este for es para buscar todos los productos que se van encontrar de nombre y precio
        for i in productos:
            titulo = i.find("a", attrs={"class": "aec-listlink"})
            precio = i.find("div", attrs={"class": "aec-custprice"})
            # Aqui estamos llevando la informacion texto
            data["titulo"].append(titulo.text)
            # print(titulo.text)
            if precio:
                data["precio"].append(precio.text)  # print(precio.text)
            else:
                data["precio"].append(None)

        btonsiguiente = navegador.find_element(By.CLASS_NAME, "aec-next")
        btonsiguiente.click()

    time.sleep(5)
    navegador.quit()
    # Creamos un dataframe con toda la informacion que hemos recopilado
    df = pd.DataFrame(data)
    df.to_csv("datasets/productosCCMusic2.csv")

def promedio():
    # Direccion de los datasets
    csv_files = [
        'datasets/ProductosCCMusic.csv',
        'datasets/ProductosCCMusic2.csv',
        'datasets/ProductosCCMusic3.csv'
    ]

    # Hacemos un diccionario para poder
    diccionario = {
        'datasets/ProductosCCMusic.csv': 'Rock Music',
        'datasets/ProductosCCMusic2.csv': 'Pop Music',
        'datasets/ProductosCCMusic3.csv': 'Country Music'
    }

    # Hacemos una lista vacia para los promedios
    averages = []

    # Hacemos un for para poder pasar cada dataset y sacar el promedio de cada uno
    for file in csv_files:
        try:
            df = pd.read_csv(file)  # cargamos el dataset
            if 'precio' in df.columns:

                df['precio'] = df['precio'].replace({'Price: \$': '', ',': '', r'\s+': ''},
                                                    regex=True)  # Quitamos precio y simbolos para que se limpie
                df['precio'] = pd.to_numeric(df['precio'], errors='coerce')  # Y lo convertimos a numero

                # Dropeamos valores NaN
                df = df.dropna(subset=['precio'])

                # Calculamos los promedios
                if not df.empty:
                    average_price = df['precio'].mean()
                    average_price = round(average_price, 2)

                    # Aqui usamos el diccionaio para que se use el nombre
                    genre = diccionario.get(file, file)
                    averages.append({'File': genre, 'Average Price': average_price})
        except Exception as e:
            print(f"Error processing {file}: {e}")

    # Creamos un dataframe con los promedios
    averages_df = pd.DataFrame(averages)
    averages_df.to_csv('datasets/average_prices.csv', index=False)

    print("Averages saved to 'datasets/average_prices.csv'")


def mysql():
    # Conectar a MySQL (sin especificar una base de datos inicialmente)
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345678"
    )
    cursor = conn.cursor()

    # Crear la base de datos si no existe
    cursor.execute("CREATE DATABASE IF NOT EXISTS ccmusic")
    cursor.execute("USE ccmusic")  # Usar la base de datos creada o existente

    # Cargar los tres datasets
    data1 = pd.read_csv('datasets/productosCCMusic.csv')
    data2 = pd.read_csv('datasets/productosCCMusic2.csv')
    data3 = pd.read_csv('datasets/productosCCMusic3.csv')

    # Crear las tablas si no existen
    def create_table(table_name, columns):
        columns_definition = ", ".join([f"`{col}` TEXT" for col in columns])
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                id INT AUTO_INCREMENT PRIMARY KEY,
                {columns_definition}
            )
        """)

    create_table('productosCCMusic', data1.columns)
    create_table('productosCCMusic2', data2.columns)
    create_table('productosCCMusic3', data3.columns)

    # Función para insertar datos en una tabla
    def insert_data_into_table(table_name, data):
        columns = ", ".join(data.columns)
        values = ", ".join(["%s"] * len(data.columns))
        insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"

        # Insertar cada fila del DataFrame en la tabla
        for row in data.itertuples(index=False, name=None):
            try:
                cursor.execute(insert_query, row)
            except mysql.connector.Error as err:
                print(f"Error al insertar los datos: {err}")

    # Insertar los datos de cada dataset en su respectiva tabla
    insert_data_into_table('productosCCMusic', data1)
    insert_data_into_table('productosCCMusic2', data2)
    insert_data_into_table('productosCCMusic3', data3)

    # Confirmar las inserciones en la base de datos
    conn.commit()

    # Cerrar la conexión a la base de datos
    conn.close()

    print("Datos insertados correctamente en las tablas.")

# Función para cargar los datos al dashboard
def load_data():
    data = pd.read_csv("datasets/average_prices.csv")
    genre_map = {
        "productosCCMusic.csv": "Rock Music",
        "productosCCMusic2.csv": "Pop Music",
        "productosCCMusic3.csv": "Country Music"
    }
    data['File'] = data['File'].map(genre_map).fillna(data['File'])
    return data


# Función para obtener el promedio del mercado en linea
def get_market_average(genre):

    market_averages = {
        "Rock Music": 18.00,  # Promedio del mercado para Rock
        "Pop Music": 22.00,  # Promedio del mercado para Pop
        "Country Music": 16  # Promedio del mercado para Country
    }
    return market_averages.get(genre, 0)


# Define el dashboard con varias opciones
def dashboard_basico():
    data = load_data()  # Cargar los datos

    # Crear el gráfico de barras para mostrar los precios promedio por género
    avg_by_genre = data.groupby('File')['Average Price'].mean().reset_index()

    blanco = {"color": "white", "fontFamily": "Poppins, sans-serif"}

    body = html.Div(
        [
            html.Div(
                [
                    html.H3("Selección de Gráficas", style={"color": "white", "textAlign": "center", "fontSize": "24px",
                                                            "fontFamily": "Poppins, sans-serif",
                                                            "paddingBottom": "20px"}),
                    dcc.RadioItems(
                        id="chart_type",
                        options=[
                            {"label": "Gráfico de Barras", "value": "bar"},
                            {"label": "Gráfico de Pie", "value": "pie"},
                            {"label": "Comparación con Promedio de Mercado", "value": "comparison"}
                        ],
                        value="bar",
                        labelStyle={"display": "block", "color": "white", "textAlign": "left", "fontSize": "18px",
                                    "padding": "10px", "fontFamily": "Poppins, sans-serif"},
                        style={"backgroundColor": "#333", "border": "none", "padding": "15px", "borderRadius": "10px"}
                    ),
                ],
                style={
                    "position": "fixed",
                    "top": 0,
                    "left": 0,
                    "width": "240px",
                    "height": "100%",
                    "background-color": "#2e2e2e",
                    "padding": "30px",
                    "color": "white",
                    "box-shadow": "2px 0px 10px rgba(0, 0, 0, 0.5)",
                    "border-radius": "0 20px 20px 0"
                }
            ),

            html.Div(
                [
                    html.H2("Comparación de Precios Promedio por Género",
                            style={"color": "white", "textAlign": "center", "fontSize": "36px",
                                   "fontFamily": "Poppins, sans-serif", "paddingBottom": "15px"}),
                    html.P(
                        "Objetivo: Mostrar y comparar los precios promedio de los diferentes géneros con el promedio de mercado.",
                        style={"color": "white", "textAlign": "center", "fontSize": "18px",
                               "fontFamily": "Poppins, sans-serif", "paddingBottom": "20px"}),
                    html.Hr(style={"borderColor": "white", "borderWidth": "2px", "marginBottom": "20px"}),


                    dcc.Graph(figure={}, id="figPrice", style={"height": "70vh", "margin": "10px 0"}),
                ],
                style={"margin-left": "260px", "padding": "30px", "background-color": "#212121",
                       "font-family": "Poppins, sans-serif", "border-radius": "20px",
                       "box-shadow": "0px 10px 30px rgba(0, 0, 0, 0.5)"}
            ),
        ],
        style={"display": "flex", "font-family": "Poppins, sans-serif", "background-color": "#121212",
               "minHeight": "100vh"}
    )
    return body

@callback(
    Output(component_id="figPrice", component_property="figure"),
    Input(component_id="chart_type", component_property="value")
)
def update_graph(chart_type):
    data = load_data()

    if chart_type == "bar":
        # Crear el gráfico de barras mostrando el precio promedio por género
        avg_by_genre = data.groupby('File')['Average Price'].mean().reset_index()
        fig = px.bar(avg_by_genre, x='File', y='Average Price', title="Promedio de Precios por Género Musical",
                     template="plotly_dark")
        fig.update_layout(title_font=dict(size=30), title_x=0.5)
        fig.update_xaxes(title="Género Musical", title_font=dict(size=16), tickangle=45)
        fig.update_yaxes(title="Precio Promedio", title_font=dict(size=16))

    elif chart_type == "pie":
        # Crear el gráfico de pie mostrando la distribución de los precios por género
        fig = px.pie(data, names="File", values="Average Price", title="Distribución de Precios Promedio por Género",
                     template="plotly_dark")
        fig.update_layout(title_font=dict(size=30), title_x=0.5)

    elif chart_type == "comparison":
        # Comparación con el promedio de mercado
        genres = data['File'].unique()
        comparison_data = []

        for genre in genres:
            genre_avg = data[data['File'] == genre]['Average Price'].mean()
            market_avg = get_market_average(genre)  # Obtener el promedio del mercado
            comparison_data.append({
                'File': genre,
                'Average Price': genre_avg,
                'Market Average': market_avg
            })

        comparison_df = pd.DataFrame(comparison_data)

        # Crear el gráfico de barras con dos barras por género
        fig = px.bar(
            comparison_df,
            x='File',
            y=['Average Price', 'Market Average'],
            barmode='group',  # Mostrar las barras agrupadas
            title="Comparación de Precios Promedio por Género con Promedio de Mercado",
            template="plotly_dark",
            labels={"File": "Género Musical", "value": "Precio Promedio"}
        )
        fig.update_layout(title_font=dict(size=30), title_x=0.5)
        fig.update_xaxes(title="Género Musical", title_font=dict(size=16), tickangle=45)
        fig.update_yaxes(title="Precio Promedio", title_font=dict(size=16))

    return fig

datos_recolectados = False


# Funciones de recolección de datos (usando las funciones que ya tienes)
def Imagenes(busqueda, paginas):
    print(f"Recolectando datos para: {busqueda} en {paginas} páginas")
def datacollect2(busqueda2, paginas2):
    print(f"Recolectando datos para: {busqueda2} en {paginas2} páginas")
def datacollect3(busqueda3, paginas3):
    print(f"Recolectando datos para: {busqueda3} en {paginas3} páginas")
    print("Calculando el promedio de los precios")


# Función que ejecuta el proceso de recolección solo una vez
def recolectar_datos():
    global datos_recolectados

    if not datos_recolectados:
        busqueda = "Rock"
        paginas = 10
        Imagenes(busqueda, paginas)

        busqueda2 = "pop"
        paginas2 = 10
        datacollect2(busqueda2, paginas2)

        busqueda3 = "country"
        paginas3 = 10
        datacollect3(busqueda3, paginas3)

        promedio()

        # Marca que los datos han sido recolectados
        datos_recolectados = True
        print("Recolección de datos completada.")
if __name__ == "__main__":
    recolectar_datos()
    # Dashboard basico
    app = Dash(__name__)
    app.layout = dashboard_basico()  # Set the layout with both charts
    app.run(debug=True)
    #mysql()
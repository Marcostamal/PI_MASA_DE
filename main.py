from fastapi import FastAPI
import pandas as pd
from pydantic import BaseModel
from typing import Optional



app = FastAPI()


class duration_max(BaseModel):
    platform: Optional[str] = None
    year: Optional[int] = None
    duration_type: Optional[str] = None

app = FastAPI(title="Peliculas puntuadas en las plataformas de Netflix, Amazon, Hulu y Disney",
              description="Esta es una API para hacer consultas sobre las caracteristicas de peliculas contenidas en nuestra base de datos")

@app.get("/")
async def index():
    texto = "Esta API fue hecha por Marcos Alejandro Segundo Almanza"
    return texto

@app.get("/platform/{platform}")
async def get_count_platform(platform: str):
    """
    Definicion
    ------------
    Esta funcion devuelve la cantidad de peliculas por plataforma
        
    parametros
    -----------
    platform: str
            Nombre de la plataforma en la que se quiere 
            buscar la cantidad de peliculas
        
    returns
    -----------
    dic: dict
        Devuelve un diccionario con la cantidad de peliculas
        
    ejemplo
    -----------
    get_count_platform("amazon")
    >>> {"Cantidad": 9668}
    """
    db = pd.read_csv("https://raw.githubusercontent.com/Marcostamal/nana/main/Plataformas_score.csv") # Cargo la data

    nom_plat = {"amazon":"a",         # Creo un diccionario para definir las entradas de mis variables
                "disney":"d",
                "hulu":"h",
                "netflix":"n"}
        
    plataforma = nom_plat[platform]   # Doy el valor de la clave que paso por el diccionario en este caso el nombre de la plataforma
    contar = 0
    for linea in db["plataforma"]:    #itero la columna plataforma y cuento cada linea
        if plataforma in linea:
            contar += 1
    dic = {"Cantidad": contar}        #Devuelvo el valor del conteo
    return dic


@app.get("/get_actor/{platform}/{year}")
async def get_actor(platform: str, year: int):
    """
    Definicion
    ------------
    Esta funcion devuelve el nombre del actor y el numero de apariciones 
    filtrado por plataforma y anio.

    parametros
    -----------
    platform: str
            Nombre de la plataforma

    year: int
            Anio en el que se lanzo la pelicula


    returns
    ----------
    return: dict
            Devuelve un diccionario con dos claves
            "actor": Contiene el nombre del actor
            "apariciones": El numero de veces que aparece el actor

    ejemplo
    ----------
    get_actor("amazon", 2015):
    >>> {"actor": "mother gose club", "apariciones": 3}
    """
    db = pd.read_csv("https://raw.githubusercontent.com/Marcostamal/nana/main/Plataformas_score.csv")  # Cargo la data

    # Mascaras para los filtros por anio y por plataforma
    filtro = db["release_year"] == year
    filtro2 = db["plataforma"] == platform[0]
    
    lista_unicos = []   #listas para guardar los actores ya que la info los trae en un string
    lista_todos = []
    
    for linea in db["cast"][filtro][filtro2]:   # iteracion por cada fila
        linea_lista = linea.split(",")          # separacion de los valores
        for actor in linea_lista:               # Valores unicos de actores
            lista_todos.append(actor)
            if actor not in lista_unicos:
                lista_unicos.append(actor.strip())
            else:
                pass
    nombre_actor = ""
    apariciones = 0
    for i in lista_todos:     # cuento cada actor y guardo el que mas se repita
        if i != "sin dato":   # Descarto este valor para que no se cuente como un actor
            veces = lista_todos.count(i)
            if veces > apariciones:
                apariciones = veces
                nombre_actor = i
            
    return {"actor":nombre_actor, "apariciones":apariciones}


@app.get("/get_score_count/{platform}/{scored}/{year}")
async def get_score_count(platform:str, scored:float, year:int):
    """
    Definicion
    ------------
    Esta funcion devuelve la cantidad de peliculas que 
    tienen una resena superior al parametro pasado


    Parametros
    -----------
    platform: str
            Nombre de la plataforma

    scored: float
            Valor de la resena a comparar

    year: int
            Anio en que salio la pelicula


    returns
    ----------
    return: dict
            Devuelve un diccionario de una clave
            como valor devuelve la cantidad de peliculas
            que tienen un scored superior al parametro pasado
            clave: "cantidad"
            valor: int

    ejemplo
    ----------
    get_score_count("amazon", 2015)
    >>> {"cantidad": 378}

    """
    db = pd.read_csv("https://raw.githubusercontent.com/Marcostamal/nana/main/Plataformas_score.csv")
    year = db["release_year"] == year
    platform = db["plataforma"] == platform[0]
    score = db["score"] > scored
    a = ((year & platform) & score)
    
    cantidad = db["id"][a].shape

    return {"cantidad": cantidad[0]}


@app.post("/get_max_duration/")
def get_max_duration(duration_max: duration_max):
    """
    Definicion
    -----------
    Esta funcion devuelve la pelicula que mas duracion tiene.
    Se puede optener por filtros de plataforma, anio, y tipo de duracion.
    Si no se pasa nada como parametro devuelve la pelicula de toda la fuente de datos.

    Parametros
    -----------
    platform: Optional[str] = None

    year: Optional[int] = None

    duration_type: Optional[str] = None


    returns
    -----------
    return: str
            Nombre de la pelicula

    ejemplo
    -----------
    get_max_duration("amazon",2015,"min")
    >>> "carmen beanch waves for sleep"
    """
    db = pd.read_csv("https://raw.githubusercontent.com/Marcostamal/nana/main/Plataformas_score.csv")
    x = 0
    y = 0
    z = 0
    if duration_max.platform == "string":
        x = db["plataforma"]
    else:
        nom_plat = {"amazon":"a",
                "disney":"d",
                "hulu":"h",
                "netflix":"n"}
        x = nom_plat[duration_max.platform]

    if duration_max.year == 0:
        y = db["release_year"]
    else:
        y = duration_max.year

    if duration_max.duration_type == "string":
        z = db["duration_type"]
    else:
        z = duration_max.duration_type

    a = db["release_year"] == y                #filtro por year
    b = db["plataforma"] == x            #filtro por platform
    c = db["duration_type"] == z      # filtro por duration_type
    filtro = ((a & b) & c)
    maximo = db[filtro]["duration_int"].max()
    pelicula = db["title"][filtro][db["duration_int"] == maximo].values
    limpio = str(pelicula)
    limpio = limpio.strip('"][')
    
    
    return str(limpio)





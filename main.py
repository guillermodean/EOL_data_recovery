import json
import pandas as pd
from Classes.Connection import Connection
from Classes.Parse import Parse

Entorno = "PRODUCCION"      #PRODUCCION | DESARROLLO | TOR | LOCAL


# Obtener las variables de acceso
with open('./database.json', 'r') as file:
    config = json.load(file)

conexion = Connection( usuario = config[Entorno]['usuario']
                        , psw = config[Entorno]['psw']
                        , host = config[Entorno]['host']
                        , DDBB = config[Entorno]['DDBB'] )
df = pd.DataFrame(Parse())
df.to_csv('data_EOL.csv', sep=';')
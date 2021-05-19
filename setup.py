import pandas as pd
import json
from classes.conexion import Conexion
from classes.ParseXml import Parse


# DEFINIR EL ENTORNO PARA QUE COJA LOS VALORES QUE SE ENCUENTRAN EN EL config.json

ENTORNO = "produccion"

# Obtener las variables de acceso

with open('config.json', 'r') as file:
    config = json.load(file)

con = Conexion(server=config[ENTORNO]['server']
               , database=config[ENTORNO]['database']
               , username=config[ENTORNO]['username']
               , password=config[ENTORNO]['password'])
n = 0
path = './xml'
# inicializar variables
ResultSet_Py_List = []
df_ = pd.DataFrame(
    columns=['name', 'result', 'value', 'expectedvalue', 'status', 'lowerlimit', 'upperlimit', 'lowerwarning',
             'upperWarning', 'units', 'runtime', 'cycles', 'timestamp', 'details'])
while True:
    df_=Parse().ParseXml(path, n, df_)
    con.subirdatos(df_)

    # todo TO SQL

    # registros = os.listdir(path)
# print(len(registros))

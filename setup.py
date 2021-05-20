import pandas as pd
import json
from classes.conexion import Conexion
from classes.ParseXml import Parse
from classes.Iteration import Iteration
import time

####### DEFINIR EL ENTORNO PARA QUE COJA LOS VALORES QUE SE ENCUENTRAN EN EL config.json  #######

ENTORNO = "desarrollo" #produccion


####### Obtener las variables de acceso #######

with open('config.json', 'r') as file:
    config = json.load(file)

# con = Conexion(server=config[ENTORNO]['server']
#                , database=config[ENTORNO]['database']
#                , username=config[ENTORNO]['username']
#                , password=config[ENTORNO]['password'])

path = config[ENTORNO]['path']

####### inicializar variables  #######

n = 0
# path = './xml'
lista = ['Valladolid']
ResultSet_Py_List = []
df_ = pd.DataFrame(
    columns=['name', 'result', 'value', 'expectedvalue', 'status', 'lowerlimit', 'upperlimit', 'lowerwarning',
             'upperWarning', 'units', 'runtime', 'cycles', 'timestamp', 'details'])

####### Inicio del bucle #######

while True:
    newfiles, lista = Iteration().newfiles(path, lista)
    if newfiles == None:
        time.sleep(180)
        print('sleeping NONE')
    else:
        df_ = Parse().ParseXml(path, n, df_, newfiles)
        Conexion(server=config[ENTORNO]['server']
                 , database=config[ENTORNO]['database']
                 , username=config[ENTORNO]['username']
                 , password=config[ENTORNO]['password']).subirdatos(df_)
        time.sleep(180)
        print('sleeping uploaded')

import os
import xml.etree.cElementTree as eT
import traceback
import pandas as pd
import json
from Classes.conexion import Conexion

####### DEFINIR EL ENTORNO PARA QUE COJA LOS VALORES QUE SE ENCUENTRAN EN EL config.json  #######

ENTORNO = "produccion" #produccion


####### Obtener las variables de acceso #######

with open('config.json', 'r') as file:
    config = json.load(file)

# con = Conexion(server=config[ENTORNO]['server']
#                , database=config[ENTORNO]['database']
#                , username=config[ENTORNO]['username']
#                , password=config[ENTORNO]['password'])

path = config[ENTORNO]['path']

####### inicializar variables  #######

class Parse:
    def __init__(self):
        self.conexion = None
        print('Parser creado')
        

    def ParseXml(self, path, n, df_, newfiles):
        dftodos=df_
        for filename in newfiles:
            datarow=Conexion(server=config[ENTORNO]['server']
                 , database=config[ENTORNO]['database']
                 , username=config[ENTORNO]['username']
                 , password=config[ENTORNO]['password']).comprobarfile(filename)
            if filename!=datarow:
                print('dentro del if filename= '+filename)
                print('dentro del if datarow= '+str(datarow))
                if not filename.endswith('.xml'):
                    continue
                fullname = os.path.join(path, filename)
                doc = eT.parse(fullname)
                nodes = doc.findall('.//tests')
                test = list()
                for node in nodes:
                    for elem in node.findall("*"):
                        try:
                            if elem.tag == "test":
                                test.append(elem.attrib)
                        except AttributeError:
                            traceback.print_exc()
                    s1 = pd.Series(test)

                    for index, value in s1.items():
                        df = pd.DataFrame.from_dict(value, orient='index')
                        df = df.transpose()
                        if n == 0:
                            # df = df.append(products, ignore_index=True)
                            df_ = df.append(df_, ignore_index=True)
                            df_['Index'] = str(filename)
                        else:
                            # df = df.append(products, ignore_index=True)
                            df_ = df.append(df_, ignore_index=True)
                            df_['Index'] = df_['Index'].fillna(str(filename))
                        n += 1
                        df1file = df.append(df_)
                        df = pd.DataFrame({"data": s1})
                dftodos=dftodos.append(df1file)  
            print(filename)
            print(datarow)
        return dftodos

    def insertRows(self,df_):
        self.conexion.subirdatos(df_)

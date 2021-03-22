import xml.etree.cElementTree as eT
import os
import pandas as pd
import traceback

class Parse():
    """ Inicializar las listas que contendrán los registros de las tablas/Df  """
    n = 0
    ResultSet_Py_List = []
    path = '../xml'
    Rutaxml=None
    df_ = pd.DataFrame(
        columns=['name', 'result', 'value', 'expectedvalue', 'status', 'lowerlimit', 'upperlimit', 'lowerwarning',
                 'upperWarning', 'units', 'runtime', 'cycles', 'timestamp', 'details'])

    def __init__(self):
        print("Parsear creado")

    def parsearXML(self, path, n, df_):
        self.path = path
        self.n = n
        self.df_ = df_
        for filename in os.listdir(path):
        #TODO len listdir(path)  compare each 5 min
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
                    df_ = df.append(df_)
                return df_
                df_.to_csv('data_EOL.csv', sep=';')

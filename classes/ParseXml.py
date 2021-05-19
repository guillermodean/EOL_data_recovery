import os
import xml.etree.cElementTree as eT
import traceback
import pandas as pd


class Parse:
    def __init__(self):
        self.conexion = None
        print('Parser creado')

    def ParseXml(self, path, n, df_):
        for filename in os.listdir(path):
            # TODO len listdir(path)  compare each 5 min

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
                df = pd.DataFrame({"data": s1})
                df_.to_csv('raba.csv', sep=';')
                return df_

    def insertRows(self,df_):
        self.conexion.subirdatos(df_)

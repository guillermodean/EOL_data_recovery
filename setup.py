import xml.etree.cElementTree as eT
import os
import pandas as pd
import traceback

ResultSet_Py_List = []
path = './xml'
for filename in os.listdir(path):
    if not filename.endswith('.xml'):
        continue
    fullname = os.path.join(path, filename)
    doc = eT.parse(fullname)
    nodes = doc.findall('.//tests')
    print(nodes)
    test = list()
    for node in nodes:
        for elem in node.findall("*"):
            try:
                if elem.tag == "test":
                    test.append(elem.attrib)
            except AttributeError:
                print("fuler")
                traceback.print_exc()
        s1 = pd.Series(test)
        df_ = pd.DataFrame(
            columns=['name', 'result', 'value', 'expectedvalue', 'status', 'lowerlimit', 'upperlimit', 'lowerwarning',
                     'upperWarning', 'units', 'runtime', 'cycles', 'timestamp', 'details'])
        for index, value in s1.items():
            print(f"Index : {index}, Value : {value}")
            print(type(value))
            df = pd.DataFrame.from_dict(value, orient='index')
            df = df.transpose()
            print(df[:10])
            df_ = df.append(df_)
        df = pd.DataFrame({"data": s1})
        print(df_.info())
        df_.to_csv('raba.csv', sep=';')

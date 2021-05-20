import os
import pandas as pd


class Iteration:
    def __init__(self):
        print('iteración iniciada')
        self.diff = None

    def newfiles(self, path, lista):
        self.path = path
        newlist = os.listdir(self.path)  # vuelvo a lanzar la consulta de los archivos en el directorio
        if len(newlist) == len(lista):
            print("no hay archivos nuevos")
            diff=None
            lista=newlist
        else:
            self.diff = (set(newlist) - set(lista))
            diff = self.diff
            lista = newlist
        return diff, lista

#
# lista=['Valladolid']
# path='./xml'
# print('cuantos registros hay en mi lista inicial: '+str(len(lista)))
# newfiles, lista = Iteration().newfiles(path, lista)
# print('cuantos registros tengo que meter en el sql porque son nuevos: '+str(len(newfiles)))
# print('raba')
# print('guardo el total de registros existentes, metidos o no: '+str(len(lista)))

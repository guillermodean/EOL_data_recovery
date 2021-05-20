# EOL data recovery

Bot para subir los archivos nuevos de XML a MSSQL

## Informacion
---

Este script se va a usar para capturar los xmls generados por las máquinas de göpel.

Estará continuamente iterando y detectando los archivos nuevos para parsearlos y subirlos a una BBDD local.

## Desarrollo
---

### Lenguajes:

* python

### Desarrollada usando:

* Pandas - para el tratamiento de datos
* pyodbc - para la conexión a BBDD
* SQLAlchemy - para insertar los datos
* numpy - para tratamiento de listas
* xml.etree.cElementTree - para parsear los documentos

### BBDD:

* MSSQL - 10.73.80.4@Ruben.Windows2018 - DATOS7QB
* La configuración está guardada en el archivo `config.json`


### Test de la API:

---

### Despliegue:


* Desplegada en:  `pte desplegar`
* Servicio: se ejecutara con PM2 en cada máquina

hay que ejecutar: 
1. Instalar python
2. Instalar PM2
3. Copiar el archivo en un repo local
4. Por consola: `pm2 start setup.py --name capturaXML --interpreter py `
5. `pm2 save`
6. `pm2 ls` para ver los servicios activos


### Repositorios:

* Project `http://10.73.82.219/Bonobo.Git.Server/EOL_data_recovery.git`


## Licencia
---
ISRI
## Organización
---
### Empresa ISRINGHAUSEN: 

ISRINGHAUSEN es una empresa con más de 50 años de experiencia en la fabricación de asientos para vehículos industriales. A día de hoy es suministrador de muchas de las principales marcas de automoción internacional.

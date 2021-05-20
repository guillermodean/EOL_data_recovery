import pyodbc
import pyodbc as sql
import sqlalchemy


class Conexion:
    server = None
    database = None
    username = None
    password = None
    conn = None
    engine = None

    def __init__(self, server, database, username, password):
        # Some other example server values are
        # server = 'localhost\sqlexpress' # for a named instance
        # server = 'myserver,port' # to specify an alternate port
        try:
            con = sql.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
            engine = sqlalchemy.create_engine("mssql+pyodbc://" + username + ":" + password + "@" + server + "/"+database+"?driver=ODBC+DRIVER+17+for+SQL+Server", pool_pre_ping=True)
            print("conectado a BBDD")
            self.conn = con
            self.engine = engine

        except pyodbc.Error as err:
            print(err)

    def subirdatos(self, df):
        df.to_sql("EOL_BAU", con=self.engine, if_exists='append', index=False)
        # df.to_csv('gramenauer.csv', sep=',') se usa para comprobar la subida
        print('datos subidos')

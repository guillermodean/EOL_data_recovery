import mysql.connector
from mysql.connector import errorcode


class Connection():
    usuario = None
    psw = None
    host = None
    DDBB = None

    conn = None

    def __init__(self, usuario, psw, host, DDBB):

        self.usuario = usuario
        self.pws = psw
        self.host = host
        self.DDBB = DDBB

        try:
            cnx = cnx = mysql.connector.connect(user=self.usuario
                                                , password=self.pws
                                                , host=self.host
                                                , database=self.DDBB)

            cnx.autocommit = False

            print("conectado a BBDD")
            self.conn = cnx

        except mysql.connector.Error as err:

            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    def execQuery(self, Query_params, params):
        cursor = self.conn.cursor()
        cursor.execute(Query_params, params)

    def execQueryArray(self, Query_params, paramsArray):
        cursor = self.conn.cursor()
        cursor.executemany(Query_params, paramsArray)

    def commit(self):
        """ Para confirmar los inserts, se tiene que terminar con un commit """
        self.conn.commit()
        # print("commit")

    def execQuerySimple(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        self.conn.commit()

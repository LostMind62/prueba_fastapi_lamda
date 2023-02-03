from mysql.connector import Error, errorcode
from mysql.connector import (connection)
CREDENTIALS = {
    "username": "admin",
    "password": "RadiZeissps310",
    "database": "radi",
    "host": "radi-test.coglntv2us28.us-west-1.rds.amazonaws.com",
    "dialect": "mysql"
}
class MySQLConnection():

    def __init__(self):
        pass

    def get_cursor(self):
        return self.cursor

    def close_connection(self):
        self.cnx.close()
        self.cursor.close()

    def connect(self):
        try:
            self.cnx = connection.MySQLConnection(user=CREDENTIALS["username"],
                                                  password=CREDENTIALS["password"],
                                                  host=CREDENTIALS["host"],
                                                  database=CREDENTIALS["database"])
            self.cursor = self.cnx.cursor()
        except Error as e:
            print(e)
        return self.cursor

    def consult(self, query, params=None):
        self.connect()
        result = None
        try:
            self.cursor.execute(query, params)
            result = self.cursor.fetchall()
        except Error as e:
            print(e)
        return result


# test
# def main():
#     a = MySQLConnection()
#     result = a.consult("SELECT * FROM DogsLostReports where id = %s", (1,))
#     print(result)
#     a.close_connection()


# if __name__ == "__main__":
#     main()
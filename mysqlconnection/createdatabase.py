import mysql.connector
from mysql.connector import Error
def is_connected():
    try:
        con = mysql.connector.Connect(host = "localhost",user = "root",password = "       ")
        if con.is_connected():
            cur = con.cursor()
            cur.execute("CREATE DATABASE ONGOLE")
            print("created database successfully")
    except Error as e:
        print("An error occured",e)
    finally:
        if con.is_connected():
            con.close() and cur.close()
            print("successfully completed")
if __name__ == "__main__":
    is_connected()
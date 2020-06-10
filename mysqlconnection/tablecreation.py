import mysql.connector
from mysql.connector import Error
def is_connected():
    try:
        con = mysql.connector.Connect(host = "localhost",user = "root",password = "   ",database = "ongole")
        if con.is_connected():
            print("connected to database ongole")
            cur = con.cursor()
            cur.execute("create table ongole.persons(id int(10),name varchar(100),age int(100), gender varchar(10), phone int(255),occupation varchar(100),income int(255))))")
        print("table created successfully")
    except Error as e:
        print("An error occured",e)
    finally:
        if con.is_connected():
            con.close() and cur.close()
            print("completed ..........")
if __name__ == "__main__":
    is_connected()
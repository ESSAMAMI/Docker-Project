import mysql.connector
from mysql.connector import Error
import pandas as pd

def getConnection():
    try:
        connection = mysql.connector.connect(host='localhost',
                                 database='CRUD',
                                 user='root',
                                 password='azerty')
        if connection.is_connected():
           db_Info = connection.get_server_info()
           print("Connected to MySQL database... MySQL Server version on ",db_Info)
           cursor = connection.cursor()
           cursor.execute("select database();")
           record = cursor.fetchone()
           print ("Your connected to - ", record)
           return connection
    except Error as e :
        print ("Error while connecting to MySQL", e)



def getPerson():
    try:
        connection = getConnection()

        if connection.is_connected():

           cursor = connection.cursor()
           cursor.execute("select * from PERSON;")
           record = cursor.fetchall()
           return record
    except Error as e :
        print ("Error while connecting to MySQL", e)

def setPerson(firstname, name, age, address, win):
    try:
        connection = getConnection()

        if connection.is_connected():

           cursor = connection.cursor()
           address = address.replace("'", "")
           query = "INSERT INTO PERSON VALUES(7, '{}', '{}', {}, '{}', '{}')".format(firstname, name, age, address, win)
           print(query)
           cursor.execute(query)
           connection.commit()
    except Error as e :
        print ("Error while connecting to MySQL", e)

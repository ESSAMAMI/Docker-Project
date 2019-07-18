import mysql.connector
from mysql.connector import Error
import pandas as pd
import random


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
           list_rand = ['SORRY TRY AGIN', 'SORRY TRY AGIN', 'SORRY TRY AGIN', 'AUDI A1', 'SORRY TRY AGIN', 'SORRY TRY AGIN']
           query = "INSERT INTO PERSON (FIRST_NAME, SURNAME, AGE, ADDRESS, WIN) VALUES('{}', '{}', {}, '{}', '{}')".format(firstname, name, age, address, list_rand[random.randint(0,4)])
           print(query)
           cursor.execute(query)
           connection.commit()
    except Error as e :
        print ("Error while connecting to MySQL", e)

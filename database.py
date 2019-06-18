import mysql.connector
from mysql.connector import Error


def connect():
    """Connect to local MySQL database"""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='iota1',
            user='pi',
            passwd='GAtech321'
        )
        if connection.is_connected():
            print('Successfully connected to the local database')
    except Error as e:
        print(e)

import json
from sense_hat import SenseHat
import datetime
import mysql.connector
from mysql.connector import Error


def json_parser(file_name):
    with open(file_name, 'r') as data:
        data_store = json.load(data)
        return data_store


print(json_parser('config.json'))


def write_data():
    """Connect to local MySQL database and write new data"""
    try:
        my_database = mysql.connector.connect(
            host='localhost',
            database='iota1',
            user='pi',
            passwd='GAtech321'
        )
        if my_database.is_connected():
            sense = SenseHat()
            print('Successfully connected to the local database')
            cursor = my_database.cursor()
            sql = "INSERT INTO data_log (date, temperature, humidity) values (%s,%s,%s)"
            val = (datetime.datetime.now(), sense.get_temperature(), sense.get_humidity())
            cursor.execute(sql, val)
            my_database.commit()
    except Error as e:
        print(e)
    finally:
        my_database.close()

write_data()

# class LoggingDate:
#     def __init__(self, temperature, humidity):
#         self.temperature = temperature
#         self.humidity = humidity


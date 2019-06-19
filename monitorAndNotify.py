import json_parser
from sense_hat import SenseHat
import datetime
import time
import mysql.connector
from mysql.connector import Error
from pushbullet import PushBullet
from pushbullet.errors import PushbulletError, InvalidKeyError, PushError


class DataLogger:
    @staticmethod
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
            time.sleep(60)  # sleep for 1 minute


class Notifier:
    ok_message = "OK"
    error_message_tile = "BAD"
    notification_count = 0

    def __init__(self, error_message):
        self.error_message = error_message

    def push_notification(self):
        try:
            pb = PushBullet('o.IcOB60dNl8mrBFHVI0AJtx68ZmSTCJIO')
            push = pb.push_note(self.error_message_tile, 'Something is going on')
        except (PushbulletError, InvalidKeyError, PushError) as e:
            print(e)

    @staticmethod
    def read_and_compare_latest_data():
        pass

    def save_push_time(self):
        pass

    def check_push_time(self):
        pass



while True:
    DataLogger.write_data()

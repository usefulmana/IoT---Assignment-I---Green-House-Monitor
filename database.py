import datetime
import mysql.connector
from mysql.connector import Error


class Database():
    def __init__(self):
        self._database_name = 'iota1'
        self._host = 'localhost'
        self._user = 'pi'
        self._password = 'GAtech321'
        self._today_date = datetime.datetime.today()

    def save_data(self, date, temperature, humidity):
        try:
            my_database = mysql.connector.connect(
                host=self._host,
                database=self._database_name,
                user=self._user,
                passwd=self._password
            )
            if my_database.is_connected():
                cursor = my_database.cursor()
                sql = "INSERT INTO data_log (date, temperature, humidity) values (%s,%s,%s)"
                val = (date, temperature, humidity)
                cursor.execute(sql, val)
                my_database.commit()
        except Error as e:
            print(e)
        finally:
            my_database.close()

    def read_data(self):
        data = []
        try:
            my_database = mysql.connector.connect(
                host=self._host,
                database=self._database_name,
                user=self._user,
                passwd=self._password
            )
            if my_database.is_connected():
                cursor = my_database.cursor()
                sql = "SELECT * FROM data_log"
                data_list = cursor.execute(sql)
                for row in data_list:
                    data.append(row)
                return data
        except Error as e:
            print(e)
        finally:
            my_database.close()

    def save_daily_report(self, status):
        try:
            my_database = mysql.connector.connect(
                host=self._host,
                database=self._database_name,
                user=self._user,
                passwd=self._password
            )
            if my_database.is_connected():
                cursor = my_database.cursor()
                sql = "INSERT INTO daily_report (date, status) values (%s,%s)"
                val = (datetime.datetime.now(), status)
                cursor.execute(sql, val)
                my_database.commit()
                print('daily report')
        except Error as e:
            print(e)
        finally:
            my_database.close()

    def read_daily_report(self):
        data = []
        try:
            my_database = mysql.connector.connect(
                host=self._host,
                database=self._database_name,
                user=self._user,
                passwd=self._password
            )
            if my_database.is_connected():
                cursor = my_database.cursor()
                sql = "SELECT * FROM daily_report"
                data_list = cursor.execute(sql)
                for row in data_list:
                    data.append(row)
                return data
        except Error as e:
            print(e)
        finally:
            my_database.close()

    def check_status_existence(self):
        try:
            my_database = mysql.connector.connect(
                host=self._host,
                database=self._database_name,
                user=self._user,
                passwd=self._password
            )
            if my_database.is_connected():
                cursor = my_database.cursor()
                sql = "SELECT * FROM daily_report WHERE record_date LIKE %s LIMIT 1"
                cursor.execute(sql, self._today_date)
                result = cursor.fetchone()

                if result == None:
                    return 0
                elif result[2] == 'OK':
                    return 1
                else:
                    return 2


        except Error as e:
            print(e)
        finally:
            my_database.close()

    def update_daily_report(self, status):
        try:
            my_database = mysql.connector.connect(
                host=self._host,
                database=self._database_name,
                user=self._user,
                passwd=self._password
            )
            if my_database.is_connected():
                cursor = my_database.cursor()
                sql = "UPDATE daily_report SET status = (%s) WHERE date = (%s)"
                val = (status, self._today_date)
                cursor.execute(sql, val)
                my_database.commit()

        except Error as e:
            print(e)
        finally:
            my_database.close()
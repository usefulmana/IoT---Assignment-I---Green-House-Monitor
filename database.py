import datetime
import mysql.connector
from mysql.connector import Error
from json_parser import Parser


class Database:
    def __init__(self):
        self._database_name = 'iota1'
        self._host = 'localhost'
        self._user = 'pi'
        self._password = 'GAtech321'
        self._today_date = datetime.datetime.today().date()

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
                cursor.execute(sql)
                result = cursor.fetchall()
                for row in result:
                    data.append(row)
                return data
        except Error as e:
            print(e)
        finally:
            my_database.close()

    def save_daily_notification(self, status):
        try:
            my_database = mysql.connector.connect(
                host=self._host,
                database=self._database_name,
                user=self._user,
                passwd=self._password
            )
            if my_database.is_connected():
                cursor = my_database.cursor()
                sql = "INSERT INTO daily_notification (record_date, status) values (%s,%s)"
                val = (datetime.datetime.now(), status)
                cursor.execute(sql, val)
                my_database.commit()
        except Error as e:
            print(e)
        finally:
            my_database.close()

    def read_daily_notification(self):
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
                sql = "SELECT * FROM daily_notification"
                cursor.execute(sql)
                result = cursor.fetchall()
                return result
        except Error as e:
            print(e)
        finally:
            my_database.close()

    def check_notification_status(self):
        try:
            my_database = mysql.connector.connect(
                host=self._host,
                database=self._database_name,
                user=self._user,
                passwd=self._password
            )
            if my_database.is_connected():
                cursor = my_database.cursor()
                sql = "SELECT * FROM daily_notification WHERE record_date = %s LIMIT 1"
                cursor.execute(sql, (self._today_date,))
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

    def update_daily_notification(self, status):
        try:
            my_database = mysql.connector.connect(
                host=self._host,
                database=self._database_name,
                user=self._user,
                passwd=self._password
            )
            if my_database.is_connected():
                cursor = my_database.cursor()
                sql = "UPDATE daily_notification SET status = (%s) WHERE record_date = (%s)"
                val = (status, self._today_date)
                cursor.execute(sql, val)
                my_database.commit()

        except Error as e:
            print(e)
        finally:
            my_database.close()

    def get_all_dates_from_database(self, days_in_report):
        try:
            my_database = mysql.connector.connect(
                host=self._host,
                database=self._database_name,
                user=self._user,
                passwd=self._password
            )
            if my_database.is_connected():
                cursor = my_database.cursor()
                # Get all dates
                date_sql = "select distinct date(date) from data_log order by date(date) desc limit {}".format(
                    days_in_report)
                cursor.execute(date_sql)
                results = cursor.fetchall()
                return results[::-1]
        except Error as e:
            print(e)
        finally:
            my_database.close()

    def get_daily_average_temp(self, date_list):
        try:
            my_database = mysql.connector.connect(
                host=self._host,
                database=self._database_name,
                user=self._user,
                passwd=self._password
            )
            if my_database.is_connected():
                avg_temp = []
                cursor = my_database.cursor()
                # Get all dates
                for d in date_list:
                    date_sql = "select round(avg(temperature),2) from data_log where date between '{} 00:00:00' and '{} 23:59:59'".format(
                        d[0], d[0])
                    cursor.execute(date_sql)
                    avg_temp.append(cursor.fetchall())
                return avg_temp
        except Error as e:
            print(e)
        finally:
            my_database.close()

    def get_daily_average_humid(self, date_list):
        try:
            my_database = mysql.connector.connect(
                host=self._host,
                database=self._database_name,
                user=self._user,
                passwd=self._password
            )
            if my_database.is_connected():
                avg_humid = []
                cursor = my_database.cursor()
                # Get all dates
                for d in date_list:
                    date_sql = "select round(avg(humidity),2) from data_log where date between '{} 00:00:00' and '{} 23:59:59'".format(
                        d[0], d[0])
                    cursor.execute(date_sql)
                    avg_humid.append(cursor.fetchall())
                return avg_humid
        except Error as e:
            print(e)
        finally:
            my_database.close()

    def get_daily_min_temperature(self, date_list):
        try:
            my_database = mysql.connector.connect(
                host=self._host,
                database=self._database_name,
                user=self._user,
                passwd=self._password
            )
            if my_database.is_connected():
                min_temp = []
                cursor = my_database.cursor()
                # Get all dates
                for d in date_list:
                    date_sql = "select min(temperature) from data_log where date between '{} 00:00:00' and '{} 23:59:59'".format(
                        d[0], d[0])
                    cursor.execute(date_sql)
                    min_temp.append(cursor.fetchall())
                return min_temp
        except Error as e:
            print(e)
        finally:
            my_database.close()

    def get_daily_max_temperature(self, date_list):
        try:
            my_database = mysql.connector.connect(
                host=self._host,
                database=self._database_name,
                user=self._user,
                passwd=self._password
            )
            if my_database.is_connected():
                max_temp = []
                cursor = my_database.cursor()
                # Get all dates
                for d in date_list:
                    date_sql = "select max(temperature) from data_log where date between '{} 00:00:00' and '{} 23:59:59'".format(
                        d[0], d[0])
                    cursor.execute(date_sql)
                    max_temp.append(cursor.fetchall())
                return max_temp
        except Error as e:
            print(e)
        finally:
            my_database.close()

    def get_daily_min_humidity(self, date_list):
        try:
            my_database = mysql.connector.connect(
                host=self._host,
                database=self._database_name,
                user=self._user,
                passwd=self._password
            )
            if my_database.is_connected():
                min_humid = []
                cursor = my_database.cursor()
                # Get all dates
                for d in date_list:
                    date_sql = "select min(humidity) from data_log where date between '{} 00:00:00' and '{} 23:59:59'".format(
                        d[0], d[0])
                    cursor.execute(date_sql)
                    min_humid.append(cursor.fetchall())
                return min_humid
        except Error as e:
            print(e)
        finally:
            my_database.close()

    def get_daily_max_humidity(self, date_list):
        try:
            my_database = mysql.connector.connect(
                host=self._host,
                database=self._database_name,
                user=self._user,
                passwd=self._password
            )
            if my_database.is_connected():
                max_humidity = []
                cursor = my_database.cursor()
                # Get all dates
                for d in date_list:
                    date_sql = "select max(humidity) from data_log where date between '{} 00:00:00' and '{} 23:59:59'".format(
                        d[0], d[0])
                    cursor.execute(date_sql)
                    max_humidity.append(cursor.fetchall())
                return max_humidity
        except Error as e:
            print(e)
        finally:
            my_database.close()

    @staticmethod
    def get_detailed_daily_report():
        db = Database()
        parser = Parser()
        date_tuple = db.get_all_dates_from_database(parser.number_of_days_in_report)
        avg_temp = db.get_daily_average_temp(date_tuple)
        avg_humid = db.get_daily_average_humid(date_tuple)
        min_temp = db.get_daily_min_temperature(date_tuple)
        max_temp = db.get_daily_max_temperature(date_tuple)
        min_humid = db.get_daily_min_humidity(date_tuple)
        max_humid = db.get_daily_max_humidity(date_tuple)

        date_list = []
        for i in date_tuple:
            date_list.append(i[0])

        avg_temp_list = []
        for i in avg_temp:
            for j in i[0]:
                avg_temp_list.append(j)

        avg_humid_list = []
        for i in avg_humid:
            for j in i[0]:
                avg_humid_list.append(j)

        min_temp_list = []
        for i in min_temp:
            for j in i[0]:
                min_temp_list.append(j)

        max_temp_list = []
        for i in max_temp:
            for j in i[0]:
                max_temp_list.append(j)

        min_humid_list = []
        for i in min_humid:
            for j in i[0]:
                min_humid_list.append(j)

        max_humid_list = []
        for i in max_humid:
            for j in i[0]:
                max_humid_list.append(j)

        ultimate_list = date_list + avg_temp_list + avg_humid_list + min_temp_list + max_temp_list + min_humid_list + max_humid_list
        pen_list = []
        for k in range(len(date_tuple)):
            for i in range(k, len(ultimate_list), len(date_tuple)):
                try_list = []
                try_list.append(ultimate_list[i])
                pen_list.append(try_list)
        print(ultimate_list)
        print(pen_list)
        return pen_list

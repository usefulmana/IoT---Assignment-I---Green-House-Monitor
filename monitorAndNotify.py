import time
import datetime
import os
from sense_hat import SenseHat
from json_parser import Parser
from database import Database
from notification import Notification
from data_checker import Checker


class GreenHouseMonitor:
    """ Main class responsible for executing the program"""
    def __init__(self):
        self._sense = SenseHat()
        self._notification = Notification()
        self._checker = Checker()
        self._database = Database()

    def get_cpu_temp(self):

    def main(self):
        # status_number = self.database.check_status_existence()
        # if status_number == 0:
        #     self.database.save_daily_report('OK')

        record_time = datetime.datetime.now()
        temperature = round(self._sense.get_temperature(), 1)
        humidity = round(self._sense.get_humidity(), 1)
        self._database.save_data(record_time, temperature, humidity)

        # status = self.checker.check_data(temperature, humidity)
        # print(status)
        # print(status_number)
        # if status != 'OK' and status_number == 1:
        #     self.database.update_daily_report(status)
        #     self.notification.push_notification(datetime.datetime.now(), status)


monitor = GreenHouseMonitor()
config = Parser()

while True:
    monitor.main()
    time.sleep(config.refresh_rate)
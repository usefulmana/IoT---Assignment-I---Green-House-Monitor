import time
import datetime
from sense_hat import SenseHat
from json_parser import Parser
from database import Database
from notification import Notification
from data_checker import Checker


class GreenHouseMonitor:
    """ Main class responsible for executing the program"""
    def __init__(self):
        self.sense = SenseHat()
        self.notification = Notification()
        self.checker = Checker()
        self.database = Database()

    def main(self):
        status_number = self.database.check_status_existence()
        if status_number == 0:
            self.database.save_daily_report('OK')

        temperature = round(self.sense.get_temperature(), 1)
        humidity = round(self.sense.get_humidity(), 1)
        self.database.save_data(temperature, humidity)

        status = self.checker.check_data(temperature,humidity)
        print(status)
        print(status_number)
        if status != 'OK' and status_number == 1:
            self.database.update_daily_report(status)
            self.notification.push_notification(datetime.datetime.now(), status)


monitor = GreenHouseMonitor()
config = Parser()

while True:
    monitor.main()
    time.sleep(config.REFRESH_RATE)
import time
import datetime
import os
from sense_hat import SenseHat
from json_parser import Parser
from database import Database
from notification import Notification
from data_checker import Checker
from led import LED


class GreenHouseMonitor:
    """ Main class responsible for executing the program"""
    def __init__(self):
        self._sense = SenseHat()
        self._notification = Notification()
        self._checker = Checker()
        self._database = Database()
        self._led = LED()

    @staticmethod
    def get_cpu_temp():
        """Getting Pi's CPU Temp"""
        res = os.popen("vcgencmd measure_temp").readline()
        t = float(res.replace("temp=", "").replace("'C\n", ""))
        return t

    @staticmethod
    def calibrate_temp(temperature):
        return round(temperature - (GreenHouseMonitor.get_cpu_temp() - temperature)/1.5)

    def main(self):
        status_number = self._database.check_notification_status()
        if status_number == 0:
            self._database.save_daily_notification('OK')

        record_time = datetime.datetime.now()
        temperature = round(self._sense.get_temperature(), 1)
        humidity = round(self._sense.get_humidity(), 1)
        self._database.save_data(record_time, GreenHouseMonitor.calibrate_temp(temperature), humidity)

        # Checking temperature and humidity of they are within range
        temp_status = self._checker.check_temperature(GreenHouseMonitor.calibrate_temp(temperature))
        humidity_status = self._checker.check_humidity(humidity)
        self._sense.clear()
        """If the return value does not contain OK meaning temperature or humidity or both are out of range, and if
        the status value in database is 'OK', a notification will be sent"""
        if temp_status.find('OK') == -1 and self._database.check_notification_status() == 1:
            self._database.update_daily_notification(temp_status)
            self._notification.push_notification(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), temp_status)
        if humidity_status.find('OK') == -1 and self._database.check_notification_status() == 1:
            self._database.update_daily_notification(humidity_status)
            self._notification.push_notification(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), humidity_status)

        # If temperature or humidity is out of range, red led will light up. If not, green led will light up.
        # if temp_status.find('OK') == -1 or humidity_status.find('OK') == -1:
        #     self._led.red_light_on()
        # else:
        #     self._led.green_light_on()


monitor = GreenHouseMonitor()
config = Parser()

while True:
    monitor.main()
    time.sleep(config.refresh_rate)
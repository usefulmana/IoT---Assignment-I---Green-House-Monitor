import datetime
from sense_hat import SenseHat
from database import Database
from notification import Notification
from data_checker import Checker
from temperature_calibrator import Calibrator


class GreenHouseMonitor:
    """ Main class responsible for executing the program"""
    def __init__(self):
        self._sense = SenseHat()
        self._notification = Notification()
        self._checker = Checker()
        self._database = Database()

    def main(self):
        status_number = self._database.check_notification_status()
        self._sense.show_message('ok')
        if status_number == 0:
            self._database.save_daily_notification('OK')

        record_time = datetime.datetime.now()
        temperature = round(self._sense.get_temperature(), 1)
        calibrated_temp = Calibrator.calibrate_temperature(temperature)
        humidity = round(self._sense.get_humidity(), 1)
        self._database.save_data(record_time, calibrated_temp, humidity)

        # Checking temperature and humidity of they are within range
        temp_status = self._checker.check_temperature(calibrated_temp)
        humidity_status = self._checker.check_humidity(humidity)
        """If the return value does not contain OK meaning temperature or humidity or both are out of range, and if
        the status value in database is 'OK', a notification will be sent"""
        if temp_status.find('OK') == -1 and self._database.check_notification_status() == 1:
            self._database.update_daily_notification(temp_status)
            self._notification.push_notification(
                "{}. Current Temperature: {} C".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                                       calibrated_temp), temp_status)
        else:
            pass
        if humidity_status.find('OK') == -1 and self._database.check_notification_status() == 1:
            self._database.update_daily_notification(humidity_status)
            self._notification.push_notification(
                "{}. Current Humidity: {} %".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                                    humidity), humidity_status)
        else:
            pass

        # If temperature or humidity is out of range, red led will light up. If not, green led will light up.
        # if temp_status.find('OK') == -1 or humidity_status.find('OK') == -1:
        #     self._led.red_light_on()
        # else:
        #     self._led.green_light_on()


monitor = GreenHouseMonitor()
monitor.main()

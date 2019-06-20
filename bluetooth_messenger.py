import bluetooth
import datetime
from sense_hat import SenseHat
from monitorAndNotify import GreenHouseMonitor
from database import Database
from data_checker import Checker
from notification import Notification

# print("performing inquiry...")
#
# nearby_devices = bluetooth.discover_devices(
#         duration=8, lookup_names=True, flush_cache=True, lookup_class=False)
#
# print("found %d devices" % len(nearby_devices))
#
# for addr, name in nearby_devices:
#     try:
#         print("  %s - %s" % (addr, name))
#     except UnicodeEncodeError:
#         print("  %s - %s" % (addr, name.encode('utf-8', 'replace')))


class BlueToothMessenger:
    def __init__(self):
        self._sense = SenseHat()
        self._database = Database()
        self._checker = Checker()
        self._notification = Notification()
        self._MY_PHONE_MAC_ADDRESS = '48:60:5F:CA:EC:6F'

    @staticmethod
    def search_nearby_devices():
        print('fdas')

    def send_message(self):
        mac_address = None
        print('gfjh')
        nearby_devices = bluetooth.discover_devices(duration=8)
        print(nearby_devices)
        for address in nearby_devices:
            if address == self._MY_PHONE_MAC_ADDRESS:
                mac_address = address
                device_name = bluetooth.lookup_name(mac_address, timeout=7)
                print("Found {} with MAC address: {}".format(device_name, mac_address))
                break

        if mac_address is not None:
            temperature = round(self._sense.get_temperature(), 1)
            calibrated_temp = GreenHouseMonitor.calibrate_temp(temperature)
            humidity = round(self._sense.get_humidity(), 1)
            time = datetime.datetime.now()

            temp_status = self._checker.check_temperature(GreenHouseMonitor.calibrate_temp(temperature))
            humidity_status = self._checker.check_humidity(humidity)

            """If the return value does not contain OK meaning temperature or humidity or both are out of range, and if
            the status value in database is 'OK', a notification will be sent"""
            if temp_status.find('OK') == -1:
                self._notification.push_notification(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), temp_status)
            if humidity_status.find('OK') == -1:
                self._notification.push_notification(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                                     humidity_status)


print('fdasfdas')
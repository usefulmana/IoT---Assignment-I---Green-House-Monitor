import bluetooth
import datetime
from virtual_sense_hat import VirtualSenseHat
from database import Database
from data_checker import Checker
from notification import Notification
from temperature_calibrator import Calibrator
import subprocess as sp


class BlueToothMessenger:
    """ This class is responsible for detecting nearby BlueTooth devices with a predetermined set of MAC addresses.
    And then it will trigger a notification to that device. Rename because of its and conflicts with a package"""
    _instance = None
    @staticmethod
    def get_instance():
        if BlueToothMessenger._instance is None:
            BlueToothMessenger()
        return BlueToothMessenger._instance

    def __init__(self):
        if BlueToothMessenger._instance is not None:
            raise Exception("This class is a singleton")
        else:
            BlueToothMessenger._instance = self
            self._sense = VirtualSenseHat.getSenseHat()
            self._database = Database.get_instance()
            self._checker = Checker()
            self._notification = Notification.get_instance()

    @staticmethod
    def get_list_of_paired_devices():
        # Getting list of paired devices
        p = sp.Popen(["bt-device", "--list"], stdin=sp.PIPE, stdout=sp.PIPE, close_fds=True)
        (stdout, stdin) = (p.stdout, p.stdin)
        # Reading response from RPi
        data = stdout.readlines()

        mac_addresses = []
        for d in data[1:]:
            # String manipulation to extract paired devices' MAC address
            mac_addresses.append(str(d).split(" ")[1][1:18])
        # Return all paired devices' MAC addresses
        return mac_addresses

    def send_message(self):
        mac_address = BlueToothMessenger.get_instance().get_list_of_paired_devices()
        nearby_devices = bluetooth.discover_devices(duration=8)
        # Check if the paired device has its BlueTooth enabled
        for address in nearby_devices:
            if address in mac_address:
                mac_address = address
                device_name = bluetooth.lookup_name(mac_address, timeout=8)
                print("Found {} with MAC address: {}".format(device_name, mac_address))
                break

        if mac_address is not None:
            # Get data from sense HAT
            temperature = round(self._sense.get_temperature(), 1)
            calibrated_temp = Calibrator.get_instance().calibrate_temperature(temperature)
            humidity = round(self._sense.get_humidity(), 1)

            # Check if data is within range
            temp_status = self._checker.check_temperature(calibrated_temp)
            humidity_status = self._checker.check_humidity(humidity)

            """If the return value does not contain OK meaning temperature or humidity or both are out of range, and if
            the status value in database is 'OK', a notification will be sent"""
            if temp_status.find('OK') == -1:
                self._notification.push_notification(
                    "{}. Current Temperature: {} C".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                                           calibrated_temp), temp_status)
            else:
                self._notification.push_notification(
                    "{}. Current Temperature: {} C".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                                           calibrated_temp), 'OK')
            if humidity_status.find('OK') == -1:
                self._notification.push_notification(
                    "{}. Current Humidity: {} %".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                                        humidity),
                    humidity_status)
            else:
                self._notification.push_notification(
                    "{}. Current Humidity: {} %".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                                        humidity), 'OK')


if __name__ == '__main__':
    messenger = BlueToothMessenger.get_instance()
    messenger.send_message()

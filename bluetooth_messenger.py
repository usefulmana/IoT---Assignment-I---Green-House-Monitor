import bluetooth
import datetime
from virtual_sense_hat import VirtualSenseHat
from database import Database
from data_checker import Checker
from notification import Notification
from temperature_calibrator import Calibrator


class BlueToothMessenger:
    """ This class is responsible for detecting nearby BlueTooth devices with a predetermined set of MAC addresses.
    And then it will trigger a notification to that device. Rename because of its and conflicts with a package"""
    def __init__(self):
        self._sense = VirtualSenseHat.getSenseHat()
        self._database = Database.get_instance()
        self._checker = Checker()
        self._notification = Notification.get_instance()
        self._MY_PHONE_MAC_ADDRESS = '48:60:5F:CA:EC:6F'
        self._LAPTOP_MAC_ADDRESS = '00:28:F8:37:FA:F9'

    def send_message(self):
        mac_address = None
        nearby_devices = bluetooth.discover_devices(duration=8)
        for address in nearby_devices:
            if address == self._MY_PHONE_MAC_ADDRESS or address == self._LAPTOP_MAC_ADDRESS:
                mac_address = address
                device_name = bluetooth.lookup_name(mac_address, timeout=7)
                print("Found {} with MAC address: {}".format(device_name, mac_address))
                break
        # sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        # port = 1
        # sock.connect((self._MY_PHONE_MAC_ADDRESS, port))
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


messenger = BlueToothMessenger()
messenger.send_message()

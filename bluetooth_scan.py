import bluetooth
from sense_hat import SenseHat


class BluetoothScanner:
    def __init__(self):
        self._paired_address = '44:1C:A8:E4:30:2E'
        self._port = 1
        self._socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

    # ===================================================================
    # Scan for nearby Bluetooth devices
    # ===================================================================

    def scan_devices(self):
        print('Scanning for nearby devices...')
        nearby_devices = bluetooth.discover_devices(lookup_names=True)
        print('Found {} nearby device(s).'.format(len(nearby_devices)))

        for address, name in nearby_devices:
            print('- Address: {} \t Name: {}'.format(address, name))

    # ===================================================================
    # Retrieve temperature and humidity values
    # ===================================================================

    def get_sensors_message(self):
        # Get sensor values
        sense = SenseHat()
        temperature = sense.get_temperature()
        humidity = sense.get_humidity()

        # Create message to be sent
        message = 'Temperature: {} - Humidity: {}\r\n'.format(temperature, humidity)
        return message

    # ===================================================================
    # Send message over Bluetooth
    # ===================================================================

    def send_message(self):
        self._socket.connect((self._paired_address, self._port))
        messsage = self.get_sensors_message()
        print('Sending message: {}'.format(messsage))
        self._socket.send(messsage.encode())


bluetooth_scanner = BluetoothScanner()
bluetooth_scanner.scan_devices()
bluetooth_scanner.send_message()

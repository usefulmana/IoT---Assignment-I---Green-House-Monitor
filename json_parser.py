import json


class Parser:
    def __init__(self):
        self._filename = 'config.json'

        with open(self._filename, 'r') as file:
            data = json.load(file)

        self._MIN_HUMIDITY = data['min_humidity']
        self._MAX_HUMIDITY = data['max_humidity']
        self._MIN_TEMPERATURE = data['min_temperature']
        self._MAX_TEMPERATURE = data['max_temperature']
        self._REFRESH_RATE = data['refresh_rate']

    @property
    def min_humidity(self):
        return self._MIN_HUMIDITY

    @property
    def max_humidity(self):
        return self._MAX_HUMIDITY

    @property
    def min_temperature(self):
        return self._MIN_TEMPERATURE

    @property
    def max_temperature(self):
        return self._MAX_TEMPERATURE

    @property
    def refresh_rate(self):
        return self._REFRESH_RATE



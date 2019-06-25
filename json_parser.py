import json


class Parser:

    """This class will parse a json config file save its content as properties."""
    _instance = None
    # Only one instance of this class should exist
    @staticmethod
    def get_instance():
        if Parser._instance is None:
            Parser()
        return Parser._instance

    def __init__(self):
        if Parser._instance is not None:
            raise Exception("This class is singleton")
        else:
            Parser._instance = self
            self._filename = 'config.json'
            with open(self._filename, 'r') as file:
                data = json.load(file)
            self._MIN_HUMIDITY = data['min_humidity']
            self._MAX_HUMIDITY = data['max_humidity']
            self._MIN_TEMPERATURE = data['min_temperature']
            self._MAX_TEMPERATURE = data['max_temperature']
            self._NUMBER_OF_DAYS_IN_REPORT = data['number_of_days_in_report']

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
    def number_of_days_in_report(self):
        return self._NUMBER_OF_DAYS_IN_REPORT


# parser = Parser()
# print(parser)
#
# parser1 = Parser()
# print(parser1)

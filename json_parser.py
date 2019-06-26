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
            self._config = 'config.json'
            self._setup = 'setup.json'
            with open(self._config, 'r') as file:
                configs = json.load(file)
            self._MIN_HUMIDITY = configs['min_humidity']
            self._MAX_HUMIDITY = configs['max_humidity']
            self._MIN_TEMPERATURE = configs['min_temperature']
            self._MAX_TEMPERATURE = configs['max_temperature']
            self._NUMBER_OF_DAYS_IN_REPORT = configs['number_of_days_in_report']
            with open(self._setup, 'r') as file:
                setup = json.load(file)
            self._DATABASE_NAME = setup['database_name']
            self._HOST = setup['host']
            self._USER = setup['user']
            self._PASSWORD = setup['password']
            self._API_KEY = setup['API_KEY']

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
        return int(abs(self._NUMBER_OF_DAYS_IN_REPORT))

    @property
    def database_name(self):
        return self._DATABASE_NAME

    @property
    def host(self):
        return self._HOST

    @property
    def user(self):
        return self._USER

    @property
    def password(self):
        return self._PASSWORD

    @property
    def api_key(self):
        return self._API_KEY


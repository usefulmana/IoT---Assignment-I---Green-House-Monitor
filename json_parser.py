import json


def parse_json(file_name):
    """Parsing a json file and returning a dictionary object"""
    with open(file_name, 'r') as data:
        return json.load(data)


class Parser:
    def __init__(self):
        self.filename = 'config.json'

        with open(self.filename, 'r') as file:
            data = json.load(file)

        self.MIN_HUMIDITY = data['min_humidity']
        self.MAX_HUMIDITY = data['max_humidity']
        self.MIN_TEMPERATURE = data['min_temperature']
        self.MAX_TEMPERATURE = data['max_temperature']


import json


def parse_json(file_name):
    """Parsing a json file and returning a dictionary object"""
    with open(file_name, 'r') as data:
        data_store = json.load(data)
        return data_store

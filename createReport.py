import pandas as pd
import sqlite3
import json


class Report:
    def __init__(self):
        self._config = self.read_config()

    # ===============================================================================
    # Read config from JSON file
    # ===============================================================================

    @staticmethod
    def read_config():
        with open('config.json') as config_file:
            config = json.load(config_file)

        return config

    # ===============================================================================
    # Main function
    # ===============================================================================

    def get_day_status(self, day_record):
        # Extract number of temperature values out of range
        upper_temp = day_record[day_record['temperature'] > self._config['max_temperature']].shape[0]
        lower_temp = day_record[day_record['temperature'] < self._config['min_temperature']].shape[0]

        # Extract number of humidity values out of range
        upper_hum = day_record[day_record['humidity'] > self._config['max_humidity']].shape[0]
        lower_hum = day_record[day_record['humidity'] < self._config['min_humidity']].shape[0]

        if sum([upper_temp, lower_temp, upper_hum, lower_hum]) == 0:
            return 'OK'
        else:
            high_temp = 'BAD: {} above max temperature'.format(upper_temp)
            low_temp = '{} below min temperature'.format(lower_temp)
            high_hum = '{} above max humidity'.format(upper_hum)
            low_hum = '{} below min humidity'.format(lower_hum)
            return ' - '.join([high_temp, low_temp, high_hum, low_hum])

    # ===============================================================================
    # Main function
    # ===============================================================================

    def generate_report(self):
        # Fetch data from database
        db = sqlite3.connect('greenhouse.db')
        db_contents = pd.read_sql_query('select * from GREENHOUSE_DATA', db)

        # Initialise report dataframe
        report = pd.DataFrame(columns=['Date', 'Status'])

        # Only keep date, drop time, get set of unique dates
        db_contents['time_stamp'] = db_contents['time_stamp'].apply(lambda x: x.split()[0])
        dates = list(set(db_contents['time_stamp']))

        for day in dates:
            # Get data of the considered day
            day_record = db_contents[db_contents['time_stamp'] == day]
            status = self.get_day_status(day_record=day_record)
            report = report.append({'Date': day, 'Status': status}, ignore_index=True)

        report.to_csv('report.csv', index=False)


report = Report()
report.generate_report()

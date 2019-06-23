from matplotlib import pyplot as plt
import pandas as pd
from json_parser import Parser
import numpy as np


# import seaborn as sb

class Analytics:
    def __init__(self):
        self.parser = Parser()

    def matplotlib_draw_temperature_report(self):
        weekly_data = pd.read_csv('detailed_data.csv')
        avg_temp = weekly_data.avg_temp
        min_temp = weekly_data.min_temp
        max_temp = weekly_data.max_temp

        # fig, ax1 = plt.subplots()
        # ax2 = ax1.twinx()
        plt.style.use('bmh')
        plt.scatter(weekly_data.date, avg_temp, c='g', label='Avg Temp')
        plt.axhline(y=self.parser.max_temperature, c='r', label='Max')
        plt.axhline(y=self.parser.min_temperature, c='b', label='Min')
        plt.plot(weekly_data.date, avg_temp, 'g-', label='_nolegend_')
        err = [avg_temp - min_temp, max_temp - avg_temp]
        plt.errorbar(weekly_data.date, avg_temp, yerr=err, fmt='go', label='_nolegend_')

        # ax2.scatter(weekly_data.date, avg_humid)
        # ax2.plot(weekly_data.date, avg_humid, label='Humidity')
        axes = plt.gca()
        axes.set_ylim([10, 40])
        plt.title('Temperature Report')
        plt.ylabel('Temperature (*C)', color='r')
        plt.xlabel('Date')
        plt.legend(loc='upper right')
        plt.savefig('matplotlib_temp_report.png')
        plt.clf()

    def matplotlib_draw_humidity_report(self):
        weekly_data = pd.read_csv('detailed_data.csv')
        avg_humid = weekly_data.avg_humid
        min_humid = weekly_data.min_humid
        max_humid = weekly_data.max_humid

        plt.style.use('bmh')
        plt.scatter(weekly_data.date, weekly_data.avg_humid, c='g', label='Avg Humidity')
        plt.axhline(y=self.parser.max_humidity, c='r', label='Max')
        plt.axhline(y=self.parser.min_humidity, c='b', label='Min')
        plt.plot(weekly_data.date, weekly_data.avg_humid, 'g-', label='_nolegend_')
        err = [avg_humid - min_humid, max_humid - avg_humid]
        plt.errorbar(weekly_data.date, avg_humid, yerr=err, fmt='go', label='_nolegend_')

        axes = plt.gca()
        axes.set_ylim([15, 90])
        plt.title('Humidity Report')
        plt.ylabel('Humidity (%)', color='b')
        plt.xlabel('Date')
        plt.legend(loc='upper right')
        plt.savefig('matplotlib_humid_report.png')
        plt.clf()

    def seaborn_draw_temperature_report(self):
        daily_data = pd.read_csv('daily_report.csv')
        parser = Parser()
        frame1 = plt.gca()
        temperature = daily_data.temperature
        last_index = daily_data.index[-1]
        col = np.where(temperature > parser.max_temperature, 'r',
                       np.where(temperature < parser.min_temperature, 'r', 'g'))
        plt.scatter(daily_data.date, temperature, c=col, label='_nolegend_')
        plt.axhline(y=self.parser.max_temperature, c='r', label='Max')
        plt.axhline(y=self.parser.min_temperature, c='r', label='Min')
        frame1.axes.get_xaxis().set_ticks([])
        plt.title('Temperature report {} {} to {}'.format('\n', daily_data.date[0], daily_data.date[last_index]))
        plt.savefig('seaborn_temperature_daily_report.png')
        plt.clf()

    def seaborn_draw_humidity_report(self):
        daily_data = pd.read_csv('daily_report.csv')
        parser = Parser()
        frame1 = plt.gca()
        humidity = daily_data.humidity
        last_index = daily_data.index[-1]
        col = np.where(humidity > parser.max_humidity, 'r', np.where(humidity < parser.min_humidity, 'r', 'g'))
        plt.scatter(daily_data.date, humidity, c=col, label='_nolegend_')
        plt.axhline(y=self.parser.max_humidity, c='r', label='Max')
        plt.axhline(y=self.parser.min_humidity, c='r', label='Min')
        frame1.axes.get_xaxis().set_ticks([])
        plt.title('Humidity report {} {} to {}'.format('\n', daily_data.date[0], daily_data.date[last_index]))
        plt.savefig('seaborn_humid_daily_report.png')
        plt.clf()


analytics = Analytics()
analytics.matplotlib_draw_humidity_report()
analytics.matplotlib_draw_temperature_report()
analytics.seaborn_draw_temperature_report()
analytics.seaborn_draw_humidity_report()

from matplotlib import pyplot as plt
import pandas as pd
from json_parser import Parser
import numpy as np
import seaborn as sns


class Analytics:
    def __init__(self):
        self.parser = Parser.get_instance()

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
        frame1 = plt.gca()
        temperature = daily_data.temperature
        last_index = daily_data.index[-1]
        col = np.where(temperature > self.parser.max_temperature, 'r',
                       np.where(temperature < self.parser.min_temperature, 'r', 'g'))
        plt.scatter(daily_data.date, temperature, c=col, label='_nolegend_')
        plt.axhline(y=self.parser.max_temperature, c='r', label='Max')
        plt.axhline(y=self.parser.min_temperature, c='r', label='Min')
        frame1.axes.get_xaxis().set_ticks([])
        plt.title('Temperature report {} {} to {}'.format('\n', daily_data.date[0], daily_data.date[last_index]))
        plt.savefig('seaborn_temperature_daily_report.png')
        plt.clf()

    def seaborn_draw_humidity_report(self):
        daily_data = pd.read_csv('daily_report.csv')
        frame1 = plt.gca()
        humidity = daily_data.humidity
        last_index = daily_data.index[-1]
        col = np.where(humidity > self.parser.max_humidity, 'r',
                       np.where(humidity < self.parser.min_humidity, 'r', 'g'))
        plt.scatter(daily_data.date, humidity, c=col, label='_nolegend_')
        plt.axhline(y=self.parser.max_humidity, c='r', label='Max')
        plt.axhline(y=self.parser.min_humidity, c='r', label='Min')
        frame1.axes.get_xaxis().set_ticks([])
        plt.title('Humidity report {} {} to {}'.format('\n', daily_data.date[0], daily_data.date[last_index]))
        plt.savefig('seaborn_humid_daily_report.png')
        plt.clf()

    def seaborn_test(self):
        l = [41, 44, 46, 46, 47, 47, 48, 48, 49, 51, 52, 53, 53, 53, 53, 55, 55, 55,
             55, 56, 56, 56, 56, 56, 56, 57, 57, 57, 57, 57, 57, 57, 57, 58, 58, 58,
             58, 59, 59, 59, 59, 59, 59, 59, 59, 60, 60, 60, 60, 60, 60, 60, 60, 61,
             61, 61, 61, 61, 61, 61, 61, 61, 61, 61, 62, 62, 62, 62, 62, 62, 62, 62,
             62, 63, 63, 63, 63, 63, 63, 63, 63, 63, 64, 64, 64, 64, 64, 64, 64, 65,
             65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 66, 66, 66, 66, 66, 66, 66,
             67, 67, 67, 67, 67, 67, 67, 67, 68, 68, 68, 68, 68, 69, 69, 69, 70, 70,
             70, 70, 71, 71, 71, 71, 71, 72, 72, 72, 72, 73, 73, 73, 73, 73, 73, 73,
             74, 74, 74, 74, 74, 75, 75, 75, 76, 77, 77, 78, 78, 79, 79, 79, 79, 80,
             80, 80, 80, 81, 81, 81, 81, 83, 84, 84, 85, 86, 86, 86, 86, 87, 87, 87,
             87, 87, 88, 90, 90, 90, 90, 90, 90, 91, 91, 91, 91, 91, 91, 91, 91, 92,
             92, 93, 93, 93, 94, 95, 95, 96, 98, 98, 99, 100, 102, 104, 105, 107, 108,
             109, 110, 110, 113, 113, 115, 116, 118, 119, 121]

        sns.distplot(l, kde=True, rug=False)
        plt.show()
        # plot.savefig('test.png')
        plt.clf()


analytics = Analytics()
analytics.matplotlib_draw_humidity_report()
analytics.matplotlib_draw_temperature_report()
analytics.seaborn_draw_temperature_report()
analytics.seaborn_draw_humidity_report()
analytics.seaborn_test()

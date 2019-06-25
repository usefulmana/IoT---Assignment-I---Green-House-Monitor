import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3

from createReport import Report


class DataVisualiser:
    def __init__(self):
        # self._db = sqlite3.connect('greenhouse.db')
        # self._df = pd.read_sql_query('select * from GREENHOUSE_DATA', self._db)
        self._df = pd.read_csv('daily_report.csv')
        self._config = Report.read_config()

    def plot_pyplot(self):
        # Create figure with 2 subplots
        fig, (ax_temp, ax_hum) = plt.subplots(1, 2, figsize=(12, 6))

        # Red line chart for temperature
        ax_temp.set_title('Temperature')
        ax_temp.set_ylabel('Degree C')
        ax_temp.plot(self._df['temperature'], color='red', label='Recorded temperature')
        self.draw_constant_line(ax=ax_temp, mode='temperature')

        # Blue line chart for humidity
        ax_hum.plot(self._df['humidity'], color='blue')
        ax_hum.set_title('Humidity')
        ax_hum.set_ylabel('%')
        self.draw_constant_line(ax=ax_temp, mode='humidity')

        # Tight layout to avoid overlaps
        plt.tight_layout()
        fig.suptitle('Data Visualisation with Matplotlib', y=1.12)
        plt.legend()
        plt.show()

    def draw_constant_line(self, ax, mode):
        ax.axhline(y=self._config['max_{}'.format(mode)], color='yellow',
                   linestyle='dashed', label='Upper threshold')
        ax.axhline(y=self._config['min_{}'.format(mode)], color='yellow',
                   linestyle='dashed', label='Lower threshold')



data_visualiser = DataVisualiser()
data_visualiser.plot_pyplot()

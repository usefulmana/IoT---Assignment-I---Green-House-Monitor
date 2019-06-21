import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns
import sqlite3


class DataVisualiser:
    def __init__(self):
        self._db = sqlite3.connect('greenhouse.db')
        self._df = pd.read_sql_query('select * from GREENHOUSE_DATA', self._db)

    def plot_pyplot(self):
        # Create figure with 2 subplots
        fig, (ax_temp, ax_hum) = plt.subplots(1, 2)

        # Red line chart for temperature
        ax_temp.plot(self._df['temperature'], 'tab:red')
        ax_temp.set_title('Temperature')
        ax_temp.set_ylabel('Degree C')

        # Blue line chart for humidity
        ax_hum.plot(self._df['humidity'], 'tab:blue')
        ax_hum.set_title('Humidity')
        ax_hum.set_ylabel('%')

        # Tight layout to avoid overlaps
        plt.tight_layout()
        fig.suptitle('Data Visualisation with Matplotlib', y=1.12)
        plt.show()


data_visualiser = DataVisualiser()
data_visualiser.plot_pyplot()

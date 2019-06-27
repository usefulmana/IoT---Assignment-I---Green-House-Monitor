import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json


class DataVisualiser:
    def __init__(self):
        self._df = pd.read_csv('daily_report.csv')

        with open('config.json') as config_file:
            self._config = json.load(config_file)

    def visualise_report(self, using_plt=True):
        # Using Seaborn style if specified
        if not using_plt:
            sns.set()

        # Create figure with 2 subplots
        fig, (ax_temp, ax_hum) = plt.subplots(1, 2, figsize=(12, 6))

        # Attributes for each axes including titles and labels
        ax_temp.set_title('Temperature')
        ax_hum.set_title('Humidity')

        # Option to use Matplotlib or Seaborn library
        if using_plt:
            self.plot_pyplot(fig=fig, ax_temp=ax_temp, ax_hum=ax_hum)
        else:
            sns.set()
            self.plot_seaborn(fig=fig, ax_temp=ax_temp, ax_hum=ax_hum)

        plt.show()

    # ==================================================================================
    # Visualisation with Matplotlib
    # ==================================================================================

    def plot_pyplot(self, fig, ax_temp, ax_hum):
        # Red line chart for temperature
        ax_temp.plot(self._df['temperature'], color='red', label='Recorded temperature')
        ax_temp.set_ylabel('Degree C')
        self.draw_constant_line(ax=ax_temp, mode='temperature')

        # Blue line chart for humidity
        ax_hum.plot(self._df['humidity'], color='blue')
        ax_hum.set_ylabel('%')
        self.draw_constant_line(ax=ax_hum, mode='humidity')

        # Set figure's title
        fig.suptitle('Data Visualisation with Matplotlib', fontsize=20)

        # Save figure as PNG image file
        plt.savefig('visualise_matplotlib.png')

    # ==================================================================================
    # Visualisation with Seaborn
    # ==================================================================================

    def plot_seaborn(self, fig, ax_temp, ax_hum):
        # Red line chart for temperature
        sns.lineplot(x='index', y='temperature', color='red', label='Temperature',
                     data=self._df.reset_index(), ax=ax_temp)
        ax_temp.set_ylabel('Degree C')
        self.draw_constant_line(ax=ax_temp, mode='temperature')

        # Blue line chart for humidity
        sns.lineplot(x='index', y='humidity', color='blue', label='Humidity',
                     data=self._df.reset_index(), ax=ax_hum)
        ax_hum.set_ylabel('%')
        self.draw_constant_line(ax=ax_hum, mode='humidity')

        # Set figure's title
        fig.suptitle('Data Visualisation with Seaborn', fontsize=20)

        # Save figure as PNG image file
        plt.savefig('visualise_seaborn.png')

    # ==================================================================================
    # Visualisation with Seaborn
    # ==================================================================================

    def draw_constant_line(self, ax, mode):
        ax.axhline(y=self._config['max_{}'.format(mode)], color='green', linewidth=1,
                   linestyle='dashed', label='Upper threshold')
        ax.axhline(y=self._config['min_{}'.format(mode)], color='olive', linewidth=1,
                   linestyle='dashed', label='Lower threshold')
        ax.legend()
        ax.get_xaxis().set_visible(False)


data_visualiser = DataVisualiser()
data_visualiser.visualise_report(using_plt=True)
data_visualiser.visualise_report(using_plt=False)

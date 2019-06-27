import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json


class DataVisualiser:
    def __init__(self):
        self._df = pd.read_csv('daily_report.csv')
        self._start_date = self._df.loc[0, 'date']
        self._end_date = self._df.loc[self._df.shape[0] - 1, 'date']

        with open('config.json') as config_file:
            self._config = json.load(config_file)

    # ==================================================================================

    def visualise_report(self, using_plt=True):
        """
            Generate graphs, show figures and save as PNG file
        @using_plt: True to plot with Matplotlib, False to plot with Seaborn
        """
        # Using Seaborn style if specified
        if not using_plt:
            sns.set()
            sns.set_palette('husl')

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

    def plot_pyplot(self, fig, ax_temp, ax_hum):
        """
            Visualisation with Matplotlib
        -------------------------------------------------
        @fig: Figure object to contain plots
        @ax_temp: Subplot object for temperature plot
        @ax_hum: Subplot object for humidity plot
        """
        # Red line chart for temperature
        ax_temp.plot(self._df['temperature'], color='red', label='Recorded temperature')
        ax_temp.set_ylabel('Degree C')
        self.draw_constant_line(ax=ax_temp, mode='temperature')

        # Blue line chart for humidity
        ax_hum.plot(self._df['humidity'], color='blue')
        ax_hum.set_ylabel('%')
        self.draw_constant_line(ax=ax_hum, mode='humidity')

        # Set figure's title
        fig_title = 'Data Visualisation with Matplotlib from {} to {}'.format(self._start_date, self._end_date)
        fig.suptitle(fig_title, fontsize=16)

        # Save figure as PNG image file
        plt.savefig('visualise_matplotlib.png')

    def draw_constant_line(self, ax, mode):
        """
            Draw constant horizontal line as value thresholds
        ------------------------------------------------------
        @ax: Subplot object
        @mode: Either 'temperature' or 'humidity'
        """
        ax.axhline(y=self._config['max_{}'.format(mode)], color='green', linewidth=1,
                   linestyle='dashed', label='Upper threshold')
        ax.axhline(y=self._config['min_{}'.format(mode)], color='olive', linewidth=1,
                   linestyle='dashed', label='Lower threshold')
        ax.legend()
        ax.get_xaxis().set_visible(False)

    # ==================================================================================

    def plot_seaborn(self, fig, ax_temp, ax_hum):
        """
            Visualisation with Seaborn
        -------------------------------------------------
        @fig: Figure object to contain plots
        @ax_temp: Subplot object for temperature plot
        @ax_hum: Subplot object for humidity plot
        """
        self._df['max_temp'] = self._config['max_temperature']
        self._df['min_temp'] = self._config['min_temperature']
        self._df['max_hum'] = self._config['max_humidity']
        self._df['min_hum'] = self._config['min_humidity']

        # Red line chart for temperature
        with sns.color_palette('husl'):
            sns.lineplot(data=self._df[['temperature', 'min_temp', 'max_temp']], ax=ax_temp)
            ax_temp.legend(['Temperature', 'Upper threshold', 'Lower threshold'])
            ax_temp.set_ylabel('Degree C')

        # Blue line chart for humidity
        with sns.color_palette('GnBu_d'):
            sns.lineplot(data=self._df[['humidity', 'min_hum', 'max_hum']], ax=ax_hum)
            ax_hum.legend(['Temperature', 'Upper threshold', 'Lower threshold'])
            ax_hum.set_ylabel('%')

        # Set figure's title
        fig_title = 'Data Visualisation with Seaborn from {} to {}'.format(self._start_date, self._end_date)
        fig.suptitle(fig_title, fontsize=16)

        # Save figure as PNG image file
        plt.savefig('visualise_seaborn.png')

# =======================================================================================


if __name__ == '__main__':
    data_visualiser = DataVisualiser()
    data_visualiser.visualise_report(using_plt=True)
    data_visualiser.visualise_report(using_plt=False)

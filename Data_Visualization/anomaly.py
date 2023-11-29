"This script defines a function to calculate anomolies in the data"
import pandas as pd
import pytimetk

# Load data
data = pd.read_csv('/Users/benjaminmakhlouf/Desktop/Merged.csv')
data['Time'] = pd.to_datetime(data['Time'])

# Filter data to include only the "Temperature" variable
data = data[data['variable'] == 'Relative Humidity']


def calculate_and_plot_anomalies(data, date_column, value_column, period, iqr_alpha, clean_alpha, clean, engine, title):
    """
    This function calculates and plots anomalies in time series data.
    Inputs: Time series data with one variable chosen,
            date_column: the column name for the date/time variable,
            value_column: the column name for the variable to be analyzed,
            period: the period of the time series (e.g. 7 for weekly, 12 for monthly),
            iqr_alpha: the alpha value for the interquartile range,
            clean_alpha: the alpha value for the cleaning,
            clean: the type of cleaning (e.g. 'min_max'),
            engine: the plotting engine (e.g. 'plotly'),
            title: the title of the plot.
    Outputs: Two plots, one of the seasonal decomposition and one of the anomalies.
    """
    anomalize_df = pytimetk.anomalize(
        data=data,
        date_column=date_column,
        value_column=value_column,
        period=period,
        iqr_alpha=iqr_alpha,  # using the default
        clean_alpha=clean_alpha,  # using the default
        clean=clean
    )

    fig1 = pytimetk.plot_anomalies_decomp(
        data=anomalize_df,
        date_column=date_column,
        engine=engine,
        title=title
    )

    fig2 = pytimetk.plot_anomalies(
        data=anomalize_df,
        date_column=date_column,
        engine=engine,
        title=title
    )

    return fig1, fig2
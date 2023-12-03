import pandas as pd
import plotly.io as pio
import pytimetk

data = pd.read_csv('/Users/benjaminmakhlouf/Desktop/daily_tidy_all_data.csv')
data['times'] = pd.to_datetime(data['times'])
data = data[data['parameter'] == 'Air_Temperature']
data = data.dropna(subset=['value_mean']).query('value_mean != 0')

print(data)
#### Data should be queried before it gets to the functions 


def create_trendline(data):
    """
    Create a trendline plot for the given data.

    Args:
        data (pandas.DataFrame): The input data containing the 'times' and 'value_mean' columns.

    Raises:
        ValueError: If the 'times' or 'value_mean' column does not exist in the data.
        ValueError: If the 'times' column is not a datetime object.
        ValueError: If there is no data in either the 'times' or 'value_mean' column.
        ValueError: If there is a non-numeric value in the 'value_mean' column.

    Returns:
        None
    """
    if 'times' not in data.columns or 'value_mean' not in data.columns:
        raise ValueError("The 'times' or 'value_mean' column does not exist in the data.")

    if data['times'].dtype != 'datetime64[ns]':
        raise ValueError("The 'times' column is not a datetime object.")

    if data['times'].empty or data['value_mean'].empty:
        raise ValueError("There is no data in either the 'times' or 'value_mean' column.")

    if not pd.to_numeric(data['value_mean'], errors='coerce').notnull().all():
        raise ValueError("There is a non-numeric value in the 'value_mean' column.")

    fig = pytimetk.plot_timeseries(
        data=data,
        date_column='times',
        value_column='value_mean'
    )
    pio.show(fig)


create_trendline(data)





def create_anomaly_graph(data):
    """
    Create an anomaly graph with anomaly detection and plot.

    Args:
        data (pandas.DataFrame): The input data containing the 'times' and 'value_mean' columns.

    Raises:
        ValueError: If the 'times' or 'value_mean' column does not exist in the data.
        ValueError: If the 'times' column is not a datetime object.
        ValueError: If there is no data in either the 'times' or 'value_mean' column.
        ValueError: If there is a non-numeric value in the 'value_mean' column.

    Returns:
        None
    """
    if 'times' not in data.columns or 'value_mean' not in data.columns:
        raise ValueError("The 'times' or 'value_mean' column does not exist in the data.")

    if data['times'].dtype != 'datetime64[ns]':
        raise ValueError("The 'times' column is not a datetime object.")

    if data['times'].empty or data['value_mean'].empty:
        raise ValueError("There is no data in either the 'times' or 'value_mean' column.")

    if not pd.to_numeric(data['value_mean'], errors='coerce').notnull().all():
        raise ValueError("There is a non-numeric value in the 'value_mean' column.")

    anomalize_df = pytimetk.anomalize(
        data=data,
        date_column='times',
        value_column='value_mean',
        period=7,
        iqr_alpha=0.05,
        clean_alpha=0.75,
        clean="min_max"
    )

    anomplot = pytimetk.plot_anomalies(
        data=anomalize_df,
        date_column='times',
        engine='plotly',
        title='Plot Anomaly Bands'
    )

    pio.show(anomplot)


create_anomaly_graph(data)



### Show the statistical decomposition of the anamoly graph 

def create_anomaly_decomp_graph(data):
    """
    Create an anomaly graph with anomaly detection and plot.

    Args:
        data (pandas.DataFrame): The input data containing the 'times' and 'value_mean' columns.

    Raises:
        ValueError: If the 'times' or 'value_mean' column does not exist in the data.
        ValueError: If the 'times' column is not a datetime object.
        ValueError: If there is no data in either the 'times' or 'value_mean' column.
        ValueError: If there is a non-numeric value in the 'value_mean' column.

    Returns:
        None
    """
    if 'times' not in data.columns or 'value_mean' not in data.columns:
        raise ValueError("The 'times' or 'value_mean' column does not exist in the data.")

    if data['times'].dtype != 'datetime64[ns]':
        raise ValueError("The 'times' column is not a datetime object.")

    if data['times'].empty or data['value_mean'].empty:
        raise ValueError("There is no data in either the 'times' or 'value_mean' column.")

    if not pd.to_numeric(data['value_mean'], errors='coerce').notnull().all():
        raise ValueError("There is a non-numeric value in the 'value_mean' column.")

    anomalize_df = pytimetk.anomalize(
        data=data,
        date_column='times',
        value_column='value_mean',
        period=7,
        iqr_alpha=0.05,
        clean_alpha=0.75,
        clean="min_max"
    )

    decomp=pytimetk.plot_anomalies_decomp(
    data        = anomalize_df,
    date_column = 'times',
    engine      = 'plotly',
    title       = 'Seasonal Decomposition'
)

pio.show(decomp)

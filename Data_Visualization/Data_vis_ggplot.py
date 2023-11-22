
"This script creates functions to produce data visualization using ggplot" 

import os
import pandas as pd
from plotnine import ggplot, aes, geom_point, labs, theme_minimal, geom_line, ggtitle, geom_smooth, ggsave

#Import test data frame
data = pd.read_csv('/Users/benjaminmakhlouf/Desktop/Merged.csv')
print(data.dtypes)
data['Time'] = pd.to_datetime(data['Time'])

def create_time_series_plot(data, time_period_start, time_period_end, frequency, plot_type):
    """
    Create a time series plot of a variable vs time using plotnine.

    Parameters:
    - data (pd.DataFrame): The DataFrame containing "Time", "Location", "variable", and "value" columns.
    - time_period_start (str): The start of the time period description.
    - time_period_end (str): The end of the time period description.
    - frequency (str): The frequency description.
    - plot_type (str): The type of plot to create ("scatter" or "line").

    Returns:
    - p (plotnine.ggplot): The time series plot.
    """
    # Check if the required columns are present in the DataFrame
    required_columns = ["Time", "Location", "variable", "value"]
    if not set(required_columns).issubset(data.columns):
        raise ValueError(f"The DataFrame must contain the following columns: {', '.join(required_columns)}.")

    # Create plot based on plot_type
    if plot_type == "scatter":
        p = ggplot(data, aes(x='Time', y='value', color='variable')) + \
            geom_point() + \
            ggtitle(f"{frequency} data from {time_period_start} to {time_period_end}")
    elif plot_type == "line":
        p = ggplot(data, aes(x='Time', y='value', color='variable')) + \
            geom_line() + \
            ggtitle(f"{frequency} data from {time_period_start} to {time_period_end}")
    else:
        raise ValueError("Invalid plot_type. Supported values are 'scatter' or 'line'.")

    # Check if the plot was successfully created
    if p is None:
        raise ValueError("Failed to create the time series plot.")

    return p


def trendline(data, time_period_start, time_period_end, frequency, trendline_type):
    """
    Add a trend line of the user's choice to the plot.

    Parameters:
    - data (pd.DataFrame): The DataFrame containing "Time", "Location", "variable", and "value" columns.
    - time_period_start (str): The start of the time period description.
    - time_period_end (str): The end of the time period description.
    - frequency (str): The frequency description.
    - trendline_type (str): The type of trendline to add ("LOESS" or "linear regression").

    Returns:
    - p (plotnine.ggplot): The scatter plot with the specified trendline.
    """

    # Check if the required columns are present in the DataFrame
    required_columns = ["Time", "Location", "variable", "value"]
    if not set(required_columns).issubset(data.columns):
        raise ValueError(f"The DataFrame must contain the following columns: {', '.join(required_columns)}.")

    # Create scatter plot
    p = ggplot(data, aes(x='Time', y='value', color='variable')) + \
        geom_line() + \
        ggtitle(f"{frequency} data from {time_period_start} to {time_period_end}")

    # Add trendline based on the specified type
    if trendline_type == "LOESS":
        p = p + geom_smooth(method="loess", se=False)  # You can customize se parameter as needed
    elif trendline_type == "linear regression":
        p = p + geom_smooth(method="lm", se=False)  # You can customize se parameter as needed
    else:
        raise ValueError("Invalid trendline_type. Supported values are 'LOESS' or 'linear regression'.")

    # Check if the plot was successfully created
    if p is None:
        raise ValueError("Failed to create the scatter plot.")

    return p


def export_plot(p, export_type):
    """
    Export the plot "p" as a .jpg or .pdf depending on the value of export_type to the user's downloads folder.

    Parameters:
    - p (plotnine.ggplot): The plot to export.
    - export_type (str): The type of export (".jpg" or ".pdf").

    Returns:
    - None
    """

    # Check if export_type is valid
    valid_export_types = [".jpg", ".pdf"]
    if export_type not in valid_export_types:
        raise ValueError(f"Invalid export_type. Supported values are {', '.join(valid_export_types)}.")

    # Get the user's downloads folder
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

    # Create the file path based on export_type
    file_path = os.path.join(downloads_folder, f"exported_plot{export_type}")

    # Save the plot using ggsave
    ggsave(p, file_path, device=export_type[1:], dpi=300)

    
"This code uses PyTimeTk to detect anomalies in time series data."

# Import libraries
import numpy as np
import pandas as pd
import plotly.io as pio


import pytimetk

# Load data
data = pd.read_csv('/Users/benjaminmakhlouf/Desktop/Merged.csv')
data['Time'] = pd.to_datetime(data['Time'])

#filter data to include only one variable
variable_name = 'your_variable_name'  # Replace 'your_variable_name' with the actual variable name
filtered_data = data[data['Variable'] == variable_name]


#plot the data to see the trend using Tk
fig = pytimetk.plot_timeseries(
    data=data,
    date_column = 'Time',
    value_column = 'value')

pio.show(fig)
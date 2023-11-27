
import streamlit as st

from data_vis import create_time_series_plot, trendline

def main():
    st.title("Lake Erie bouey data")

    # Sidebar with user input
    st.sidebar.header("Choose variables to plot")

    # Choose time period start and end based of unique values present in the data 
    time_period_start = st.sidebar.selectbox("Select Time Period Start", data['Time'].dt.strftime("%B %Y").unique())
    time_period_end = st.sidebar.selectbox("Select Time Period End", data['Time'].dt.strftime("%B %Y").unique())
    
    #Choose frequency and plot type based on predefined values
    frequency = st.sidebar.selectbox("Select Frequency", ["Daily", "Weekly", "Monthly", "Yearly"])
    plot_type = st.sidebar.selectbox("Select Plot Type", ["scatter", "line"])
    trendline_type = st.sidebar.selectbox("Select Trendline Type", ["None", "LOESS", "Linear Regression"])

    # Generate and display the plot
    if plot_type == "scatter":
        p = create_time_series_plot(data, time_period_start, time_period_end, frequency, "scatter")
    elif plot_type == "line":
        p = create_time_series_plot(data, time_period_start, time_period_end, frequency, "line")
  if trendline_type != "None":
        p = trendline(p, time_period_start, time_period_end, frequency, trendline_type)

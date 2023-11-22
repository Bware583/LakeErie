
import streamlit as st
import pandas as pd
from io import BytesIO
import base64

def main():
    st.title("Graphs")

    # Sidebar with user input
    st.sidebar.header("User Input")

    time_period_start = st.sidebar.selectbox("Select Time Period Start", data['Time'].dt.strftime("%B %Y").unique())
    time_period_end = st.sidebar.selectbox("Select Time Period End", data['Time'].dt.strftime("%B %Y").unique())
    frequency = st.sidebar.selectbox("Select Frequency", data['Frequency'].unique())
    plot_type = st.sidebar.selectbox("Select Plot Type", ["scatter", "line"])

    # Generate and display the plot
    if plot_type == "scatter":
        p = create_time_series_plot(data, time_period_start, time_period_end, frequency, "scatter")
    elif plot_type == "line":
        p = create_time_series_plot(data, time_period_start, time_period_end, frequency, "line")
    
    # Add trendline if desired
    trendline_type = st.sidebar.selectbox("Select Trendline Type", ["None", "LOESS", "Linear Regression"])
    if trendline_type != "None":
        p = trendline(p, time_period_start, time_period_end, frequency, trendline_type)

    # Display the plot
    st.pyplot(p)

    # Export the plot as a downloadable link
    st.sidebar.markdown("### Export Plot")
    export_type = st.sidebar.selectbox("Select Export Type", [".jpg", ".pdf"])
    if st.sidebar.button("Export Plot"):
        img_str = export_plot_to_base64(p)
        st.sidebar.markdown(f"![Exported Plot]({img_str})")
        st.markdown(f"### [Download Exported Plot]({img_str})")
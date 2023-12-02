import folium 

def map_main(selected_buoy):
    st.title("Simple Map with Leaflet")

    # Create a map object using Folium
    m = folium.Map(location=[latitude, longitude], zoom_start=13)

    # Define the buoy locations
    buoy_locations = [
        {"name": "Buoy 1", "latitude": 40.7128, "longitude": -74.0060},
        {"name": "Buoy 2", "latitude": 34.0522, "longitude": -118.2437},
        {"name": "Buoy 3", "latitude": 51.5074, "longitude": -0.1278},
        {"name": "Buoy 4", "latitude": 48.8566, "longitude": 2.3522},
        {"name": "Buoy 5", "latitude": 55.7558, "longitude": 37.6176},
        {"name": "Buoy 6", "latitude": -33.8651, "longitude": 151.2093}
    ]

    # Add markers for each buoy
    for buoy in buoy_locations:
        if buoy["name"] == selected_buoy:
            color = "red"
        else:
            color = "gray"
        folium.Marker([buoy["latitude"], buoy["longitude"]], popup=buoy["name"], icon=folium.Icon(color=color)).add_to(m)

    # Display the map using Streamlit
    folium_static(m)

if __name__ == "__main__":
    selected_buoy = "Buoy 3"  # Replace with the selected buoy name
    map_main(selected_buoy)